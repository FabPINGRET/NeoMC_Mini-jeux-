"""Ragoût de la sorcière d'Halloween (importé par theme_npcs.py, jamais lancé seul) : un seul objet, l'effet est tiré à la consommation.

Objet STEW : ragoût fixe (custom_data mg_thg + mg_thst, aucun effet de ragoût). L'advancement mg:theme_stew (consume_item sur
mg_thst) appelle lobby/theme/stew_eat, qui ricane puis tire 1..8 : 1-4 effet vanilla (invisibilité, lueur, nausée, lévitation),
5-8 effet maison : stew_mini (taille -70 %, 30 s), stew_moon (marche lunaire : gravité -75 %, saut +30 %, 20 s, à vérifier en jeu :
~5,5 blocs de haut), stew_burp et stew_wind (instantanés). Le vent (charge de vent sous les pieds, le mangeur en est le propriétaire)
tombe en rot si stew_wind_ok : joueur en élytres libres, pas de sol sous les pieds, ou bloc fragile (tag mg:wind_touchy) à moins de 2 blocs en horizontale (y -1..+2) ou un
armor_stand / mannequin à moins de 4 blocs. Un effet vanilla (1-4) se cumule avec un effet maison encore actif : un seul effet par ragoût.
Effets chronométrés : un seul à la fois (stew_clear d'abord), objectif mg.ths en secondes, modificateurs d'attribut mg:thstew
(jamais les valeurs de base), tag mg.thmini pendant le mini-moi. stew_clear les retire ; il est appelé par la seconde (fin, joueur
occupé ; la fin du mini-moi est reportée tant que la tête est bloquée), par lobby/theme/<t>/off (sans contrôle de tête : accepté),
par core/request (stew_game), core/attr_reset et desinstaller. Un 2e ragoût chronométré mangé en mini sans place pour se relever
tombe en rot. Les anciens ragoûts (mg_thg sans mg_thst, effets vanilla) sont retirés chaque seconde ; leurs effets darkness / hunger /
luck restent effacés au lancement d'une partie (stew_game) pendant la transition. Tout reste sous lobby/theme/ (cf. theme_world.load).
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
VANILLA = [('invisibility', 20), ('glowing', 10), ('nausea', 8), ('levitation', 5)]      # tirages 1..4 (secondes)
OLD_EFFECTS = ['darkness', 'hunger', 'luck']                                             # effets des anciens ragoûts
CUSTOM = ['mini', 'moon', 'burp', 'wind']                                                # tirages 5..8
TOUCHY = ['#minecraft:doors', '#minecraft:trapdoors', '#minecraft:fence_gates', '#minecraft:buttons',
          'minecraft:lever', 'minecraft:bell', '#minecraft:candles', '#minecraft:candle_cakes']      # blocs que le coup de vent déclencherait
F = 'lobby/theme'
SELF = 'execute at @s run playsound minecraft:'
ROT = ('execute if entity @s[tag=mg.thmini] at @s unless block ~ ~1 ~ #minecraft:replaceable '
       f'run return run function mg:{F}/stew_burp')           # mini-moi sans place pour se relever : pas d'autre effet chronométré


def bar(text, color):
    return 'title @s actionbar ' + C.js({'text': text, 'color': color})


def eat(busy):
    lines = ['# 🎃 Ragoût mystère consommé (advancement mg:theme_stew ; @s = joueur) : ricanement, puis effet tiré au hasard',
             'advancement revoke @s only mg:theme_stew',
             '# hors thème, en partie, en survie ou occupé ailleurs : consommé sans effet']
    lines.append('execute unless score $theme mg.st matches 1.. run return 0')
    lines += [f'execute if entity @s[tag={t}] run return 0' for t in ['mg.surv'] + busy]
    lines += [SELF + 'entity.witch.ambient neutral @a[distance=..16] ~ ~ ~ 1 1',
              f'execute store result score $thr mg.st run random value 1..{len(VANILLA) + len(CUSTOM)}']
    lines += [f'execute if score $thr mg.st matches {i} run return run effect give @s minecraft:{e} {s} 0' for i, (e, s) in enumerate(VANILLA, 1)]
    return lines + [f'execute if score $thr mg.st matches {i} run return run function mg:{F}/stew_{k}' for i, k in enumerate(CUSTOM, len(VANILLA) + 1)]


def timed(desc, mods, secs, sound, pitch, msg, color, extra=()):
    """Effet chronométré : le précédent est retiré, modificateurs ajoutés, compte à rebours mg.ths."""
    return [f'# 🎃 Ragoût ({desc}, {secs} s, objectif mg.ths) ; @s = joueur', ROT, f'function mg:{F}/stew_clear'] + \
           [f'attribute @s minecraft:{a} modifier add {MOD} {v} add_multiplied_base' for a, v in mods] + list(extra) + \
           [f'scoreboard players set @s mg.ths {secs}', SELF + f'entity.{sound} neutral @a[distance=..16] ~ ~ ~ 1 {pitch}', bar(msg, color)]


def clear():
    return ['# Retire les modificateurs, le tag mini-moi et le chrono du ragoût chez @s (silencieux ; jamais les valeurs de base)'] + \
           [f'attribute @s minecraft:{a} modifier remove {MOD}' for a in ('scale', 'gravity', 'jump_strength')] + \
           ['tag @s remove mg.thmini', 'scoreboard players reset @s mg.ths']


def game():
    return ['# Lancement d\'une partie (@s = participant) : plus d\'effet de ragoût (anciens ragoûts compris : transition)'] + \
           [f'effect clear @s minecraft:{e}' for e in [e for e, _ in VANILLA] + OLD_EFFECTS] + [f'function mg:{F}/stew_clear']


def burp():
    return ['# 🎃 Ragoût : rot de sorcière, instantané (@s = joueur) ; aussi le repli du coup de vent et du ragoût sans place',
            SELF + 'entity.player.burp neutral @a[distance=..16] ~ ~ ~ 2 0.5',
            'execute at @s run particle minecraft:dust{color:[0.35,0.8,0.2],scale:1.2} ~ ~1.5 ~ 0.3 0.2 0.3 0.02 14 normal',
            'execute at @s run title @a[distance=..10,tag=!mg.play] actionbar [{"selector":"@s"}," a roté comme une sorcière !"]']


def wind():
    owner = 'minecraft:wind_charge,tag=mg.thwind'
    return ['# 🎃 Ragoût : coup de vent sous les pieds, instantané (@s = joueur) ; rot si stew_wind_ok refuse',
            f'execute store result score $thw mg.st at @s run function mg:{F}/stew_wind_ok',
            f'execute if score $thw mg.st matches 0 run return run function mg:{F}/stew_burp',
            'execute at @s run summon minecraft:wind_charge ~ ~0.05 ~ {Tags:["mg.thwind"],Motion:[0d,-1d,0d]}',
            f'data modify entity @e[type={owner},limit=1] Owner set from entity @s UUID',
            f'tag @e[type={owner}] remove mg.thwind']


def wind_ok():
    """1 si rien de fragile autour des pieds (@s, position = pieds) : tout refus sort en 0, la valeur est toujours écrite."""
    rng = lambda lo, hi: [f'{d}' if d else '' for d in range(lo, hi + 1)]
    return ['# Le coup de vent est-il sans risque ? 0 : en vol (élytres libres) ou sans sol sous les pieds (la charge exploserait loin en bas),',
            '# bloc déclenchable (#mg:wind_touchy, x/z -2..2, y -1..2) ou mannequin à moins de 4 blocs',
            'execute if entity @s[tag=mg.elyf] run return 0',
            'execute if block ~ ~-1 ~ #minecraft:replaceable run return 0'] + \
           [f'execute if block ~{dx} ~{dy} ~{dz} #mg:wind_touchy run return 0'
            for dx in rng(-2, 2) for dy in rng(-1, 2) for dz in rng(-2, 2)] + \
           [f'execute if entity @e[type={t},distance=..4] run return 0' for t in ('minecraft:armor_stand', 'minecraft:mannequin')] + ['return 1']


def write_files(busy):
    """Écrit stew_eat/clear/game/mini/moon/burp/wind/wind_ok, l'advancement mg:theme_stew et le tag de blocs mg:wind_touchy."""
    w = C.w
    w(f'{F}/stew_eat', eat(busy))
    w(f'{F}/stew_clear', clear())
    w(f'{F}/stew_game', game())
    w(f'{F}/stew_mini', timed('mini-moi : taille -70 %', [('scale', -0.7)], 30, 'allay.item_given', 2, '🍄 Tu rétrécis !', 'light_purple',
                              extra=['tag @s add mg.thmini']))
    w(f'{F}/stew_moon', timed('marche lunaire : gravité -75 %, saut +30 %', [('gravity', -0.75), ('jump_strength', 0.3)], 20,
                              'enderman.teleport', 0.6, '🌙 Marche lunaire !', 'aqua'))
    w(f'{F}/stew_burp', burp())
    w(f'{F}/stew_wind', wind())
    w(f'{F}/stew_wind_ok', wind_ok())
    for rel, obj in (('tags/block/wind_touchy.json', {'values': TOUCHY}),
                     ('advancement/theme_stew.json',
                      {'criteria': {'stew': {'trigger': 'minecraft:consume_item', 'conditions': {'item': {'predicates': {
                          'minecraft:custom_data': '{mg_thst:1b}'}}}}}, 'rewards': {'function': f'mg:{F}/stew_eat'}})):
        path = os.path.join(C.D, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(json.dumps(obj, indent=2, ensure_ascii=False) + '\n')


def second_lines(busy):
    """Chaque seconde : anciens ragoûts retirés, compte à rebours, fin (reportée pour le mini si la tête est bloquée), joueur occupé."""
    return ['# Ragoût mystère : anciens ragoûts (effets vanilla) retirés ; compte à rebours (mg.ths)',
            f'clear @a {OLD_STEW}',
            'scoreboard players remove @a[scores={mg.ths=1..}] mg.ths 1',
            '# à 0, le mini-moi ne reprend pas sa taille sous un plafond bas : reporté d\'une seconde',
            'execute as @a[tag=mg.thmini,scores={mg.ths=0}] at @s unless block ~ ~1 ~ #minecraft:replaceable run scoreboard players set @s mg.ths 1',
            'execute as @a[scores={mg.ths=0}] at @s run playsound minecraft:block.amethyst_block.chime neutral @a[distance=..16] ~ ~ ~ 1 0.8',
            f'execute as @a[scores={{mg.ths=0}}] run function mg:{F}/stew_clear'] + \
           [f'execute as @a[tag={t},scores={{mg.ths=1..}}] run function mg:{F}/stew_clear' for t in busy]


def off_lines():
    """Ajouté au off du thème : lobby/theme/tick ne tourne plus sans thème, plus personne ne ferait fondre l'effet."""
    return [f'execute as @a[scores={{mg.ths=1..}}] run function mg:{F}/stew_clear']


def wire():
    """Objectif mg.ths, anciens effets de ragoût retirés de core/request, nettoyages (partie, attr_reset, désinstallation).
    Appelé en dernier par theme_npcs.wire() : l'ancre de core/request est posée par celui-ci."""
    C.objectives([('mg.ths', 'dummy')])
    C.drop_lines('core/request', [f'effect clear @a[tag=mg.play] minecraft:{e}' for e in ('invisibility', 'glowing', 'nausea', 'darkness', 'hunger', 'luck')])
    C.patch('core/request', 'scoreboard players reset @a[tag=!mg.surv] mg.thfw', [f'execute as @a[tag=mg.play] run function mg:{F}/stew_game'])
    C.patch('core/attr_reset', 'function mg:core/attr_reset_g', [f'function mg:{F}/stew_clear'])
    C.patch('desinstaller', 'advancement revoke @a only mg:theme_fw',
            ['advancement revoke @a only mg:theme_stew', f'execute as @a run function mg:{F}/stew_clear'])
