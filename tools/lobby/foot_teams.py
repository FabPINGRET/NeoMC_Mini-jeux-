"""⚽ Terrain de foot : équipes et socles du vestiaire (importé par gen_foot.py, jamais lancé seul).

Équipes propres au foot (mg_ftr rouge, mg_ftb bleu : créées par core/load, JAMAIS mg_red / mg_blue des jeux). Tags mg.ftr / mg.ftb.
- Socle rouge / bleu : tag, équipe, actionbar (foot/tick n'appelle pas la fonction à qui l'a déjà : tag=!mg.ftr). Compteur $eq (mg.ftn).
- Socle blanc : quitte l'équipe. Socle or : quitte l'équipe et remonte à la surface, devant le portail du foot du hub (FB.RETURN).
- foot/cleanup (@s) : retire les tags d'équipe et quitte l'équipe SI c'est mg_ftr / mg_ftb (jamais l'équipe d'un jeu). Appelé par les socles,
  foot/away, core/reset_player, core/request (lancement d'une partie) et la désactivation par un admin.
- foot/away (@s) : sorti de la zone (ou de l'overworld) : plus compté (mg.ftin), plus d'équipe, score de buts libres (mg.ft) effacé.
- foot/enter (@s) : première entrée dans la zone depuis la dernière sortie (tag mg.ftin) : compteur $ent, score de buts libres à 0, message d'accueil.
Le score de buts libres de chacun est son propre mg.ft (jamais $ftg) ; tag mg.ftlt = dernier toucheur de la balle (foot_game.py).
"""
import common as C
import foot_build as FB


def write():
    w, js = C.w, C.js
    for key, tag, other, team, txt, col in (('red', 'mg.ftr', 'mg.ftb', 'mg_ftr', '🔴 Équipe rouge', 'red'),
                                            ('blue', 'mg.ftb', 'mg.ftr', 'mg_ftb', '🔵 Équipe bleue', 'blue')):
        w(f'foot/pad_{key}', [f'# @s marche sur le socle {key} : équipe {txt[2:]} (foot/tick ne l\'appelle pas à qui a déjà {tag})',
                              f'tag @s add {tag}', f'tag @s remove {other}', f'team join {team} @s', 'scoreboard players add $eq mg.ftn 1',
                              'title @s actionbar ' + js({'text': txt, 'color': col, 'bold': True}),
                              'execute at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.2'])
    w('foot/pad_white', ['# @s (en équipe) marche sur le socle blanc : quitte son équipe', 'function mg:foot/cleanup',
                         'title @s actionbar ' + js({'text': '✖ Tu as quitté ton équipe', 'color': 'gray'}),
                         'execute at @s run playsound minecraft:block.note_block.bass master @s ~ ~ ~ 1 0.8'])
    w('foot/leave', ['# @s marche sur le socle or : quitte son équipe, perd ses buts libres et remonte à la surface (devant le portail du foot du hub)',
                     'function mg:foot/cleanup', 'tag @s remove mg.ftin',
                     'scoreboard players reset @s mg.ft', 'tag @s remove mg.ftlt',
                     f'tp @s {FB.RETURN[0]} {FB.RETURN[1]} {FB.RETURN[2]} facing 0.5 64 0.5',
                     'title @s actionbar ' + js({'text': '🏠 Remonter au spawn', 'color': 'yellow'})])
    w('foot/cleanup', ['# @s quitte les équipes du foot (tags ; équipe quittée seulement si c\'est mg_ftr / mg_ftb : jamais celle d\'un jeu)',
                       'tag @s remove mg.ftr', 'tag @s remove mg.ftb',
                       'execute if entity @s[team=mg_ftr] run team leave @s', 'execute if entity @s[team=mg_ftb] run team leave @s'])
    w('foot/away', ['# @s (mg.ftr, mg.ftb ou mg.ftin) : toujours sur le terrain ? Oui (et en overworld) : rien ; non : plus compté, plus d\'équipe',
                    f'execute if entity @s[{FB.FOOT_ZONE}] at @s if dimension minecraft:overworld run return 0',
                    'tag @s remove mg.ftin', 'function mg:foot/cleanup',
                    'scoreboard players reset @s mg.ft', 'tag @s remove mg.ftlt'])
    w('foot/enter', ['# @s entre sur le terrain / au vestiaire (tag mg.ftin jusqu\'à sa sortie : foot/away) : ses buts libres repartent de 0',
                     'tag @s add mg.ftin', 'scoreboard players add $ent mg.ftn 1', 'scoreboard players set @s mg.ft 0',
                     'title @s actionbar ' + js([{'text': '⚽ Terrain de foot : ', 'color': 'green', 'bold': True},
                                                 {'text': 'marche sur un socle pour choisir ton équipe, ou joue libre.', 'color': 'gray'}])])
