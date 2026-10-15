"""Fonctions communes des décors saisonniers (importé par gen_themes.py, jamais lancé seul) : off, sync, restore, reskin, tick.

Chacune appelle les fonctions du thème actif ($theme) d'après THEMES = [(id, clé, libellé, mg.opt, fabrique), ...].
"""
import common as C

w = C.w


def write_dispatch(THEMES):
    w('lobby/theme/off', ['# Retire le décor saisonnier en place ($theme) et rétablit le spawn d\'origine', 'function mg:lobby/theme/sync',
                          'execute unless score $theme mg.st matches 1.. run return run tellraw @s {"text":"Aucun décor saisonnier en place.","color":"gray"}'] +
      [f'execute if score $theme mg.st matches {tid} run function mg:lobby/theme/{key}/off' for tid, key, *_ in THEMES] +
      ['scoreboard players set $theme mg.st 0', 'data remove storage mg:lobby theme', 'function mg:lobby/theme/clear', 'function mg:lobby/theme/water_fix',
       'function mg:lobby/deco', 'function mg:lobby/food_skin',
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
    w('lobby/theme/tick', ['# Habillage des animaux tourné comme eux (chaque tick), puis ambiance du thème (chaque seconde)',
                           'execute as @e[type=minecraft:item_display,tag=mg.thrid] on vehicle rotated as @s on passengers '
                           'if entity @s[tag=mg.thrid] run rotate @s ~ 0',
                           'scoreboard players add $tht mg.st 1', 'execute if score $tht mg.st matches ..19 run return 0',
                           'scoreboard players set $tht mg.st 0'] +
      [f'execute if score $theme mg.st matches {tid} run function mg:lobby/theme/{key}/fx' for tid, key, *_ in THEMES])
