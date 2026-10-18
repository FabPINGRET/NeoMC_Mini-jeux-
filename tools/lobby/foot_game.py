"""⚽ Terrain de foot : jeu (importé par gen_foot.py, jamais lancé seul) - balle, buts, score, boucles foot/tick et foot/second.

- foot/tick (chaque tick, tant qu'un joueur est dans FOOT_ZONE) : entrée (compteur), socles du vestiaire, dernier toucheur de la balle, buts.
- foot/second (toutes les 2 s, core/tick sur $lan mg.t = 30, gardé par `if loaded`) : entretien de la balle (une seule, tagguée mg.ball, corps
  test_block ; une balle d'une autre forme ou un sulfur_cube « sans tag » est tué ; hors terrain ou 20 s sans joueur à moins de 6 blocs :
  retour au centre), départ des joueurs d'équipe sortis, résistance (pas de PvP), score en actionbar, remise à zéro du score après 30 s sans joueur.
- Règle du vrai foot : un but compte pour l'équipe ADVERSE du but, quel que soit le tireur. But dans le but ouest (rouge) : +1 Bleus ;
  dans le but est (bleu) : +1 Rouges. Personne en équipe sur le terrain : buts libres, comptés PAR JOUEUR (mg.ft de chacun) au dernier
  toucheur (tag mg.ftlt, posé par foot/touch sur le plus proche de la balle) ; chacun ne voit que son propre score (score « * »).
- Balle : sulfur_cube au corps test_block (dessiné en ballon par le resource pack), archétype mg:football (write_archetype : frottement et
  résistance de l'air réduits, rebond). L'archétype n'est lu qu'au démarrage du serveur.
Scores : objectif mg.ft ($ftr Rouges, $ftb Bleus, $ftg total des buts libres (stats admin seulement), $fte passes de 2 s sans joueur, $fti passes
de 2 s sans joueur près de la balle, $ftk nombre de balles ; chaque joueur sur le terrain : ses buts libres). Compteurs d'usage : $but dans mg.ftn
(foot_admin.py).
"""
import os

import common as C
import foot_build as FB

Z = FB.FOOT_ZONE
BALL_ITEM = 'minecraft:test_block'       # corps de la balle : bloc de test, dessiné en ballon par le resource pack (foot_rp.py)
# archétype mg:football (data/mg/sulfur_cube_archetype/football.json), format de bouncy.json vanilla : identifiants et valeurs
ARCH_ID = 'mg:football'
BOUNCINESS = 0.6                         # rebond (add_value ; bouncy vanilla : 0,9)
FRICTION = -0.95                         # frottement réduit de 95 % : la balle roule loin (add_multiplied_total)
AIR_DRAG = -0.99                         # résistance de l'air réduite de 99 % (add_multiplied_total)
KNOCKBACK_RESIST = -2                    # annule la résistance au recul du cube, ordinaire et d'explosion (add_value)
HIT_POWER = {'horizontal_power': 0.6625, 'vertical_power': 0.105}   # recul quand on frappe la balle (bouncy vanilla : 0,4125 horizontal)
SOUND = 'entity.sulfur_cube.bouncy'      # sons du bouncy vanilla
SCORE_TXT = lambda: [{'text': '🔴 ', 'color': 'red'}, {'score': {'name': '$ftr', 'objective': 'mg.ft'}, 'color': 'red', 'bold': True},      # noqa: E731
                     {'text': ' – ', 'color': 'gray'}, {'score': {'name': '$ftb', 'objective': 'mg.ft'}, 'color': 'blue', 'bold': True},
                     {'text': ' 🔵', 'color': 'blue'}]


def write():
    w, js = C.w, C.js
    w('foot/tick', ['# ⚽ Terrain de foot : chaque tick tant qu\'un joueur est sur le terrain, ou au vestiaire (core/tick)',
                    f'execute as @a[{Z},tag=!mg.ftin,gamemode=!spectator] run function mg:foot/enter',
                    '# socles du vestiaire : rouge et bleu = équipe (une fois), blanc = quitter, or = retour au spawn (pas les spectateurs)',
                    f'execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.ftr,gamemode=!spectator,{FB.pad_box("red")}] run function mg:foot/pad_red',
                    f'execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.ftb,gamemode=!spectator,{FB.pad_box("blue")}] run function mg:foot/pad_blue',
                    f'execute as @a[tag=!mg.play,tag=!mg.out,tag=mg.ftr,gamemode=!spectator,{FB.pad_box("white")}] run function mg:foot/pad_white',
                    f'execute as @a[tag=!mg.play,tag=!mg.out,tag=mg.ftb,gamemode=!spectator,{FB.pad_box("white")}] run function mg:foot/pad_white',
                    f'execute as @a[tag=!mg.play,tag=!mg.out,gamemode=!spectator,{FB.pad_box("gold")}] run function mg:foot/leave',
                    '# dernier toucheur : un joueur à moins de 3 blocs de la balle (distance mesurée depuis la balle : pas de x,y,z dans le sélecteur)',
                    f'execute as {FB.BALL1} at @s if entity @a[gamemode=!spectator,distance=..3] run function mg:foot/touch',
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
        '# balle d\'une ancienne forme (bloc d\'oak_planks) : tuée, ball_new en fait une nouvelle',
        f'execute as {FB.BALLS} unless entity @s[nbt={{equipment:{{body:{{id:"{BALL_ITEM}"}}}}}}] run kill @s',
        f'execute store result score $ftk mg.ft if entity {FB.BALLS}',
        f'execute if score $ftk mg.ft matches 2.. run kill {FB.BALLS}',
        'execute unless score $ftk mg.ft matches 1 run function mg:foot/ball_new',
        f'execute as {FB.BALL1} unless entity @s[{FB.BALL_BOX}] run function mg:foot/ball_home',
        'function mg:foot/ball_idle',
        '# sur le terrain : pas de PvP (la chute ne fait déjà rien au lobby : core/attr_reset), score, remise à zéro du score quand il est vide',
        f'effect give @a[{Z}] minecraft:resistance 3 4 true',
        f'scoreboard players add @a[{Z}] mg.ft 0',
        f'title @a[{Z}] actionbar ' + js([{'text': '⚽ ', 'color': 'white'}] + SCORE_TXT() + [
            {'text': ' · tes buts libres ', 'color': 'gray'}, {'score': {'name': '*', 'objective': 'mg.ft'}, 'color': 'yellow'}]),
        f'execute if entity @a[{Z}] run scoreboard players set $fte mg.ft 0',
        f'execute unless entity @a[{Z}] run scoreboard players add $fte mg.ft 1',
        'execute if score $fte mg.ft matches 15.. run function mg:foot/score_reset'])
    w('foot/score_reset', ['# 30 s sans joueur sur le terrain : nouveau match', 'scoreboard players set $ftr mg.ft 0', 'scoreboard players set $ftb mg.ft 0',
                           'scoreboard players set $ftg mg.ft 0', 'scoreboard players set $fte mg.ft 0'])
    # ---------------------------------------------------------------- balle
    w('foot/ball_new', ['# Balle (sulfur_cube, bloc de test en corps : ballon du resource pack ; archétype mg:football) au centre ; '
                        'jamais mg.lby / mg.mob / mg.npc : les nettoyages du lobby la tueraient',
                        f'summon minecraft:sulfur_cube {FB.CENTRE} {{Tags:["mg.ball"],equipment:{{body:{{id:"{BALL_ITEM}",count:1}}}},'
                        'drop_chances:{body:0f},Invulnerable:1b,PersistenceRequired:1b}',
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
    w('foot/touch', ['# Balle (@s, à la position de la balle) avec un joueur à moins de 3 blocs : le plus proche devient le dernier toucheur',
                     'tag @a[tag=mg.ftlt] remove mg.ftlt', 'tag @p[gamemode=!spectator,distance=..3] add mg.ftlt'])
    w('foot/goal_free', ['# But sans équipe sur le terrain : +1 buts libres au dernier toucheur ($ftg : total, stats admin) ; chacun ne voit que SON score',
                         'scoreboard players add $ftg mg.ft 1', 'scoreboard players add @a[tag=mg.ftlt] mg.ft 1',
                         f'title @a[{Z}] subtitle ' + js([{'text': 'tes buts libres : ', 'color': 'gray'},
                                                          {'score': {'name': '*', 'objective': 'mg.ft'}, 'color': 'yellow'}]),
                         f'title @a[{Z}] title ' + js({'text': '⚽ But !', 'color': 'gold', 'bold': True}),
                         'tag @a remove mg.ftlt', 'function mg:foot/goal_fx'])
    w('foot/goal_fx', [f'execute as @a[{Z}] at @s run playsound minecraft:entity.firework_rocket.twinkle master @s ~ ~ ~ 1 1'])


def write_archetype():
    """Écrit data/mg/sulfur_cube_archetype/football.json (même format que bouncy.json vanilla) : la balle (corps test_block) roule et rebondit.
    Lu seulement au démarrage du serveur."""
    def mod(attr, amount, op):
        return {'amount': amount, 'attribute': f'minecraft:{attr}', 'id': f'{ARCH_ID}_{"add" if op == "add_value" else "mul"}_{attr}', 'operation': op}
    arch = {'attribute_modifiers': [mod('knockback_resistance', KNOCKBACK_RESIST, 'add_value'),
                                    mod('explosion_knockback_resistance', KNOCKBACK_RESIST, 'add_value'),
                                    mod('bounciness', BOUNCINESS, 'add_value'),
                                    mod('friction_modifier', FRICTION, 'add_multiplied_total'),
                                    mod('air_drag_modifier', AIR_DRAG, 'add_multiplied_total')],
            'buoyant': True, 'items': BALL_ITEM, 'knockback_modifiers': HIT_POWER,
            'sound_settings': {'hit_sound': f'{SOUND}.hit', 'push_sound': f'{SOUND}.push',
                               'push_sound_cooldown': 0.7, 'push_sound_impulse_threshold': 0.3}}
    p = os.path.join(C.D, 'sulfur_cube_archetype', 'football.json')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(C.js(arch) + '\n')
