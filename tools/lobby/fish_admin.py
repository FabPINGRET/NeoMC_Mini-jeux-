"""🎣 Pêche à l'étang : administration (importé par gen_fish.py, jamais lancé seul) - coupure, compteurs, boutons, mg.opt 86 et 87.

Même mécanique que foot_admin.py (act, add_buttons et chat_line en viennent : aucune copie).
- mg.opt 86 : coupe / rétablit la pêche ($lfoff mg.st = 1 : coupée, absent : active). Couper : socle retiré (bloc remis à l'état d'origine du
  spawn, zone cliquable et panneau tués), cannes retirées, prises en cours abandonnées. Rétablir : socle reposé (lobby/fish/build).
- mg.opt 87 : compteurs d'usage (objectif mg.lfn : $rod cannes prises, $catch poissons, $gold dorés, $junk déchets, $use stat vanilla brute
  des lancers, dont $cast = $use / 2 : la stat compte le lancer ET la remontée, donc approximatif) et état.
- Boutons dans dialog/lobby_events.json (avant « trigger mg.menu ») et lignes de lobby/ev/menu_chat (après celles du foot).
  gen_events.py réécrit ces deux fichiers : le relancer impose de relancer gen_foot.py, gen_fish.py puis gen_sit.py.
"""
import common as C
import fish_rod as FR
from foot_admin import OPT_STATS as FOOT_STATS, TIP_STATS as FOOT_TIP, act, add_buttons, chat_line

OPT_TOGGLE, OPT_STATS = 86, 87
TIP_TOGGLE = 'Active ou coupe la pêche à l\'étang du spawn (active par défaut)'
TIP_STATS = 'Affiche les compteurs d\'usage de la pêche (cannes, prises, dorés, déchets, lancers)'
COUNTERS = [('$rod', '🎣 Cannes prises'), ('$catch', '⭐ Prises'), ('$gold', '✨ Dorés'), ('$junk', 'Déchets'), ('$cast', '🎣 Lancers ≈')]


def write(orig):
    """Écrit lobby/fish/admin_toggle et admin_stats ; orig = bloc d'origine du spawn à la place du socle (theme_world.W, sinon air)."""
    w, js = C.w, C.js
    w('lobby/fish/admin_toggle', ['# Admin (@s) : coupe / rétablit la pêche à l\'étang ($lfoff mg.st = 1 : coupée, absent : active)',
                                  'execute store success score #lfw mg.st if score $lfoff mg.st matches 1',
                                  'execute if score #lfw mg.st matches 1 run scoreboard players reset $lfoff mg.st',
                                  'execute if score #lfw mg.st matches 1 run function mg:lobby/fish/build',
                                  'execute if score #lfw mg.st matches 1 run return run tellraw @s ' + js({'text': '🎣 Pêche à l\'étang : activée (socle reposé).', 'color': 'green'}),
                                  'scoreboard players set $lfoff mg.st 1',
                                  'kill @e[tag=mg.lfs]', 'kill @e[type=minecraft:marker,tag=mg.lfm]', 'tag @a remove mg.lfc',
                                  f'setblock {FR.POS} {orig}',
                                  f'clear @a {FR.PRED}', FR.DROPPED, 'function mg:lobby/fish/purge',
                                  'tellraw @s ' + js({'text': '🎣 Pêche à l\'étang : désactivée (socle et cannes retirés).', 'color': 'red'})])
    w('lobby/fish/admin_stats', ['# Admin (@s) : compteurs d\'usage de la pêche (objectif mg.lfn), depuis sa création'] +
      [f'execute unless score {n} mg.lfn matches 0.. run scoreboard players set {n} mg.lfn 0' for n in ('$rod', '$catch', '$gold', '$junk', '$use')] +
      ['# la stat vanilla compte le lancer et la remontée : lancers ≈ $use / 2',
       'scoreboard players operation $cast mg.lfn = $use mg.lfn', 'scoreboard players set #lf2 mg.st 2',
       'scoreboard players operation $cast mg.lfn /= #lf2 mg.st',
       'execute if score $lfoff mg.st matches 1 run tellraw @s ' + js({'text': '🎣 Pêche à l\'étang : désactivée', 'color': 'red'}),
       'execute unless score $lfoff mg.st matches 1 run tellraw @s ' + js({'text': '🎣 Pêche à l\'étang : activée', 'color': 'green'}),
       'tellraw @s ' + js([{'text': 'Usage : ', 'color': 'gray'}] + sum([[
           {'text': ('' if i == 0 else ' · ') + lab + ' ', 'color': 'white'},
           {'score': {'name': n, 'objective': 'mg.lfn'}, 'color': 'yellow'}] for i, (n, lab) in enumerate(COUNTERS)], []))])


def wire():
    """Boutons du menu des événements (fenêtre et menu texte, après ceux du foot) et lignes de core/opt."""
    add_buttons('lobby_events.json', [act('🎣 Pêche on/off', 'green', OPT_TOGGLE, TIP_TOGGLE), act('🎣 Stats pêche', 'aqua', OPT_STATS, TIP_STATS)],
                before='trigger mg.menu')
    C.patch('lobby/ev/menu_chat', chat_line('⚽ Stats foot', 'aqua', FOOT_STATS, FOOT_TIP), [chat_line('🎣 Pêche on/off', 'green', OPT_TOGGLE, TIP_TOGGLE),
                                                                                           chat_line('🎣 Stats pêche', 'aqua', OPT_STATS, TIP_STATS)])
    reset = 'scoreboard players reset @s mg.opt'
    for line in [f'execute if score @s mg.opt matches {OPT_TOGGLE}..{OPT_STATS} unless entity @s[tag=mg.admin] run tellraw @s '
                 '{"text":"⚠ Réservé aux admins.","color":"red"}',
                 f'execute if score @s mg.opt matches {OPT_TOGGLE} if entity @s[tag=mg.admin] run function mg:lobby/fish/admin_toggle',
                 f'execute if score @s mg.opt matches {OPT_STATS} if entity @s[tag=mg.admin] run function mg:lobby/fish/admin_stats']:
        C.patch('core/opt', reset, [line], where='before')
