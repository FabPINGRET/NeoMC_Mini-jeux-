"""Ragoût de la sorcière d'Halloween (importé par theme_npcs.py, jamais lancé seul) : un seul objet, l'effet est tiré à la consommation.

Objet STEW : ragoût fixe (custom_data mg_thg + mg_thst, aucun effet de ragoût, nutrition 0, mangeable rassasié grâce à can_always_eat). L'advancement mg:theme_stew (consume_item sur
mg_thst) appelle lobby/theme/stew_eat, qui ricane puis tire 1..10 : 1-4 effet vanilla (invisibilité 45 s, lueur 30 s, nausée 15 s,
lévitation 10 s suivie d'une chute lente 18 s ; durée annoncée en actionbar), 5-10 effet maison : stew_mini (taille -70 %, 45 s),
stew_moon (marche lunaire : gravité -75 %, saut +30 %, 30 s, à vérifier en jeu : ~5,5 blocs de haut), stew_rabbit (lapin : taille -65 %, saut +30 %, vitesse +20 %, 40 s, joueur invisible
et remplacé par un vrai lapin figé qui le suit, cf. ci-dessous), stew_flash (vitesse +80 %, pas +0,85, 20 s, étincelles chaque tick),
stew_skate (patinoire : friction_modifier -1,0, air_drag_modifier -0,8 et vitesse -60 %, 25 s) et stew_bounce (rebond : bounciness +0,8, saut +20 %, 30 s).
Les attributs friction_modifier, air_drag_modifier et bounciness viennent de 26.2 ; leurs ids et le sens de la glisse (valeur plus basse = plus glissant) sont vérifiés dans le registre 26.2 et les données vanilla (sulfur_cube fast_sliding : -0,95).
Rétention horizontale par tick (javap LivingEntity 26.2) = clamp(1-(1-friction du bloc)*m_friction) * clamp(1-(1-0,91)*m_traînée), m = valeur de l'attribut (base 1) : m_friction 0 et m_traînée 0,2 donnent ~0,982 (glace ~0,892).
Accélération au sol = vitesse x 0,216 / f^3 (f = friction modifiée) : sans le -60 % de vitesse, la vitesse max serait ~5,5x la marche ; avec, ~2,2x au sol ; en sautant en continu ~5x, ~10x en sprint (vitesse de vol 0,02 / 0,026 et élan de saut 0,2 non touchés par movement_speed ; avant : ~1 bloc/tick en sprint sauté).
Effets de bord de la traînée -80 % : chutes plus rapides (vitesse terminale 0,08/(1-0,996) = 20 blocs/tick au lieu de 4 en vanilla, dégâts de chute inchangés, ils dépendent de la distance), sauts ~1,30 bloc et sauts en sprint nettement plus longs (rétention en l'air 0,982 au lieu de 0,91) ; l'élytre n'est pas touché (updateFallFlyingMovement utilise des traînées fixes 0,99 / 0,98, vérifié par javap).
Un effet vanilla (1-4) se cumule avec un effet maison encore actif : un seul effet par ragoût.
Effets chronométrés : un seul à la fois (stew_clear d'abord), objectif mg.ths en secondes, modificateurs d'attribut mg:thstew
(jamais les valeurs de base), tag mg.thmini pendant le mini-moi et le lapin, mg.thzap pendant le flash. stew_clear les retire ; il est appelé par la seconde (fin, joueur
occupé, mg.pkr compris ; la fin du mini-moi est reportée tant que la tête est bloquée), par lobby/theme/<t>/off (sans contrôle de tête : accepté),
par core/request (stew_game), core/attr_reset et desinstaller. Un 2e ragoût chronométré mangé en mini sans place pour se relever
fait pschitt (stew_fizzle, sans toucher aux attributs). Les anciens ragoûts (mg_thg sans mg_thst, effets vanilla) sont retirés chaque seconde ; leurs effets darkness / hunger /
luck restent effacés au lancement d'une partie (stew_game) pendant la transition. Tout reste sous lobby/theme/ (cf. theme_world.load).
Lapin : tag mg.thbun (joueur et lapin), objectif mg.thbn = identifiant du lapin (compteur $thbn, copié sur le joueur et sur son lapin), équipe mg_thbun
(collisionRule never, créée par core/load, retirée par desinstaller). stew_rabbit_tp (chaque tick, par lobby/theme/tick) recolle le lapin au joueur ;
stew_rabbit_keep (chaque seconde) le recrée s'il a disparu, rafraîchit l'invisibilité courte (3 s) du joueur ; les lapins orphelins (tag mg.thbo posé puis non retiré) sont tués dans la même seconde.
Limites connues : objets tenus, armure et chapeaux restent visibles sur le joueur-lapin ; la fin du lapin efface l'invisibilité, y compris une invisibilité vanilla (tirage 1) mangée pendant.
"""
import json
import os

import common as C

MOD = 'mg:thstew'
STEW = ('minecraft:suspicious_stew[minecraft:custom_data={mg_thg:1b,mg_thst:1b},minecraft:custom_name={"text":"Ragoût mystère","color":"gold","italic":false},'
        'minecraft:lore=[{"text":"Une sorcière y a jeté un peu de tout…","color":"gray","italic":false},'
        '{"text":"Effet : surprise !","color":"dark_purple","italic":false}],'
        'minecraft:food={nutrition:0,saturation:0f,can_always_eat:true},!minecraft:use_remainder,'
        'minecraft:suspicious_stew_effects=[]]')
OLD_STEW = 'minecraft:suspicious_stew[minecraft:custom_data={mg_thg:1b}]'                # ancien ragoût : custom_data exactement mg_thg
VANILLA = [('invisibility', 45, '👻 Invisible !', 'gray', []), ('glowing', 30, '✨ Tu brilles à travers les murs !', 'yellow', []),
           ('nausea', 15, '😵 Le monde tourne…', 'dark_green', []),
           ('levitation', 10, '🎈 Tu t\'envoles… et tu redescends en douceur', 'light_purple', [('slow_falling', 18)])]   # tirages 1..4 : (effet, secondes, texte, couleur, effets en plus)
OLD_EFFECTS = ['darkness', 'hunger', 'luck']                                             # effets des anciens ragoûts
CUSTOM = ['mini', 'moon', 'rabbit', 'flash', 'skate', 'bounce']                          # tirages 5..10
SKATE = [('friction_modifier', -1.0), ('air_drag_modifier', -0.8), ('movement_speed', -0.6)]   # friction -100 %, traînée de l'air -80 %, vitesse -60 % (rétention ~0,982/tick, avant 0,946, glace ~0,892 : glissade ~3x plus longue ; vitesse max ~2,2x la marche (au sol) : 0,04 x 0,216 = 0,0086/tick / (1 - 0,982) ; saut ~1,30 bloc (avant ~1,28, vanilla ~1,25))
OP = 'add_multiplied_base'                                                               # opération par défaut des modificateurs
ATTRS = ('scale', 'gravity', 'jump_strength', 'movement_speed', 'step_height', 'friction_modifier', 'air_drag_modifier', 'bounciness')
F = 'lobby/theme'
SELF = 'execute at @s run playsound minecraft:'
NO_ROOM = ('execute if entity @s[tag=mg.thmini] at @s unless block ~ ~1 ~ #minecraft:replaceable '
           f'run return run function mg:{F}/stew_fizzle')     # mini-moi sans place pour se relever : pschitt, ni stew_clear ni attribut (le joueur serait redimensionné coincé)
RB = 'minecraft:rabbit'
RABBIT_AS = f'as @e[type={RB},tag=mg.thbun] if score @s mg.thbn = $thbi mg.st run '    # lapin du joueur courant (id copié dans $thbi)
RABBIT_ID = 'execute ' + RABBIT_AS
INVIS = 'effect give @s minecraft:invisibility 3 0 true'                                 # courte : rafraîchie chaque seconde par stew_rabbit_keep
COPY_ID = 'scoreboard players operation $thbi mg.st = @s mg.thbn'


def bar(text, color):
    return 'title @s actionbar ' + C.js({'text': text, 'color': color})


def stew_busy(busy):
    """Joueurs qui n'ont pas de ragoût : les occupés du thème, plus le parkour (mg.pkr)."""
    return list(busy) + ['mg.pkr']


def eat(busy):
    lines = ['# 🎃 Ragoût mystère consommé (advancement mg:theme_stew ; @s = joueur) : ricanement, puis effet tiré au hasard',
             'advancement revoke @s only mg:theme_stew',
             '# hors thème, en partie, en survie ou occupé ailleurs : consommé sans effet']
    lines.append('execute unless score $theme mg.st matches 1.. run return 0')
    lines += [f'execute if entity @s[tag={t}] run return 0' for t in ['mg.surv'] + stew_busy(busy)]
    lines += [SELF + 'entity.witch.ambient neutral @a[distance=..16] ~ ~ ~ 1 1',
              f'execute store result score $thr mg.st run random value 1..{len(VANILLA) + len(CUSTOM)}']
    for i, (e, s, text, color, extras) in enumerate(VANILLA, 1):
        pre = f'execute if score $thr mg.st matches {i} run '
        lines += [pre + bar(f'{text} ({s} s)', color)] + [pre + f'effect give @s minecraft:{x} {xs} 0' for x, xs in extras] + \
                 [pre + f'return run effect give @s minecraft:{e} {s} 0']
    return lines + [f'execute if score $thr mg.st matches {i} run return run function mg:{F}/stew_{k}' for i, k in enumerate(CUSTOM, len(VANILLA) + 1)]


def timed(desc, mods, secs, sound, pitch, msg, color, extra=()):
    """Effet chronométré : le précédent est retiré, modificateurs (attribut, valeur[, opération]) ajoutés, compte à rebours mg.ths."""
    return [f'# 🎃 Ragoût ({desc}, {secs} s, objectif mg.ths) ; @s = joueur', NO_ROOM,f'function mg:{F}/stew_clear'] + \
           [f'attribute @s minecraft:{a} modifier add {MOD} {v} {op[0] if op else OP}' for a, v, *op in mods] + list(extra) + \
           [f'scoreboard players set @s mg.ths {secs}', SELF + f'entity.{sound} neutral @a[distance=..16] ~ ~ ~ 1 {pitch}', bar(f'{msg} ({secs} s)', color)]


def clear():
    return ['# Retire les modificateurs, le tag mini-moi / lapin / flash, le lapin et le chrono du ragoût chez @s (silencieux ; jamais les valeurs de base)'] + \
           [f'attribute @s minecraft:{a} modifier remove {MOD}' for a in ATTRS] + \
           ['execute if entity @s[tag=mg.thbun] run effect clear @s minecraft:invisibility',
            'execute if entity @s[tag=mg.thbun] run ' + COPY_ID,
            'execute if entity @s[tag=mg.thbun] ' + RABBIT_AS + 'kill @s',
            'tag @s remove mg.thmini', 'tag @s remove mg.thbun', 'tag @s remove mg.thzap', 'scoreboard players reset @s mg.ths']


def game():
    extras = [x for *_, ex in VANILLA for x, _ in ex]
    return ['# Lancement d\'une partie (@s = participant) : plus d\'effet de ragoût (anciens ragoûts compris : transition)'] + \
           [f'effect clear @s minecraft:{e}' for e in [v[0] for v in VANILLA] + extras + OLD_EFFECTS] + [f'function mg:{F}/stew_clear']


def fizzle():
    return ['# 🎃 Ragoût : pschitt, instantané (@s = joueur) ; repli du ragoût chronométré sans place pour se relever, mini-moi sous un bloc (aucun attribut touché, pas de stew_clear)',
            SELF + 'entity.witch.celebrate neutral @a[distance=..16] ~ ~ ~ 1 1.4',
            'execute at @s run particle minecraft:smoke ~ ~1 ~ 0.3 0.3 0.3 0.02 10 normal',
            'execute at @s run particle minecraft:poof ~ ~1 ~ 0.3 0.3 0.3 0.02 6 normal',
            bar('🫧 Le ragoût fait pschitt… rien ne se passe', 'gray')]


def rabbit_body():
    """Crée le lapin figé du joueur (@s = joueur) : id attribué au premier lapin, repris ensuite ; le lapin hérite de l'id puis rejoint l'équipe sans collision."""
    new = f'@e[type={RB},tag=mg.thbnew]'
    return ['# 🎃 Lapin du ragoût : un vrai lapin figé, appelé par stew_rabbit et stew_rabbit_keep (@s = joueur) ; id du joueur conservé (mg.thbn)',
            'execute unless score @s mg.thbn matches 1.. run scoreboard players add $thbn mg.st 1',
            'execute unless score @s mg.thbn matches 1.. run scoreboard players operation @s mg.thbn = $thbn mg.st',
            'execute at @s run summon minecraft:rabbit ~ ~ ~ {Tags:["mg.thbun","mg.thbnew"],NoAI:1b,Silent:1b,Invulnerable:1b,PersistenceRequired:1b,'
            'DeathLootTable:"minecraft:empty",attributes:[{id:"minecraft:scale",base:0.8}]}',
            f'scoreboard players operation {new} mg.thbn = @s mg.thbn',
            f'team join mg_thbun {new}',
            f'tag {new} remove mg.thbnew']


def rabbit_tp():
    return ['# Chaque tick (lobby/theme/tick ; @s = joueur lapin, à sa position) : le lapin se recolle au joueur, dans son axe', COPY_ID,
            RABBIT_ID + 'tp @s ~ ~ ~ ~ 0']


def rabbit_keep():
    """Chaque seconde (@s = joueur lapin) : le lapin du joueur échappe au balayage ; recréé s'il n'existe plus nulle part."""
    return ['# Chaque seconde (lobby/theme/npc_second ; @s = joueur lapin) : invisibilité rafraîchie, son lapin est gardé (tag mg.thbo retiré), recréé s\'il a disparu',
            INVIS, COPY_ID,
            RABBIT_ID + 'tag @s remove mg.thbo', 'scoreboard players set $thbf mg.st 0', RABBIT_ID + 'scoreboard players set $thbf mg.st 1',
            f'execute if score $thbf mg.st matches 0 run function mg:{F}/stew_rabbit_body']


def write_files(busy):
    """Écrit stew_eat/clear/game/mini/moon/fizzle/rabbit(_body/_tp/_keep)/flash/skate/bounce et l'advancement mg:theme_stew."""
    w = C.w
    w(f'{F}/stew_eat', eat(busy))
    w(f'{F}/stew_clear', clear())
    w(f'{F}/stew_game', game())
    w(f'{F}/stew_mini', timed('mini-moi : taille -70 %', [('scale', -0.7)], 45, 'allay.item_given', 2, '🍄 Mini-moi : tu rétrécis !', 'light_purple',
                              extra=['tag @s add mg.thmini']))
    w(f'{F}/stew_moon', timed('marche lunaire : gravité -75 %, saut +30 %', [('gravity', -0.75), ('jump_strength', 0.3)], 30,
                              'enderman.teleport', 0.6, '🌙 Marche lunaire : saute très haut !', 'aqua'))
    w(f'{F}/stew_fizzle', fizzle())
    w(f'{F}/stew_rabbit', timed('lapin : taille -65 %, saut +30 %, vitesse +20 %, vrai lapin figé', [('scale', -0.65), ('jump_strength', 0.3), ('movement_speed', 0.2)], 40,
                                'rabbit.jump', 1.2, '🐰 Tu es un lapin !', 'gold',
                                extra=['tag @s add mg.thmini', 'tag @s add mg.thbun', INVIS,
                                       'execute at @s run particle minecraft:poof ~ ~0.4 ~ 0.3 0.3 0.3 0.02 12 normal', f'function mg:{F}/stew_rabbit_body']))
    w(f'{F}/stew_rabbit_body', rabbit_body())
    w(f'{F}/stew_rabbit_tp', rabbit_tp())
    w(f'{F}/stew_rabbit_keep', rabbit_keep())
    w(f'{F}/stew_flash', timed('flash : vitesse +80 %, pas +0,85', [('movement_speed', 0.8), ('step_height', 0.85)], 20,
                               'breeze.wind_burst', 1.2, '⚡ Flash : super vitesse !', 'yellow', extra=['tag @s add mg.thzap']))
    w(f'{F}/stew_skate', timed('patinoire : friction -100 %, traînée de l\'air -80 %, vitesse -60 %', SKATE, 25, 'player.hurt_freeze', 1, '⛸ Patinoire : ça glisse !', 'aqua'))
    w(f'{F}/stew_bounce', timed('rebond : bounciness +0,8, saut +20 %', [('bounciness', 0.8, 'add_value'), ('jump_strength', 0.2)], 30,
                                'slime.jump', 1, '🏀 Tu rebondis !', 'gold'))
    for rel, obj in (('advancement/theme_stew.json',
                      {'criteria': {'stew': {'trigger': 'minecraft:consume_item', 'conditions': {'item': {'predicates': {
                          'minecraft:custom_data': '{mg_thst:1b}'}}}}}, 'rewards': {'function': f'mg:{F}/stew_eat'}}),):
        path = os.path.join(C.D, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(json.dumps(obj, indent=2, ensure_ascii=False) + '\n')


def second_lines(busy):
    """Chaque seconde : anciens ragoûts retirés, compte à rebours, fin (reportée pour le mini si la tête est bloquée), joueur occupé, lapins gardés."""
    return ['# Ragoût mystère : anciens ragoûts (effets vanilla) retirés ; compte à rebours (mg.ths)',
            f'clear @a {OLD_STEW}',
            'scoreboard players remove @a[scores={mg.ths=1..}] mg.ths 1',
            '# à 0, le mini-moi ne reprend pas sa taille sous un plafond bas : reporté d\'une seconde',
            'execute as @a[tag=mg.thmini,scores={mg.ths=0}] at @s unless block ~ ~1 ~ #minecraft:replaceable run scoreboard players set @s mg.ths 1',
            'execute as @a[scores={mg.ths=0}] at @s run playsound minecraft:block.amethyst_block.chime neutral @a[distance=..16] ~ ~ ~ 1 0.8',
            f'execute as @a[scores={{mg.ths=0}}] run function mg:{F}/stew_clear'] + \
           [f'execute as @a[tag={t},scores={{mg.ths=1..}}] run function mg:{F}/stew_clear' for t in stew_busy(busy)] + \
           ['# lapins : tous marqués orphelins, ceux des joueurs lapin sont gardés (stew_rabbit_keep), les autres tués',
            f'tag @e[type={RB},tag=mg.thbun] add mg.thbo',
            f'execute as @a[tag=mg.thbun] run function mg:{F}/stew_rabbit_keep',
            f'kill @e[type={RB},tag=mg.thbo]']


def off_lines():
    """Ajouté au off du thème : lobby/theme/tick ne tourne plus sans thème, plus personne ne ferait fondre l'effet."""
    return [f'execute as @a[scores={{mg.ths=1..}}] run function mg:{F}/stew_clear', f'kill @e[type={RB},tag=mg.thbun]']


def wire():
    """Objectifs mg.ths / mg.thbn, équipe mg_thbun, boucle du lapin (tick), anciens effets de ragoût retirés de core/request, nettoyages (partie, attr_reset, désinstallation).
    Appelé en dernier par theme_npcs.wire() : l'ancre de core/request est posée par celui-ci."""
    C.objectives([('mg.ths', 'dummy')])
    C.objectives([('mg.thbn', 'dummy')])       # appel séparé : C.patch ne fait rien seulement si TOUTES les lignes sont déjà là (sinon mg.ths en double)
    C.patch('core/load', 'scoreboard objectives add mg.bw trigger', ['team add mg_thbun'])      # un patch par ligne indépendante (cf. ci-dessus)
    C.patch('core/load', 'team add mg_thbun', ['team modify mg_thbun collisionRule never'])
    C.patch('lobby/theme/tick', 'scoreboard players add $tht mg.st 1', [f'execute as @a[tag=mg.thbun] at @s run function mg:{F}/stew_rabbit_tp'], where='before')
    C.patch('lobby/theme/tick', 'scoreboard players add $tht mg.st 1',
            ['execute as @a[tag=mg.thzap] at @s run particle minecraft:electric_spark ~ ~0.2 ~ 0.2 0.1 0.2 0 2 normal'], where='before')
    C.drop_lines('core/request', [f'effect clear @a[tag=mg.play] minecraft:{e}' for e in ('invisibility', 'glowing', 'nausea', 'darkness', 'hunger', 'luck')])
    C.patch('core/request', 'scoreboard players reset @a[tag=!mg.surv] mg.thfw', [f'execute as @a[tag=mg.play] run function mg:{F}/stew_game'])
    C.patch('core/attr_reset', 'function mg:core/attr_reset_g', [f'function mg:{F}/stew_clear'])
    C.patch('desinstaller', 'advancement revoke @a only mg:theme_fw',
            ['advancement revoke @a only mg:theme_stew', f'execute as @a run function mg:{F}/stew_clear'])
    C.patch('desinstaller', f'execute as @a run function mg:{F}/stew_clear', [f'kill @e[type={RB},tag=mg.thbun]'])
    C.patch('desinstaller', f'kill @e[type={RB},tag=mg.thbun]', ['team remove mg_thbun'])
