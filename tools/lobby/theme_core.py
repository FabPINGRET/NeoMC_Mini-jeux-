"""Fonctions communes des décors saisonniers (importé par gen_themes.py, jamais lancé seul) : off, sync, restore, reskin, tick, branchements.

Chacune appelle les fonctions du thème actif ($theme) d'après THEMES = [(id, clé, libellé, mg.opt, fabrique), ...].
"""
import common as C
import theme_fall as TF
from theme_world import LOBBY

w = C.w


def write_dispatch(THEMES):
    w('lobby/theme/off', ['# Retire le décor saisonnier en place ($theme) et rétablit le spawn d\'origine', 'function mg:lobby/theme/sync',
                          'execute unless score $theme mg.st matches 1.. run return run tellraw @s {"text":"Aucun décor saisonnier en place.","color":"gray"}'] +
      [f'execute if score $theme mg.st matches {tid} run function mg:lobby/theme/{key}/off' for tid, key, *_ in THEMES] +
      ['scoreboard players set $theme mg.st 0', 'data remove storage mg:lobby theme', *TF.off_lines(), 'function mg:lobby/theme/clear',
       '# $thsw (bascule d\'un thème à l\'autre) : le place du nouveau thème remet l\'eau d\'aplomb, une seule fois pour les deux',
       'execute unless score $thsw mg.st matches 1 run function mg:lobby/theme/water_fix',
       'function mg:lobby/deco', 'function mg:lobby/food_skin',
       '# allée des champions (hors décor généré) : reconstruite telle quelle', 'function mg:hall/build',
       'execute unless score $thsw mg.st matches 1 run tellraw @a[tag=mg.admin] {"text":"Décor saisonnier retiré, spawn d\'origine rétabli.","color":"gray"}'])
    # $theme perdu (scoreboard réinitialisé) alors que la copie mg:lobby theme reste : le score en est rétabli
    w('lobby/theme/sync', ['# $theme remis d\'après sa copie mg:lobby theme s\'il manque ou vaut 0 (appelé par on, off, toggle, restore)',
                           'execute unless score $theme mg.st matches 1.. store result score $theme mg.st run data get storage mg:lobby theme'])
    # Redémarrage / rechargement : le décor actif (score $theme, sinon sa copie mg:lobby theme) est reposé quand un joueur
    # est au spawn depuis 5 s (chunks chargés) : blocs manquants, entités, eau ; rien n'est doublé
    w('lobby/theme/restore', ['# Décor saisonnier reposé après un redémarrage (appelé par core/tick tant que $thrs >= 1)',
                              'scoreboard players add $thrs mg.st 1',
                              'execute if score $thrs mg.st matches ..100 run return 0',
                              'scoreboard players set $thrs mg.st 0',
                              'function mg:lobby/theme/sync'] +
      [f'execute if score $theme mg.st matches {tid} run function mg:lobby/theme/{key}/place' for tid, key, *_ in THEMES] +
      ['execute if score $theme mg.st matches 1.. store result storage mg:lobby theme int 1 run scoreboard players get $theme mg.st'])
    w('lobby/theme/reskin', ['# Appelé à la fin de lobby/deco : rhabille les entités du décor selon le thème actif'] +
      [f'execute if score $theme mg.st matches {tid} run function mg:lobby/theme/{key}/reskin' for tid, key, *_ in THEMES] + ['function mg:lobby/food_skin'])
    w('lobby/theme/tick', ['# Habillage des animaux tourné comme eux (chaque tick), puis cycle des chutes et ambiance du thème (chaque seconde)',
                           'execute as @e[type=minecraft:item_display,tag=mg.thrid] on vehicle rotated as @s on passengers '
                           'if entity @s[tag=mg.thrid] run rotate @s ~ 0',
                           'scoreboard players add $tht mg.st 1', 'execute if score $tht mg.st matches ..19 run return 0',
                           'scoreboard players set $tht mg.st 0', 'function mg:lobby/theme/fall_tick'] +
      [f'execute if score $theme mg.st matches {tid} run function mg:lobby/theme/{key}/fx' for tid, key, *_ in THEMES])


def write_wiring(THEMES):
    """Branche les thèmes dans les fonctions du pack (tick, chargement, deco, menu admin, désinstallation)."""
    C.patch('core/tick', 'execute if score $setup mg.st matches 1 run function mg:lobby/ev/tick',
            ['execute if score $theme mg.st matches 1.. run function mg:lobby/theme/tick'])
    C.patch('core/tick', 'execute if score $theme mg.st matches 1.. run function mg:lobby/theme/tick',
            [f'execute if score $thrs mg.st matches 1.. if entity {LOBBY} run function mg:lobby/theme/restore'])
    # sans thème, les animaux restants (sortis de la zone, ancien monde) sont retirés, toutes les 2 s ($lan : 40 ticks) ;
    # pas si le score est perdu mais la copie storage reste (lobby/theme/sync le rétablit au prochain restore)
    C.patch('core/tick', f'execute if score $thrs mg.st matches 1.. if entity {LOBBY} run function mg:lobby/theme/restore',
            ['execute if score $lan mg.t matches 30 unless score $theme mg.st matches 1.. unless data storage mg:lobby theme '
             'as @e[tag=mg.thmob] run function mg:lobby/theme/gone'])
    C.patch('core/load', 'scoreboard objectives add mg.st dummy', ['scoreboard players set $thrs mg.st 1'])
    C.patch('core/load', 'scoreboard objectives add mg.st dummy', ['scoreboard players set $thsw mg.st 0'])   # drapeau de bascule jamais resté à 1
    # reconstruction du spawn : le décor est reposé par restore (comme après un redémarrage)
    C.patch('lobby/build_end', 'data modify storage mg:lobby v6 set value 1b',
            ['execute if score $theme mg.st matches 1.. run scoreboard players set $thrs mg.st 1'])
    C.patch('lobby/deco', 'data modify storage mg:lobby deco3 set value 1b',
            ['execute if score $theme mg.st matches 1.. run function mg:lobby/theme/reskin'])
    C.patch('core/opt', 'execute if score @s mg.opt matches 62..65 run function mg:tpg/run',
            [f'execute if score @s mg.opt matches {THEMES[0][3]}..{THEMES[-1][3]} unless entity @s[tag=mg.admin] run tellraw @s {{"text":"⚠ Réservé aux admins.","color":"red"}}'] +
            [f'execute if score @s mg.opt matches {opt} if entity @s[tag=mg.admin] run function mg:lobby/theme/{key}/toggle' for _, key, _, opt, _ in THEMES])
    C.patch('desinstaller', '# Désinstallation (OP) — retire scoreboards, équipes, décor et zones chargées',
            ['execute if score $theme mg.st matches 1.. run function mg:lobby/theme/off'])
    C.patch('desinstaller', 'execute if score $theme mg.st matches 1.. run function mg:lobby/theme/off',
            ['data remove storage mg:lobby theme'])           # même si $theme est perdu : plus de copie qui repose un décor
    C.patch('desinstaller', 'execute if score $theme mg.st matches 1.. run function mg:lobby/theme/off',
            ['function mg:lobby/theme/sync'], where='before')   # $theme perdu mais copie storage là : off doit quand même tourner
