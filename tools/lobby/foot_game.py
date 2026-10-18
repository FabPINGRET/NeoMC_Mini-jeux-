"""⚽ Terrain de foot : jeu (importé par gen_foot.py, jamais lancé seul) - balle, buts, score, boucles foot/tick et foot/second.

- foot/tick (chaque tick, tant qu'un joueur est dans FOOT_ZONE) : entrée (compteur), socles du vestiaire, buts.
- foot/second (toutes les 2 s, core/tick sur $lan mg.t = 30, gardé par `if loaded`) : entretien de la balle (une seule, tagguée mg.ball ;
  sulfur_cube « sans tag » tué dans la zone ; hors terrain ou 20 s sans joueur à moins de 6 blocs : retour au centre), départ des joueurs
  d'équipe sortis, résistance (pas de PvP), score en actionbar, remise à zéro du score après 30 s sans joueur sur le terrain.
- Règle du vrai foot : un but compte pour l'équipe ADVERSE du but, quel que soit le tireur. But dans le but ouest (rouge) : +1 Bleus ;
  dans le but est (bleu) : +1 Rouges. Personne en équipe sur le terrain : compteur de buts libres.
Scores : objectif mg.ft ($ftr Rouges, $ftb Bleus, $ftg buts libres, $fte passes de 2 s sans joueur, $fti passes de 2 s sans joueur près de la balle,
$ftk nombre de balles). Compteurs d'usage : $but dans mg.ftn (foot_admin.py).
"""
import common as C
import foot_build as FB

Z = FB.FOOT_ZONE
SCORE_TXT = lambda: [{'text': '🔴 ', 'color': 'red'}, {'score': {'name': '$ftr', 'objective': 'mg.ft'}, 'color': 'red', 'bold': True},      # noqa: E731
                     {'text': ' – ', 'color': 'gray'}, {'score': {'name': '$ftb', 'objective': 'mg.ft'}, 'color': 'blue', 'bold': True},
                     {'text': ' 🔵', 'color': 'blue'}]


def write():
    w, js = C.w, C.js
    w('foot/tick', ['# ⚽ Terrain de foot : chaque tick tant qu\'un joueur est sur le terrain, au vestiaire ou dans le puits (core/tick)',
                    f'execute as @a[{Z},tag=!mg.ftin,gamemode=!spectator] run function mg:foot/enter',
                    '# socles du vestiaire : rouge et bleu = équipe (une fois), blanc = quitter, or = retour au spawn (pas les spectateurs)',
                    f'execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.ftr,gamemode=!spectator,{FB.pad_box("red")}] run function mg:foot/pad_red',
                    f'execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.ftb,gamemode=!spectator,{FB.pad_box("blue")}] run function mg:foot/pad_blue',
                    f'execute as @a[tag=!mg.play,tag=!mg.out,tag=mg.ftr,gamemode=!spectator,{FB.pad_box("white")}] run function mg:foot/pad_white',
                    f'execute as @a[tag=!mg.play,tag=!mg.out,tag=mg.ftb,gamemode=!spectator,{FB.pad_box("white")}] run function mg:foot/pad_white',
                    f'execute as @a[tag=!mg.play,tag=!mg.out,gamemode=!spectator,{FB.pad_box("gold")}] run function mg:foot/leave',
                    '# buts : la balle, même en partie, dans un renfoncement',
                    f'execute if entity @e[type=minecraft:sulfur_cube,tag=mg.ball,{FB.GOAL_W}] run function mg:foot/goal_w',
                    f'execute if entity @e[type=minecraft:sulfur_cube,tag=mg.ball,{FB.GOAL_E}] run function mg:foot/goal_e'])
    w('foot/second', [
        '# ⚽ Terrain de foot : entretien toutes les 2 s (core/tick : $lan mg.t = 30, chunks chargés)',
        '# terrain coupé par un admin : plus de balle',
        f'execute if score $ftoff mg.st matches 1 run kill {FB.BALLS}',
        'execute if score $ftoff mg.st matches 1 run return 0',
        '# joueurs d\'équipe (ou comptés à l\'entrée) qui ne sont plus sur le terrain',
        'execute as @a[tag=mg.ftr] run function mg:foot/away', 'execute as @a[tag=mg.ftb] run function mg:foot/away',
        'execute as @a[tag=mg.ftin] run function mg:foot/away',
        '# balle : une seule, tagguée (les autres sulfur_cube de la zone disparaissent ; deux balles : on repart de zéro)',
        f'kill @e[type=minecraft:sulfur_cube,tag=!mg.ball,{Z}]',
        f'execute store result score $ftk mg.ft if entity {FB.BALLS}',
        f'execute if score $ftk mg.ft matches 2.. run kill {FB.BALLS}',
        'execute unless score $ftk mg.ft matches 1 run function mg:foot/ball_new',
        f'execute as {FB.BALL1} unless entity @s[{FB.BALL_BOX}] run function mg:foot/ball_home',
        'function mg:foot/ball_idle',
        '# sur le terrain : pas de PvP (la chute ne fait déjà rien au lobby : core/attr_reset), score, remise à zéro du score quand il est vide',
        f'effect give @a[{Z}] minecraft:resistance 3 4 true',
        f'title @a[{Z}] actionbar ' + js([{'text': '⚽ ', 'color': 'white'}] + SCORE_TXT() + [
            {'text': ' · buts libres ', 'color': 'gray'}, {'score': {'name': '$ftg', 'objective': 'mg.ft'}, 'color': 'yellow'}]),
        f'execute if entity @a[{Z}] run scoreboard players set $fte mg.ft 0',
        f'execute unless entity @a[{Z}] run scoreboard players add $fte mg.ft 1',
        'execute if score $fte mg.ft matches 15.. run function mg:foot/score_reset'])
    w('foot/score_reset', ['# 30 s sans joueur sur le terrain : nouveau match', 'scoreboard players set $ftr mg.ft 0', 'scoreboard players set $ftb mg.ft 0',
                           'scoreboard players set $ftg mg.ft 0', 'scoreboard players set $fte mg.ft 0'])
    # ---------------------------------------------------------------- balle
    w('foot/ball_new', ['# Balle (sulfur_cube, bloc d\'oak_planks en corps) au centre ; jamais mg.lby / mg.mob / mg.npc : les nettoyages du lobby la tueraient',
                        f'summon minecraft:sulfur_cube {FB.CENTRE} {{Tags:["mg.ball"],equipment:{{body:{{id:"minecraft:oak_planks",count:1}}}},'
                        'Invulnerable:1b,PersistenceRequired:1b}',
                        'scoreboard players set $fti mg.ft 0'])
    w('foot/ball_home', ['# La balle revient au centre, immobile (appelé par un but, par la sortie du terrain, par l\'inactivité)',
                         f'execute as {FB.BALLS} run tp @s {FB.CENTRE}',
                         f'data modify entity {FB.BALL1} Motion set value [0.0d,0.0d,0.0d]',
                         'scoreboard players set $fti mg.ft 0'])
    w('foot/ball_idle', ['# 20 s (10 passes) sans joueur à moins de 6 blocs de la balle : retour au centre',
                         'scoreboard players add $fti mg.ft 1',
                         f'execute at {FB.BALL1} if entity @a[distance=..6] run scoreboard players set $fti mg.ft 0',
                         'execute if score $fti mg.ft matches 10.. run function mg:foot/ball_home'])
    # ---------------------------------------------------------------- buts
    # (but dans le but ROUGE = ouest : +1 aux Bleus ; but dans le but BLEU = est : +1 aux Rouges)
    for side, goal, (gx, scorer, scorer_name), goal_name in (('w', 'ouest', (-14.5, '$ftb', 'Bleus'), 'ROUGE'), ('e', 'est', (19.5, '$ftr', 'Rouges'), 'BLEU')):
        w(f'foot/goal_{side}', [f'# But dans le but {goal_name} ({goal}) : le point va aux {scorer_name}, quel que soit le tireur (vraie règle du foot)',
                                f'particle minecraft:firework {gx} 49.5 -31 0.4 0.8 1.6 0.1 40 force',
                                'function mg:foot/ball_home', 'scoreboard players add $but mg.ftn 1',
                                f'execute unless entity @a[{FB.BALL_BOX},tag=mg.ftr] unless entity @a[{FB.BALL_BOX},tag=mg.ftb] run return run function mg:foot/goal_free',
                                f'scoreboard players add {scorer} mg.ft 1', 'function mg:foot/goal_show'])
    w('foot/goal_show', ['# Titre, score et son pour tous sur le terrain (le score est déjà à jour)',
                         f'title @a[{Z}] subtitle ' + js([{'text': 'Rouges ', 'color': 'red'}] + SCORE_TXT()[1:4] + [{'text': ' Bleus', 'color': 'blue'}]),
                         f'title @a[{Z}] title ' + js({'text': '⚽ BUT !', 'color': 'gold', 'bold': True}),
                         'function mg:foot/goal_fx'])
    w('foot/goal_free', ['# But sans équipe sur le terrain : compteur de buts libres',
                         'scoreboard players add $ftg mg.ft 1',
                         f'title @a[{Z}] subtitle ' + js([{'text': 'buts libres : ', 'color': 'gray'},
                                                          {'score': {'name': '$ftg', 'objective': 'mg.ft'}, 'color': 'yellow'}]),
                         f'title @a[{Z}] title ' + js({'text': '⚽ But !', 'color': 'gold', 'bold': True}),
                         'function mg:foot/goal_fx'])
    w('foot/goal_fx', [f'execute as @a[{Z}] at @s run playsound minecraft:entity.firework_rocket.twinkle master @s ~ ~ ~ 1 1'])
