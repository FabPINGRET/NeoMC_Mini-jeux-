"""🎯 TDM sniper — Rouge contre Bleu au sniper (id 246), dans les arènes du duel (Canyon, Ville, Glacier).

    python tools/tdm/gen_tdm.py .        (depuis la racine du dépôt ; idempotent ; APRÈS gen_duel_maps.py et gen_duel.py
    (arènes, MAPS, fonction duel/pick) et après tout générateur qui réécrit core/request, core/begin, core/game_tick ou
    core/return_lobby ; avant tools/variantes/gen_variants.py)

Même sniper que le duel (rayon, tête = 2 dégâts, corps = 1, 2 PV, accroupi = lunette) mais le kit est marqué mg_tm : le duel
ne le touche pas. Le jeu est une partie du cœur (prepare / go / tick / cleanup, équipes mg_red / mg_blue de core/assign_teams).
L'arène est tirée au hasard parmi celles sans duel en cours et réservée par $tma (le duel ne la prend plus, build_all non plus).
Réapparition immédiate à un des 12 départs de son équipe, 3 s de protection. Pas de tir ami : le rayon traverse les coéquipiers.
25 frags pour gagner (ou le plus de frags au bout de 8 min). Seul : mode entraînement (pas de victoire).
Armes : le sniper (clic droit) et un couteau (clic gauche, advancement mg:tdm_melee, 1 dégât, recharge 1 s ; helpers de duel_play.py).
Des packs de soin (pomme dorée, ramassés à 1 PV) apparaissent de temps en temps sur des emplacements fixes (tdm_packs.py).
Le combat (tick, lunette, tir, rayon, couteau, frags) est dans tdm_play.py.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'arcade'))
sys.path.insert(0, os.path.join(HERE, '..', 'duel'))
sys.path.insert(0, HERE)
import common as C
import duel_play
import tdm_packs
import tdm_play
from duel_invite import tx, say
from gen_duel_maps import MAPS

w, js = C.w, C.js
GID = 246
WIN, LIMIT, PROT = 25, 9600, 60          # frags pour gagner, durée max (8 min, en ticks), protection de réapparition (3 s)
OBJ = [('mg.tmk', 'dummy ' + js({'text': '🎯 Frags', 'color': 'gold'})), ('mg.tmhp', 'dummy'), ('mg.tmcd', 'dummy'), ('mg.tmx', 'dummy'),
       ('mg.tmkc', 'dummy')]
TAGS = ['mg.tmsh', 'mg.tmen', 'mg.tmvc', 'mg.tmp', 'mg.tmsc']
SLOTS = [(dx, k) for k in range(2) for dx in (-5, -3, -1, 1, 3, 5)]      # 12 départs par équipe : x (de 0,5) et rang de départ (zl 66 / 68)
RGB = {'red': 16711680, 'blue': 255}


def prepare():
    w('tdm/prepare', [
        '# 🎯 TDM sniper — préparation : arène du duel libre au hasard, réservée par $tma',
        'scoreboard players set $tma mg.st 0',
        'execute unless data storage mg:duel {built:1b} run return run function mg:tdm/no_map',
        'function mg:duel/pick',
        'execute if score $dli mg.st matches 0 run return run function mg:tdm/no_map',
        'scoreboard players operation $tma mg.st = $dli mg.st',
        '# point de reconnexion (spectateur) : au-dessus du centre de l\'arène',
        'scoreboard players set $px mg.st 0',
    ] + [f'execute if score $tma mg.st matches {i} run scoreboard players set $py mg.st {m["y"] + 20}' for i, m in enumerate(MAPS, 1)]
      + [f'execute if score $tma mg.st matches {i} run scoreboard players set $pz mg.st {m["z"]}' for i, m in enumerate(MAPS, 1)] + [
        'clear @a[tag=mg.play]',
        'gamemode adventure @a[tag=mg.play]',
        'tag @a remove mg.tmp',
        'scoreboard players set $nt mg.st 2',
        'function mg:core/assign_teams',
        'scoreboard players reset * mg.tmk',
        '# premiers départs : un par rang dans l\'équipe (pas de tirage : deux coéquipiers ne partagent pas un départ)',
        'scoreboard players set $tmri mg.st 0',
        'scoreboard players set $tmbi mg.st 0',
        f'scoreboard players set #tm12 mg.st {len(SLOTS)}',
        'execute as @a[tag=mg.play] run function mg:tdm/spawn_first',
    ] + [f'execute if score $tma mg.st matches {i} run ' + say('@a[tag=mg.play]', tx('🎯 Carte : ', 'gray'), tx(m['name'], 'gold', bold=True))
         for i, m in enumerate(MAPS, 1)])
    w('tdm/no_map', [
        '# Annulation pendant la préparation (aucune arène utilisable) : pas de gel ni de partie (core/request s\'arrête à $state 3)',
        'execute unless data storage mg:duel {built:1b} run ' + say(
            '@a[tag=mg.play]', tx('🎯 TDM sniper : les arènes du duel ne sont pas encore construites (réessaie dans quelques minutes). Partie annulée.', 'red')),
        'execute if data storage mg:duel {built:1b} run ' + say(
            '@a[tag=mg.play]', tx('🎯 TDM sniper : toutes les arènes du duel sont occupées par un duel. Partie annulée.', 'red')),
        'scoreboard players set $tma mg.st 0',
        '# pas de note : rate/begin (qui pose $rgf) n\'a pas tourné, rate/collect noterait sinon la partie précédente',
        'scoreboard players set $rgf mg.st 0',
        'function mg:core/abort',
    ])


def spawn():
    w('tdm/spawn', ['# (Ré)apparition de @s (participant, $tma = arène) à un départ de son équipe tiré au hasard',
                    f'execute store result score #tms mg.st run random value 0..{len(SLOTS) - 1}',
                    'function mg:tdm/spawn_do'])
    w('tdm/spawn_first', [
        '# Premier départ de @s (prepare) : rang d\'arrivée dans son équipe (modulo le nombre de départs)',
        'execute if entity @s[team=mg_red] run scoreboard players operation #tms mg.st = $tmri mg.st',
        'execute if entity @s[team=mg_red] run scoreboard players add $tmri mg.st 1',
        'execute if entity @s[team=mg_blue] run scoreboard players operation #tms mg.st = $tmbi mg.st',
        'execute if entity @s[team=mg_blue] run scoreboard players add $tmbi mg.st 1',
        'scoreboard players operation #tms mg.st %= #tm12 mg.st',
        'function mg:tdm/spawn_do'])
    sp = ['# Apparition de @s (participant, $tma = arène, #tms = départ) : PV neufs, 3 s de protection (mg.tmp), tir impossible',
          'scoreboard players set @s mg.tmhp 2',
          'function mg:tdm/unscope',
          'tag @s add mg.tmp',
          f'scoreboard players set @s mg.tmx {PROT}',
          'scoreboard players set @s mg.tmcd 0',
          'scoreboard players set @s mg.tmkc 0',
          'title @s actionbar ' + js(tx('3', 'yellow', bold=True))]
    for i, m in enumerate(MAPS, 1):
        sp.append(f'execute if score $tma mg.st matches {i} positioned 0.5 {m["y"]} {m["z"]}.5 run function mg:tdm/spawn_slot')
    w('tdm/spawn_do', sp)
    # rouge au nord (regard vers le sud, 0), bleu au sud (regard 180) ; la position exécutée est le centre de l'arène, à la hauteur du sol
    sl = ['# (@s, position = centre de l\'arène à la hauteur du sol, #tms = départ 0..11) : tp au départ de l\'équipe',
          'execute if entity @s[team=mg_red] run spawnpoint @s ~ ~ ~-66',
          'execute if entity @s[team=mg_blue] run spawnpoint @s ~ ~ ~66']
    for t, sgn, yaw in (('red', -1, 0), ('blue', 1, 180)):
        for k, (dx, row) in enumerate(SLOTS):
            sl.append(f'execute if entity @s[team=mg_{t}] if score #tms mg.st matches {k} run tp @s ~{dx} ~ ~{sgn * (66 + 2 * row)} {yaw} 0')
    w('tdm/spawn_slot', sl)
    w('tdm/respawn', ['# @s : mort hors tir ou sorti de l\'arène : réapparition sans frag',
                      'scoreboard players set @s mg.deaths 0',
                      'function mg:tdm/spawn',
                      '# la mort vanilla a retiré résistance, saturation et l\'attribut de chute',
                      'function mg:tdm/buffs',
                      'function mg:core/heal'])
    w('tdm/buffs', [
        '# (@s = participant ; tdm/go et tdm/respawn) : pas de mort hors tir (coups de poing, couteau), pas de dégâts de chute',
        'effect give @s minecraft:resistance infinite 4 true',
        'effect give @s minecraft:saturation infinite 0 true',
        'attribute @s minecraft:fall_damage_multiplier base set 0'])


def kit():
    sniper = ('minecraft:warped_fungus_on_a_stick[custom_data={mg_tm:1b},item_model="minecraft:spyglass",unbreakable={},custom_name='
              + js(tx('🎯 Sniper TDM', 'aqua', bold=True, italic=False)) + ',lore=['
              + js(tx('Clic droit : tir (recharge 2 s)', 'gray', italic=False)) + ','
              + js(tx('Accroupi : lunette — tête = élimination, corps = 2 touches', 'gray', italic=False)) + ']]')
    lines = ['# Kit TDM (@s) : le sniper en main, le couteau (clic gauche) dans l\'inventaire, cuir aux couleurs de l\'équipe',
             'clear @s *[custom_data~{mg_tm:1b}]',
             f'item replace entity @s weapon.mainhand with {sniper}',
             'give @s ' + duel_play.knife('mg_tm')]
    for t, rgb in RGB.items():
        for slot, piece in (('chest', 'chestplate'), ('head', 'helmet'), ('legs', 'leggings'), ('feet', 'boots')):
            lines.append(f'execute if entity @s[team=mg_{t}] run item replace entity @s armor.{slot} with minecraft:leather_{piece}[dyed_color={rgb},unbreakable={{}}]')
    w('tdm/kit', lines)


def play():
    intro = js([tx('🎯 TDM SNIPER : ', 'gold', bold=True),
                tx('tête = élimination, corps = 2 touches, accroupi = lunette. Tu réapparais tout de suite (3 s de protection). '
                   f'{WIN} frags pour gagner l\'équipe, {LIMIT // 1200} min max. Pas de tir ami.')])
    w('tdm/go', [
        '# Départ',
        'scoreboard players set $tmt mg.st 0',
        '# premier pack de soin 20 s après le GO',
        'scoreboard players set $tmhc mg.st 400',
        '# la protection posée par spawn pendant le prepare ne court qu\'à partir d\'ici : on tire dès le GO',
        'tag @a remove mg.tmp',
        'scoreboard players reset @a mg.tmx',
        'title @a[tag=mg.play] actionbar ""',
        'execute as @a[tag=mg.play] run function mg:tdm/kit',
        '# core/begin vient de retirer la résistance du compte à rebours : pas de mort hors tir (coups de poing), pas de dégâts de chute',
        'execute as @a[tag=mg.play] run function mg:tdm/buffs',
        'scoreboard players set @a mg.deaths 0',
        'scoreboard players set Rouge mg.tmk 0',
        'scoreboard players set Bleu mg.tmk 0',
        'scoreboard objectives setdisplay sidebar mg.tmk',
        'tellraw @a[tag=mg.play] ' + intro,
        'execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] ' + js(
            tx('🎯 Mode entraînement (seul) : pas d\'adversaire ni de victoire ; il faut au moins 2 joueurs pour une vraie partie.', 'yellow')),
    ])
    w('tdm/timeout', [
        f'# {LIMIT // 1200} min : le plus de frags gagne',
        'execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] ' + js(tx('🎯 Fin de l\'entraînement.', 'yellow')),
        'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
        'execute if score Rouge mg.tmk > Bleu mg.tmk run return run function mg:core/win_red',
        'execute if score Bleu mg.tmk > Rouge mg.tmk run return run function mg:core/win_blue',
        'function mg:core/draw',
    ])
    w('tdm/cleanup', [
        '# Fin de partie (appelée aussi après une annulation pendant la préparation : sans effet sur ce qui n\'existe pas)',
        'scoreboard players set $tma mg.st 0',
        'kill @e[type=minecraft:marker,tag=mg.tmend]',
        'kill @e[type=minecraft:item_display,tag=mg.tmhk]',
        tdm_play.item_kill([m['z'] for m in MAPS]),
        'title @a[tag=mg.play] clear',
    ] + [f'tag @a remove {t}' for t in TAGS] + ['scoreboard players reset * mg.tmk'])


def main(root):
    C.init(root)
    prepare()
    spawn()
    kit()
    play()
    tdm_play.build(w, js, [m['z'] for m in MAPS], WIN, LIMIT)
    tdm_packs.check_spots(MAPS, [(dx, sgn * (66 + 2 * row)) for sgn in (-1, 1) for dx, row in SLOTS])
    tdm_packs.build(w, js, MAPS)
    duel_play.write_adv(C.D, 'tdm_melee', 'mg:tdm/melee_adv')
    C.register([GID], 'tdm', [C.announce(GID, '', '🎯 TDM SNIPER', 'gold', f'rouges contre bleus au sniper, {WIN} frags pour gagner !')])
    C.objectives(OBJ)
    C.patch('desinstaller', 'function mg:duel/remove', ['kill @e[type=minecraft:item_display,tag=mg.tmhk]'])
    # deux appels d'une ligne : patch() n'est pas idempotent si une partie seulement des lignes existe déjà
    C.patch('desinstaller', 'kill @e[type=minecraft:item_display,tag=mg.tmhk]', ['function mg:tdm/cleanup'])
    print('TDM OK')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
