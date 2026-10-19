"""👑 Ombrelune : les 9 boss (phases, attaques, barres de vie, récompenses) et les 8 donjons (salles à vagues, portes, alpha).
Module importé par gen_ombrelune.py.

Boss : $ob<i> actif (0/1), $obc<i> attente avant de pouvoir revenir, $obr<i> secondes sans joueur, $obt<i>_<j> minuteurs des attaques.
Donjons : $od<i> état (0 libre, 1..3 vague de la salle, 4 alpha, 5 terminé), $odw<i> secondes sans joueur.
"""
import math

import ol_world as W
import ol_structs as S
import ol_mobs as M
import ol_quest as Q
from ol_core import w, js, P, TEXT, DIM, bit_test

A = S.ARENAS


def leather(col, *slots):
    return ','.join(f'{s}:{{id:"minecraft:leather_{p}",count:1,components:{{"minecraft:dyed_color":{col}}}}}' for s, p in slots)


def resist(hp):
    """PV au-delà du plafond de 1024 : compensés par un effet de résistance (chaque niveau = -20 % de dégâts)."""
    r = 0 if hp <= 1150 else (1 if hp <= 1500 else (2 if hp <= 2400 else 3))
    return (f'active_effects:[{{id:"minecraft:resistance",amplifier:{r - 1},duration:-1,show_particles:0b}}],' if r else '')


def mob(m, name, col, hp, dmg, scale, extra='', eq='', spd=0.3, kb=0.8):
    nmj = js(TEXT(name, col, bold=True))
    extra = resist(hp) + extra
    hp = min(hp, 1024)
    eqs = f'equipment:{{{eq}}},drop_chances:{{mainhand:0f,offhand:0f,head:0f,chest:0f,legs:0f,feet:0f}},' if eq else ''
    return (f'summon minecraft:{m} ~ ~ ~ {{Tags:["mg.ol","mg.olm","mg.olboss","mg.ollast","mg.olbn"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",'
            f'CanPickUpLoot:0b,CustomName:{nmj},CustomNameVisible:1b,Health:{hp}f,{eqs}{extra}'
            f'attributes:[{{id:"minecraft:max_health",base:{hp}}},{{id:"minecraft:attack_damage",base:{dmg}}},{{id:"minecraft:scale",base:{scale}}},'
            f'{{id:"minecraft:follow_range",base:48}},{{id:"minecraft:movement_speed",base:{spd}}},{{id:"minecraft:knockback_resistance",base:{kb}}},'
            f'{{id:"minecraft:step_height",base:1.5}}]}}')


# clé : nom, couleur (barre), invocation, PV, attaques [(nom, période en s)], région
BOSSES = {
    'brennic': ('Brennic, seigneur des brigands', 'red', [mob('vindicator', 'Brennic', 'red', 320, 9, 1.3, eq='mainhand:{id:"minecraft:iron_axe",count:1},head:{id:"minecraft:golden_helmet",count:1},chest:{id:"minecraft:golden_chestplate",count:1}')],
                320, [('whirl', 7), ('call', 20), ('charge', 11)], 'w'),
    'ystar': ('Ysh\'tar, la reine-araignée', 'green', [mob('spider', 'Ysh\'tar', 'dark_green', 650, 10, 3.4, spd=0.32)], 650,
              [('web', 6), ('brood', 15), ('venom', 8), ('leap', 10)], 'nw'),
    'hrimgar': ('Hrimgar, le géant du givre', 'blue', [mob('zombie', 'Hrimgar', 'aqua', 1000, 16, 3.0, extra='CanBreakDoors:0b,',
                                                          eq='mainhand:{id:"minecraft:iron_axe",count:1},' + leather(14741759, ('head', 'helmet'), ('chest', 'chestplate'), ('legs', 'leggings')), spd=0.28)],
                1000, [('slam', 7), ('breath', 10), ('spikes', 9), ('wolves', 25)], 'n'),
    'morvaine': ('Morvaine, la mère-sorcière', 'purple', [mob('witch', 'Morvaine', 'dark_purple', 1200, 10, 1.4)], 1200,
                 [('blink', 8), ('swarm', 14), ('hex', 9), ('cloud', 11)], 'ne'),
    'sethkar': ('Sethkar, le pharaon-liche', 'yellow', [mob('wither_skeleton', 'Sethkar', 'gold', 1500, 18, 1.6,
                                                            eq='mainhand:{id:"minecraft:golden_sword",count:1},head:{id:"minecraft:golden_helmet",count:1}')], 1500,
                [('storm', 13), ('mummies', 16), ('beam', 7), ('jars', 1)], 'e'),
    'ignarok': ('Ignarok, dragon de feu', 'red', ['function mg:ombre/beast/ignarok', 'tag @e[tag=mg.ollast] add mg.olbn'], 1800,
                [('breath', 6), ('gust', 12), ('flight', 22), ('tail', 8)], 'se'),
    'colosse': ('Le Colosse de runes', 'blue', [mob('iron_golem', 'Colosse de runes', 'blue', 2400, 24, 2.8, extra='PlayerCreated:0b,', spd=0.26, kb=1.0)], 2400,
                [('quake', 8), ('beam', 6), ('rocks', 15), ('shield', 1)], 's'),
    'malveth': ('Malveth, l\'archimage', 'purple', [mob('evoker', 'Malveth', 'dark_purple', 2800, 14, 1.4, spd=0.34)], 2800,
                [('bolt', 5), ('blink', 9), ('guards', 1), ('dark', 12)], 'sw'),
    'nyxar': ('Nyxar, dragon de la Lune Noire', 'purple', ['function mg:ombre/beast/nyxar', 'tag @e[tag=mg.ollast] add mg.olbn'], 3200,
              [('breath', 6), ('dive', 14), ('spectres', 18), ('roar', 11)], 'sw'),
}
BK = list(BOSSES)
BIDX = {k: i for i, k in enumerate(BK)}


def arena(k):
    a = A[k]
    return a['c'], a['r']


SECOND = ['# Chaque seconde : boss (déclenchement, suivi, victoire) et donjons']
SETUP = ['# Session : barres des boss et des alphas']
CLEAR = ['# Fin de session : barres retirées']
for k, (name, col, summ, hp, abil, reg) in BOSSES.items():
    i = BIDX[k]
    (cx, cy, cz), r = arena(k)
    step = Q.BOSS_STEP[k]
    tag = f'mg.olb_{k}'
    at = f'positioned {cx} {cy} {cz}'
    ri = W.ORDER.index(reg) + 1
    home = A[k].get('home', (cx, cy, cz))
    SETUP += [f'bossbar add mg:olb{i} {js(TEXT("👑 " + name, "gold"))}', f'bossbar set mg:olb{i} color {col}', f'bossbar set mg:olb{i} style notched_10',
              f'bossbar set mg:olb{i} max {min(hp, 1024)}', f'bossbar set mg:olb{i} players', f'scoreboard players set $ob{i} mg.st 0', f'scoreboard players set $obc{i} mg.st 0']
    CLEAR += [f'bossbar remove mg:olb{i}', f'scoreboard players set $ob{i} mg.st 0']
    # ---- départ
    START = [f'# {name} : début du combat', f'execute positioned {home[0]} {home[1]} {home[2]} run function mg:{P}/boss/{k}_spawn',
             f'scoreboard players set $ob{i} mg.st 1', f'scoreboard players set $obr{i} mg.st 0', f'scoreboard players set $obp{i} mg.st 0'] + \
            [f'scoreboard players set $obt{i}_{j} mg.st {per + 3}' for j, (an, per) in enumerate(abil)] + \
            [f'bossbar set mg:olb{i} value {min(hp, 1024)}', f'execute {at} as @a[tag=mg.olw,gamemode=adventure,distance=..{r + 24}] run function mg:{P}/cs/boss_{k}',
             f'execute as @e[tag={tag}] run data merge entity @s {{NoAI:1b}}', f'schedule function mg:{P}/boss/wake 120t']
    w(f'boss/{k}_start', START)
    w(f'boss/{k}_spawn', [f'# {name} : apparition (ici)'] + summ + [f'tag @e[tag=mg.olbn] add {tag}', 'tag @e[tag=mg.olbn] add mg.olboss', 'tag @e[tag=mg.olbn] add mg.olm',
                                                                    'scoreboard players operation @e[tag=mg.olbn] mg.olses = $olses mg.st', 'tag @e[tag=mg.olbn] remove mg.olbn'])
    # ---- chaque seconde
    TICK = [f'# {name} : chaque seconde', f'execute {at} run bossbar set mg:olb{i} players @a[tag=mg.olw,distance=..{r + 26}]',
            f'execute store result bossbar mg:olb{i} value run data get entity @e[tag={tag},limit=1] Health',
            f'execute {at} run tag @a[tag=mg.olw,distance=..{r + 8}] add mg.olboss_in',
            f'execute {at} unless entity @e[tag={tag},distance=..{r + 6}] run tp @e[tag={tag}] {home[0]} {home[1]} {home[2]}',
            f'execute {at} unless entity @a[tag=mg.olw,gamemode=adventure,distance=..{r + 22}] run scoreboard players add $obr{i} mg.st 1',
            f'execute {at} if entity @a[tag=mg.olw,gamemode=adventure,distance=..{r + 22}] run scoreboard players set $obr{i} mg.st 0',
            f'execute if score $obr{i} mg.st matches 15.. run return run function mg:{P}/boss/{k}_reset',
            f'execute as @e[tag={tag}] store result score $hp mg.st run data get entity @s Health',
            f'execute if score $hp mg.st matches ..{min(hp, 1024) // 4} as @e[tag={tag},tag=!mg.olrage] at @s run function mg:{P}/boss/rage']
    for j, (an, per) in enumerate(abil):
        TICK += [f'scoreboard players remove $obt{i}_{j} mg.st 1',
                 f'execute if score $obt{i}_{j} mg.st matches ..0 as @e[tag={tag},limit=1] at @s run function mg:{P}/boss/{k}/{an}',
                 f'execute if score $obt{i}_{j} mg.st matches ..0 run scoreboard players set $obt{i}_{j} mg.st {per}']
    w(f'boss/{k}', TICK)
    w(f'boss/{k}_reset', [f'# {name} : plus personne, le combat est remis à zéro', f'scoreboard players set $ob{i} mg.st 0', f'bossbar set mg:olb{i} players',
                          f'execute as @e[tag={tag}] run kill @s', f'kill @e[tag=mg.olminion_{k}]', 'kill @e[tag=mg.oljar]'] +
      ([f'function mg:{P}/boss/colosse/pill_reset'] if k == 'colosse' else []))
    WIN = [f'# {name} est vaincu', f'scoreboard players set $ob{i} mg.st 0', f'scoreboard players set $obc{i} mg.st 300', f'bossbar set mg:olb{i} players',
           f'kill @e[tag=mg.olminion_{k}]', 'kill @e[tag=mg.oljar]',
           f'execute {at} as @a[tag=mg.olw,distance=..{r + 40}] run function mg:{P}/boss/{k}_rw',
           f'execute {at} run particle minecraft:totem_of_undying ~ ~2 ~ 3 2 3 0.5 200 force',
           f'execute {at} run playsound minecraft:ui.toast.challenge_complete master @a[distance=..80] ~ ~ ~ 1 0.8']
    w(f'boss/{k}_win', WIN)
    mo = M.MATS[M.REG_MAT[reg]][0]
    RW = [f'# @s a participé à la victoire sur {name}', 'title @s times 10 60 20', 'title @s title {"text":"VICTOIRE","color":"gold","bold":true}',
          f'title @s subtitle {js(TEXT(name + " est tombé", "yellow"))}', f'scoreboard players add @s mg.olg {200 * ri}', f'scoreboard players add @s {mo} 5',
          'scoreboard players add @s mg.olm9 1', f'function mg:{P}/xp {{n:{400 * ri}}}',
          f'tellraw @s {js(TEXT(f"  +{200 * ri} 💰, +5 {M.MATS[M.REG_MAT[reg]][1]}, +1 poussière de lune", "gold"))}'] + \
        bit_test('mg.olbk', i) + [f'execute if score $b mg.st matches 0 run function mg:{P}/boss/{k}_first',
                                  f'execute if score @s mg.olch matches {step} run function mg:{P}/q/adv']
    w(f'boss/{k}_rw', RW)
    w(f'boss/{k}_first', [f'scoreboard players operation @s mg.olbk += #p{i} mg.st', 'scoreboard players add @s mg.olsp 2',
                          'tellraw @a[tag=mg.olw] ' + js([TEXT('👑 ', 'gold'), {'selector': '@s', 'color': 'yellow'}, TEXT(' a vaincu ', 'gray'), TEXT(name, 'gold', bold=True),
                                                           TEXT(' ! (+2 points de caractéristique)', 'gray')])])
    SECOND += [f'scoreboard players remove $obc{i} mg.st 1',
               '# arène plus chargée (plus personne autour) : le combat s\'arrête sans victoire ; boss resté d\'un ancien combat : retiré',
               f'execute if score $ob{i} mg.st matches 1 {at} unless loaded ~ ~ ~ run scoreboard players set $ob{i} mg.st 0',
               f'execute unless score $ob{i} mg.st matches 1 as @e[tag={tag}] run kill @s',
               f'execute if score $ob{i} mg.st matches 1 unless entity @e[tag={tag}] run function mg:{P}/boss/{k}_win',
               f'execute unless score $ob{i} mg.st matches 1 if score $obc{i} mg.st matches ..0 {at} if entity @a[tag=mg.olw,gamemode=adventure,distance=..{r},scores={{mg.olch={step}..}}] run function mg:{P}/boss/{k}_start',
               f'execute if score $ob{i} mg.st matches 1 run function mg:{P}/boss/{k}']
w('boss/wake', ['# Fin de la cinématique d\'un boss : ils s\'animent', f'execute in {DIM} as @e[tag=mg.olboss] run data merge entity @s {{NoAI:0b}}'])
w('boss/rage', ['# Boss enragé (25 %)', 'tag @s add mg.olrage', 'effect give @s minecraft:speed infinite 0 true', 'effect give @s minecraft:strength infinite 0 true',
                'scoreboard players set @s mg.olat 16', 'tag @s add mg.olroar', 'playsound minecraft:entity.ender_dragon.growl hostile @a ~ ~ ~ 2 0.8',
                'tellraw @a[tag=mg.olw,distance=..60] [{"selector":"@s","color":"red","bold":true},{"text":" est enragé !","color":"red"}]'])


def minion(k, kind, n, spread=4):
    out = []
    for j in range(n):
        a = 2 * math.pi * j / max(1, n)
        out += [f'execute positioned ~{round(spread * math.cos(a), 1)} ~ ~{round(spread * math.sin(a), 1)} run function mg:{P}/m/{kind}',
                f'tag @e[tag=mg.ollast] add mg.olminion_{k}',
                'execute as @e[tag=mg.ollast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..40]']
    return out


def near(r):
    return f'@a[tag=mg.olw,gamemode=adventure,distance=..{r}]'


def aoe(r, d, src, extra=()):
    return [f'execute as {near(r)} run damage @s {d} minecraft:mob_attack by @e[tag={src},limit=1]'] + [f'effect give {near(r)} {e}' for e in extra]


def cone(rng, d, src, part, extra=()):
    """Souffle en cône vers le joueur le plus proche."""
    return [f'execute facing entity @p[tag=mg.olw,gamemode=adventure] eyes positioned ^ ^1 ^2 run particle {part} ^ ^ ^{rng / 2} 1 0.6 {rng / 3:.1f} 0.04 120 force',
            f'execute facing entity @p[tag=mg.olw,gamemode=adventure] eyes positioned ^ ^ ^{rng / 2} as {near(rng / 2 + 1)} run damage @s {d} minecraft:mob_attack by @e[tag={src},limit=1]'] + \
        [f'execute facing entity @p[tag=mg.olw,gamemode=adventure] eyes positioned ^ ^ ^{rng / 2} run effect give {near(rng / 2 + 1)} {e}' for e in extra]


# ---------------------------------------------------------------- attaques
B = {}
B['brennic'] = {
    'whirl': ['particle minecraft:sweep_attack ~ ~1 ~ 2.5 0.4 2.5 0 20', 'playsound minecraft:entity.player.attack.sweep hostile @a ~ ~ ~ 2 0.5', 'scoreboard players set @s mg.olat 10'] +
             aoe(4.5, 8, 'mg.olb_brennic'),
    'call': ['execute if score $hp mg.st matches 230.. run return 0', 'tellraw @a[distance=..40] {"text":"Brennic : « À moi, les gars ! »","color":"red"}'] +
            minion('brennic', 'bandit', 1) + minion('brennic', 'archer', 1, 6),
    'charge': ['effect give @s minecraft:speed 3 3 true', 'playsound minecraft:entity.vindicator.celebrate hostile @a ~ ~ ~ 2 0.7',
               'execute facing entity @a[tag=mg.olw,gamemode=adventure,sort=furthest,distance=..30,limit=1] feet rotated ~ -10 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:ombre/vec {d:1.6}',
               'function mg:ombre/push'],
}
B['ystar'] = {
    'web': ['playsound minecraft:entity.spider.ambient hostile @a ~ ~ ~ 2 0.5', f'execute as {near(18)} at @s run function mg:ombre/m/web_at'],
    'brood': ['playsound minecraft:entity.spider.hurt hostile @a ~ ~ ~ 2 0.5'] + minion('ystar', 'arachneen', 3),
    'venom': ['particle minecraft:item_slime ~ ~1 ~ 2 0.5 2 0 40', 'effect give ' + near(5) + ' minecraft:poison 4 1', 'scoreboard players set @s mg.olat 8'],
    'leap': ['execute facing entity @p[tag=mg.olw,gamemode=adventure] feet rotated ~ -25 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:ombre/vec {d:1.4}',
             'function mg:ombre/push', 'playsound minecraft:entity.spider.step hostile @a ~ ~ ~ 2 0.5'],
}
B['hrimgar'] = {
    'slam': ['particle minecraft:explosion ~ ~0.5 ~ 3 0.2 3 0 12', 'particle minecraft:block{block_state:"minecraft:packed_ice"} ~ ~0.3 ~ 4 0.2 4 0 120',
             'playsound minecraft:entity.generic.explode hostile @a ~ ~ ~ 1.5 0.5', 'scoreboard players set @s mg.olat 10'] + aoe(6, 12, 'mg.olb_hrimgar', ['minecraft:levitation 1 2 true']),
    'breath': ['playsound minecraft:entity.breeze.wind_burst hostile @a ~ ~ ~ 2 0.5'] + cone(10, 8, 'mg.olb_hrimgar', 'minecraft:snowflake', ['minecraft:slowness 4 2']),
    'spikes': [f'execute as {near(18)} at @s run summon minecraft:marker ~ ~ ~ {{Tags:["mg.ol","mg.olspike"]}}', 'scoreboard players set @e[tag=mg.olspike] mg.olst 2',
               'playsound minecraft:block.glass.break hostile @a ~ ~ ~ 1.5 0.5'],
    'wolves': minion('hrimgar', 'loupneige', 2, 5),
}
B['morvaine'] = {
    'blink': ['particle minecraft:witch ~ ~1 ~ 0.5 1 0.5 0 40', 'execute store result score $r mg.st run random value 0..3'] +
             [f'execute if score $r mg.st matches {j} run tp @s ~{round(8 * math.cos(math.pi / 2 * j))} ~ ~{round(8 * math.sin(math.pi / 2 * j))}' for j in range(4)] +
             ['execute at @s run particle minecraft:witch ~ ~1 ~ 0.5 1 0.5 0 40', 'playsound minecraft:entity.enderman.teleport hostile @a ~ ~ ~ 1.5 0.6'],
    'swarm': ['tellraw @a[distance=..40] {"text":"Morvaine : « Levez-vous, mes noyés ! »","color":"dark_purple"}'] + minion('morvaine', 'noye', 2) + minion('morvaine', 'embourbe', 1, 6),
    'hex': ['execute as @a[tag=mg.olw,gamemode=adventure,distance=..20,sort=random,limit=1] run function mg:ombre/boss/hex'],
    'cloud': ['execute as @a[tag=mg.olw,gamemode=adventure,distance=..20,sort=random,limit=1] at @s run summon minecraft:area_effect_cloud ~ ~ ~ {Tags:["mg.ol"],Radius:3f,Duration:120,'
              'potion_contents:{potion:"minecraft:strong_poison"},custom_particle:{type:"minecraft:entity_effect",color:[0.3,0.8,0.2,1.0]}}'],
}
w('boss/hex', ['effect give @s minecraft:levitation 2 1', 'effect give @s minecraft:darkness 4 0 true', 'title @s actionbar {"text":"🕸 Malédiction de Morvaine !","color":"dark_purple"}',
               'scoreboard players set @s mg.olal 30', 'execute at @s run playsound minecraft:entity.witch.celebrate hostile @s ~ ~ ~ 1 0.6'])
sx, sy, sz = A['sethkar']['c']
JARS = [(sx - 7, sy, sz - 7), (sx + 7, sy, sz - 7), (sx, sy, sz + 7)]
B['sethkar'] = {
    'storm': ['playsound minecraft:entity.breeze.idle_air hostile @a ~ ~ ~ 2 0.4', 'particle minecraft:falling_dust{block_state:"minecraft:sand"} ~ ~4 ~ 8 3 8 0 400 force'] +
             aoe(14, 5, 'mg.olb_sethkar', ['minecraft:blindness 3 0 true']),
    'mummies': minion('sethkar', 'momie', 2, 5),
    'beam': ['execute as @a[tag=mg.olw,gamemode=adventure,distance=..20,sort=random,limit=1] at @s run function mg:ombre/boss/curse'],
    'jars': ['execute if score $hp mg.st matches 513.. run return 0', 'execute if score $obp' + str(BIDX['sethkar']) + ' mg.st matches 1.. run return run function mg:ombre/boss/sethkar/jarchk',
             'scoreboard players set $obp' + str(BIDX['sethkar']) + ' mg.st 1', 'data merge entity @s {Invulnerable:1b}',
             'tellraw @a[distance=..40] {"text":"Sethkar se réfugie dans sa magie : brise les trois vases canopes (clic droit) !","color":"gold","bold":true}'] +
            [f'summon minecraft:interaction {x + 0.5} {y} {z + 0.5} {{Tags:["mg.ol","mg.oljar"],width:1.2f,height:1.6f,response:1b}}' for x, y, z in JARS] +
            [f'summon minecraft:item_display {x + 0.5} {y + 0.6} {z + 0.5} {{Tags:["mg.ol","mg.oljar","mg.oljard"],item:{{id:"minecraft:decorated_pot",count:1}},Glowing:1b,'
             'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}' for x, y, z in JARS],
}
w('boss/sethkar/jarchk', ['# Plus de vases : Sethkar redevient vulnérable', 'execute if entity @e[type=minecraft:interaction,tag=mg.oljar] run return run particle minecraft:enchant ~ ~2 ~ 1 1 1 0.5 20',
                          'execute if entity @s[nbt={Invulnerable:1b}] run tellraw @a[distance=..40] {"text":"La protection de Sethkar se brise !","color":"gold"}',
                          'data merge entity @s {Invulnerable:0b}'])
w('boss/jar_int', ['# @s (vase canope) : brisé', 'execute on target if entity @s[tag=mg.olw] at @s run playsound minecraft:block.decorated_pot.shatter master @a ~ ~ ~ 1 1',
                   'execute at @s run particle minecraft:block{block_state:"minecraft:terracotta"} ~ ~1 ~ 0.4 0.4 0.4 0 30',
                   'execute at @s run kill @e[tag=mg.oljard,distance=..1.5]', 'kill @s'])
w('boss/curse', ['particle minecraft:dust{color:[1.0,0.8,0.1],scale:2} ~ ~1 ~ 0.3 1 0.3 0 30 force', 'particle minecraft:end_rod ~ ~6 ~ 0.1 4 0.1 0 40 force',
                 'damage @s 12 minecraft:magic', 'effect give @s minecraft:hunger 4 2 true', 'playsound minecraft:entity.evoker.prepare_attack hostile @a ~ ~ ~ 1 0.6'])
B['ignarok'] = {
    'breath': ['scoreboard players set @s mg.olat 14', 'playsound minecraft:entity.blaze.shoot hostile @a ~ ~ ~ 2 0.4', 'playsound minecraft:item.firecharge.use hostile @a ~ ~ ~ 2 0.6',
               'execute facing entity @p[tag=mg.olw,gamemode=adventure] eyes positioned ^ ^3 ^4 run particle minecraft:flame ^ ^ ^3 1 0.6 2 0.06 200 force',
               'execute facing entity @p[tag=mg.olw,gamemode=adventure] eyes positioned ^ ^ ^6 as ' + near(5) + ' run function mg:ombre/boss/fire'],
    'gust': ['particle minecraft:gust_emitter_large ~ ~2 ~ 1 1 1 0 3 force', 'playsound minecraft:entity.ender_dragon.flap hostile @a ~ ~ ~ 2 0.7',
             f'execute as {near(9)} at @s facing entity @e[tag=mg.olb_ignarok,limit=1] feet rotated ~180 -20 run function mg:ombre/boss/knock'],
    'flight': ['effect give @s minecraft:levitation 3 3 true', 'playsound minecraft:entity.ender_dragon.growl hostile @a ~ ~ ~ 3 0.8', 'tag @s add mg.olroar', 'scoreboard players set @s mg.olat 30',
               f'execute as {near(26)} at @s run summon minecraft:marker ~ ~ ~ {{Tags:["mg.ol","mg.olfall"]}}', 'scoreboard players set @e[tag=mg.olfall] mg.olst 3'],
    'tail': ['scoreboard players set @s mg.olat 8', 'particle minecraft:sweep_attack ~ ~1 ~ 3 0.4 3 0 20', 'playsound minecraft:entity.player.attack.sweep hostile @a ~ ~ ~ 2 0.4'] +
            aoe(6, 9, 'mg.olb_ignarok'),
}
w('boss/fire', ['execute if score @s mg.olfire matches 1.. run damage @s 5 minecraft:in_fire', 'execute unless score @s mg.olfire matches 1.. run damage @s 12 minecraft:in_fire',
                'execute unless score @s mg.olfire matches 1.. run effect give @s minecraft:wither 3 0'])
w('boss/knock', ['# @s (joueur) : projeté loin (dans la direction du contexte)', 'effect give @s minecraft:levitation 1 6 true', 'damage @s 4 minecraft:fly_into_wall',
                 'tp @s ^ ^ ^3'])
cpx = A['colosse']['c']
B['colosse'] = {
    'quake': ['particle minecraft:explosion ~ ~0.5 ~ 4 0.3 4 0 16 force', 'particle minecraft:block{block_state:"minecraft:deepslate_tiles"} ~ ~0.3 ~ 6 0.2 6 0 200 force',
              'playsound minecraft:entity.iron_golem.damage hostile @a ~ ~ ~ 2 0.4', 'playsound minecraft:entity.generic.explode hostile @a ~ ~ ~ 1.5 0.5'] +
             aoe(8, 14, 'mg.olb_colosse', ['minecraft:levitation 1 3 true']),
    'beam': ['execute as @a[tag=mg.olw,gamemode=adventure,distance=..24,sort=random,limit=1] at @s run function mg:ombre/boss/rune_beam'],
    'rocks': minion('colosse', 'troggo', 2, 6),
    'shield': ['execute if entity @e[tag=mg.olpill,scores={mg.olst=..0}] run return run data merge entity @s {Invulnerable:1b,Glowing:1b}',
               'execute if entity @s[nbt={Invulnerable:1b}] run tellraw @a[distance=..40] {"text":"Les quatre piliers sont éteints : le Colosse est vulnérable !","color":"aqua","bold":true}',
               'data merge entity @s {Invulnerable:0b,Glowing:0b}'],
}
w('boss/rune_beam', ['particle minecraft:dust{color:[0.3,0.6,1.0],scale:2} ~ ~1 ~ 0.3 1 0.3 0 40 force', 'particle minecraft:electric_spark ~ ~1 ~ 0.4 1 0.4 0.3 40 force',
                     'damage @s 10 minecraft:magic', 'playsound minecraft:block.beacon.deactivate hostile @a ~ ~ ~ 1.5 1.4'])
PILL = S.SPOTS['colosse_pillars']
PSET = ['# Piliers runiques du Colosse : rallumés (le bouclier tient tant que brille un pilier)']
PSUM = []                                    # piliers posés une fois dans le monde (entités permanentes)
for (x, y, z) in PILL:
    PSUM += [f'summon minecraft:interaction {x} {y} {z} {{Tags:["mg.ol","mg.olpill"],width:1.4f,height:5.2f,response:1b}}',
             f'setblock {int(x)} {y + 4} {int(z)} minecraft:light_blue_stained_glass']
    PSET.append(f'setblock {int(x)} {y + 4} {int(z)} minecraft:light_blue_stained_glass')
PSET.append('scoreboard players set @e[tag=mg.olpill] mg.olst 0')
w('boss/colosse/pill_reset', PSET)
w('boss/pill_int', ['# @s (pilier) : éteint 30 s par un clic', 'execute if score @s mg.olst matches 1.. run return run data remove entity @s interaction',
                    'scoreboard players set @s mg.olst 30', 'execute at @s run setblock ~ ~4 ~ minecraft:black_stained_glass',
                    'execute at @s run playsound minecraft:block.beacon.deactivate master @a ~ ~ ~ 1 1', 'execute at @s run particle minecraft:electric_spark ~ ~4 ~ 0.4 0.4 0.4 0.2 30',
                    'data remove entity @s interaction'])
w('boss/pill_sec', ['# Piliers : rallumés au bout de 30 s', 'scoreboard players remove @e[tag=mg.olpill,scores={mg.olst=1..}] mg.olst 1',
                    'execute as @e[tag=mg.olpill,scores={mg.olst=0}] at @s if block ~ ~4 ~ minecraft:black_stained_glass run setblock ~ ~4 ~ minecraft:light_blue_stained_glass'])
B['malveth'] = {
    'bolt': ['execute as @a[tag=mg.olw,gamemode=adventure,distance=..24,sort=random,limit=1] at @s run function mg:ombre/boss/shadow'],
    'blink': ['particle minecraft:reverse_portal ~ ~1 ~ 0.5 1 0.5 0.1 60', 'execute store result score $r mg.st run random value 0..3'] +
             [f'execute if score $r mg.st matches {j} run tp @s {A["malveth"]["c"][0] + round(9 * math.cos(math.pi / 2 * j + 0.6))} {A["malveth"]["c"][1]} {A["malveth"]["c"][2] + round(9 * math.sin(math.pi / 2 * j + 0.6))}'
              for j in range(4)] + ['playsound minecraft:entity.enderman.teleport hostile @a ~ ~ ~ 1.5 0.5'],
    'guards': ['execute if entity @s[tag=mg.olshd] unless entity @e[tag=mg.olminion_malveth] run function mg:ombre/boss/malveth/unshield',
               'execute if score $hp mg.st matches ..683 unless entity @s[tag=mg.olg1] run function mg:ombre/boss/malveth/shield',
               'execute if score $hp mg.st matches ..341 unless entity @s[tag=mg.olg2] run function mg:ombre/boss/malveth/shield'],
    'dark': ['effect give ' + near(30) + ' minecraft:darkness 5 0 true', 'playsound minecraft:ambient.soul_sand_valley.mood hostile @a ~ ~ ~ 2 0.6'],
}
w('boss/malveth/shield', ['execute if entity @s[tag=mg.olg1] run tag @s add mg.olg2', 'tag @s add mg.olg1', 'tag @s add mg.olshd', 'data merge entity @s {Invulnerable:1b,Glowing:1b}',
                          'tellraw @a[distance=..40] {"text":"Malveth : « Mes gardes, protégez-moi ! » (tue ses gardes pour briser son bouclier)","color":"dark_purple","bold":true}'] +
  minion('malveth', 'ossement', 4, 5))
w('boss/malveth/unshield', ['tag @s remove mg.olshd', 'data merge entity @s {Invulnerable:0b,Glowing:0b}',
                            'tellraw @a[distance=..40] {"text":"Le bouclier de Malveth vole en éclats !","color":"light_purple"}'])
w('boss/shadow', ['particle minecraft:dust{color:[0.4,0.1,0.6],scale:2} ~ ~1 ~ 0.3 1 0.3 0 40 force', 'particle minecraft:soul ~ ~1 ~ 0.4 1 0.4 0.05 20 force',
                  'execute unless score @s mg.olbless matches 1.. run damage @s 18 minecraft:magic', 'execute if score @s mg.olbless matches 1.. run damage @s 12 minecraft:magic',
                  'effect give @s minecraft:wither 3 1', 'playsound minecraft:entity.wither.shoot hostile @a ~ ~ ~ 1 0.8'])
B['nyxar'] = {
    'breath': ['scoreboard players set @s mg.olat 14', 'playsound minecraft:entity.ender_dragon.shoot hostile @a ~ ~ ~ 2 0.5'] +
              cone(12, 14, 'mg.olb_nyxar', 'minecraft:dragon_breath', ['minecraft:wither 3 1']),
    'dive': ['effect give @s minecraft:levitation 2 4 true', 'tag @s add mg.olroar', 'scoreboard players set @s mg.olat 20', 'playsound minecraft:entity.ender_dragon.growl hostile @a ~ ~ ~ 3 0.5',
             f'execute as @a[tag=mg.olw,gamemode=adventure,distance=..24,sort=random,limit=1] at @s run summon minecraft:marker ~ ~ ~ {{Tags:["mg.ol","mg.oldive"]}}',
             'scoreboard players set @e[tag=mg.oldive] mg.olst 3'],
    'spectres': minion('nyxar', 'spectre', 2, 6),
    'roar': ['scoreboard players set @s mg.olat 20', 'tag @s add mg.olroar', 'playsound minecraft:entity.ender_dragon.growl hostile @a ~ ~ ~ 3 0.4',
             'effect give ' + near(18) + ' minecraft:darkness 4 0 true', 'effect give ' + near(18) + ' minecraft:slowness 3 1'],
}
for k, ab in B.items():
    for an, L in ab.items():
        w(f'boss/{k}/{an}', [f'# {BOSSES[k][0]} : {an}'] + L)
# marqueurs différés (pics de glace, chutes de feu, piqué)
w('boss/fx_sec', ['# Chaque seconde : pics de glace, pluies de feu, piqué de Nyxar, piliers',
                  'scoreboard players remove @e[type=minecraft:marker,tag=mg.olspike] mg.olst 1', 'scoreboard players remove @e[type=minecraft:marker,tag=mg.olfall] mg.olst 1',
                  'scoreboard players remove @e[type=minecraft:marker,tag=mg.oldive] mg.olst 1',
                  'execute as @e[type=minecraft:marker,tag=mg.olspike] at @s run particle minecraft:snowflake ~ ~0.2 ~ 0.6 0.1 0.6 0 12',
                  'execute as @e[type=minecraft:marker,tag=mg.olfall] at @s run particle minecraft:flame ~ ~6 ~ 0.6 2 0.6 0.02 20 force',
                  'execute as @e[type=minecraft:marker,tag=mg.olspike,scores={mg.olst=..0}] at @s run function mg:ombre/boss/spike_hit',
                  'execute as @e[type=minecraft:marker,tag=mg.olfall,scores={mg.olst=..0}] at @s run function mg:ombre/boss/fall_hit',
                  'execute as @e[type=minecraft:marker,tag=mg.oldive,scores={mg.olst=..0}] at @s run function mg:ombre/boss/dive_hit',
                  f'function mg:{P}/boss/pill_sec', 'tag @a remove mg.olboss_in'])
w('boss/spike_hit', ['particle minecraft:block{block_state:"minecraft:blue_ice"} ~ ~1 ~ 0.4 1 0.4 0 40 force', 'playsound minecraft:block.glass.break hostile @a ~ ~ ~ 1 0.6',
                     'execute as @a[tag=mg.olw,gamemode=adventure,distance=..2] run damage @s 10 minecraft:freeze',
                     'effect give @a[tag=mg.olw,gamemode=adventure,distance=..2] minecraft:levitation 1 5 true', 'kill @s'])
w('boss/fall_hit', ['particle minecraft:explosion ~ ~1 ~ 0.5 0.5 0.5 0 3 force', 'particle minecraft:lava ~ ~1 ~ 1 1 1 0 20 force', 'playsound minecraft:entity.generic.explode hostile @a ~ ~ ~ 1 0.8',
                    'execute as @a[tag=mg.olw,gamemode=adventure,distance=..2.5] run function mg:ombre/boss/fire', 'kill @s'])
w('boss/dive_hit', ['tp @e[tag=mg.olb_nyxar] ~ ~ ~', 'particle minecraft:explosion_emitter ~ ~1 ~ 0 0 0 0 1 force', 'playsound minecraft:entity.generic.explode hostile @a ~ ~ ~ 2 0.5',
                    'execute as @a[tag=mg.olw,gamemode=adventure,distance=..6] run damage @s 16 minecraft:mob_attack by @e[tag=mg.olb_nyxar,limit=1]', 'kill @s'])

# ================================================================ donjons
for di, (key, D) in enumerate(S.DUNGEONS.items()):
    reg = D['region']
    ri = W.ORDER.index(reg) + 1
    rooms = D['rooms']
    vertical_door = D['dir'] in ('north', 'south')
    xs = [r_['c'][0] for r_ in rooms]
    zs = [r_['c'][2] for r_ in rooms]
    pad = max(r_['half'] for r_ in rooms) + 2
    bx0, bz0 = math.floor(min(xs) - pad), math.floor(min(zs) - pad)
    bx1, bz1 = math.ceil(max(xs) + pad), math.ceil(max(zs) + pad)
    y = D['y']
    BOX = f'x={bx0},y={y - 1},z={bz0},dx={bx1 - bx0},dy=14,dz={bz1 - bz0}'
    D['box'] = BOX
    alpha = {'crypt': 'a_crypte', 'nest': 'a_tisseuse', 'ice': 'a_wendigo', 'sunken': 'a_noye', 'tomb': 'a_momie', 'forge': 'a_forgeron',
             'mine': 'a_contremaitre', 'souls': 'a_ames'}[key]
    ahp = min(M.K[alpha]['hp'], 1024)
    doors = []
    for r_ in rooms[:-1]:
        dx_, dy_, dz_ = r_['door']
        if vertical_door:
            doors.append((dx_ - 1, dy_, dz_, dx_ + 1, dy_ + 2, dz_))
        else:
            doors.append((dx_, dy_, dz_ - 1, dx_, dy_ + 2, dz_ + 1))
    door_blk = S.DUN_THEMES[D['theme']]['door']
    if door_blk == 'cobweb':
        door_blk = 'iron_bars'
    w(f'dg/{key}/close', [f'# {D["name"]} : portes fermées'] + [f'fill {a} {b} {c} {d} {e} {f} minecraft:{door_blk}' for (a, b, c, d, e, f) in doors])
    for n, (a, b, c, d, e, f) in enumerate(doors):
        w(f'dg/{key}/open{n}', [f'fill {a} {b} {c} {d} {e} {f} minecraft:air', f'playsound minecraft:block.iron_door.open master @a {a} {b} {c} 1 0.6',
                                f'tellraw @a[{BOX}] {{"text":"🚪 La porte s\'ouvre…","color":"gray"}}'])
    L = [f'# {D["name"]} ({reg}) : chaque seconde', f'execute unless entity @a[tag=mg.olw,{BOX}] run scoreboard players add $odw{di} mg.st 1',
         f'execute if entity @a[tag=mg.olw,{BOX}] run scoreboard players set $odw{di} mg.st 0',
         f'execute if score $odw{di} mg.st matches 40.. unless score $od{di} mg.st matches 0 run return run function mg:{P}/dg/{key}/reset',
         f'execute store result score $n mg.st if entity @e[tag=mg.oldg{di}]']
    for n, r_ in enumerate(rooms):
        cx, cy, cz = r_['c']
        h = r_['half']
        rbox = f'x={math.floor(cx - h)},y={cy},z={math.floor(cz - h)},dx={2 * h},dy={r_["h"]},dz={2 * h}'
        if n < 3:
            L.append(f'execute if score $od{di} mg.st matches {n * 2} if entity @a[tag=mg.olw,{rbox}] positioned {cx} {cy} {cz} run function mg:{P}/dg/{key}/wave{n}')
            L.append(f'execute if score $od{di} mg.st matches {n * 2 + 1} positioned {cx} {cy} {cz} if loaded ~ ~ ~ unless entity @e[tag=mg.oldg{di}] run function mg:{P}/dg/{key}/clear{n}')
            w(f'dg/{key}/wave{n}', [f'# {D["name"]} : vague de la salle {n + 1}', f'scoreboard players set $od{di} mg.st {n * 2 + 1}'] +
              ([f'function mg:{P}/dg/{key}/close'] if n == 0 else []) + [
                                    f'execute store result score $g mg.st if entity @a[tag=mg.olw,{BOX}]', 'scoreboard players operation $g mg.st *= #2 mg.st',
                                    f'scoreboard players add $g mg.st {3 + n}', 'execute if score $g mg.st matches 10.. run scoreboard players set $g mg.st 9',
                                    f'function mg:{P}/dg/spawn_{reg}', f'tag @e[tag=mg.oldgn] add mg.oldg{di}', 'tag @e[tag=mg.oldgn] add mg.oldg',
                                    'execute as @e[tag=mg.oldgn,tag=mg.olprov] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,distance=..30]',
                                    'tag @e[tag=mg.oldgn] remove mg.oldgn',
                                    f'title @a[{BOX}] actionbar {js(TEXT("⚔ " + D["name"] + f" : salle {n + 1} / 4", "red", bold=True))}',
                                    f'playsound minecraft:event.raid.horn hostile @a[{BOX}] {cx} {cy} {cz} 0.6 1.4'])
            w(f'dg/{key}/clear{n}', [f'scoreboard players set $od{di} mg.st {n * 2 + 2}', f'function mg:{P}/dg/{key}/open{n}'] +
              ([f'execute as @a[tag=mg.olw,{BOX}] run function mg:{P}/xp {{n:{40 * ri}}}'] if True else []))
        else:
            L.append(f'execute if score $od{di} mg.st matches 6 if entity @a[tag=mg.olw,{rbox}] positioned {cx} {cy} {cz} run function mg:{P}/dg/{key}/alpha')
            w(f'dg/{key}/alpha', [f'# {D["name"]} : l\'alpha se réveille', f'scoreboard players set $od{di} mg.st 7', f'function mg:{P}/m/{alpha}',
                                  f'tag @e[tag=mg.ollast] add mg.oldg{di}', 'tag @e[tag=mg.ollast] add mg.oldg', 'tag @e[tag=mg.ollast] add mg.oldga',
                                  'execute as @e[tag=mg.ollast] run data merge entity @s {CustomNameVisible:1b,Glowing:1b}',
                                  f'bossbar set mg:oldg{di} max {ahp}', f'bossbar set mg:oldg{di} players @a[{BOX}]',
                                  f'title @a[{BOX}] title {js(TEXT("ALPHA", "dark_red", bold=True))}', f'title @a[{BOX}] subtitle {js(TEXT(D["alpha"], "gray"))}',
                                  f'playsound minecraft:entity.ravager.roar hostile @a[{BOX}] {cx} {cy} {cz} 1 0.7'])
    L += [f'execute if score $od{di} mg.st matches 7 run bossbar set mg:oldg{di} players @a[{BOX}]',
          f'execute if score $od{di} mg.st matches 7 store result bossbar mg:oldg{di} value run data get entity @e[tag=mg.oldga,tag=mg.oldg{di},limit=1] Health',
          f'execute if score $od{di} mg.st matches 7 positioned {rooms[-1]["c"][0]} {rooms[-1]["c"][1]} {rooms[-1]["c"][2]} if loaded ~ ~ ~ unless entity @e[tag=mg.oldga,tag=mg.oldg{di}] run function mg:{P}/dg/{key}/win']
    w(f'dg/{key}/tick', L)
    tx, ty, tz = D['chest']
    w(f'dg/{key}/win', [f'# {D["name"]} : terminé', f'scoreboard players set $od{di} mg.st 8', f'bossbar set mg:oldg{di} players',
                        f'particle minecraft:totem_of_undying {tx} {ty + 1} {tz} 1 1 1 0.3 80 force',
                        f'execute as @a[tag=mg.olw,{BOX}] run function mg:{P}/dg/{key}/rw'])
    mo = M.MATS[M.REG_MAT[reg]][0]
    w(f'dg/{key}/rw', [f'# @s termine {D["name"]}', f'scoreboard players add @s mg.olg {150 * ri}', f'scoreboard players add @s {mo} 4', f'function mg:{P}/xp {{n:{300 * ri}}}',
                       'execute store result score $r mg.st run random value 1..2', 'execute if score $r mg.st matches 1 run scoreboard players add @s mg.olsp 1',
                       'title @s times 10 50 15', 'title @s title {"text":"DONJON TERMINÉ","color":"gold","bold":true}', f'title @s subtitle {js(TEXT(D["name"], "yellow"))}',
                       f'tellraw @s {js(TEXT(f"  +{150 * ri} 💰, +4 matériaux (et peut-être une gemme)", "gold"))}'] + bit_test('mg.oldg', di) +
      [f'execute if score $b mg.st matches 0 run function mg:{P}/dg/{key}/first'])
    w(f'dg/{key}/first', [f'scoreboard players operation @s mg.oldg += #p{di} mg.st', f'function mg:{P}/xp {{n:{500 * ri}}}',
                          'tellraw @a[tag=mg.olw] ' + js([TEXT('🏆 ', 'gold'), {'selector': '@s', 'color': 'yellow'}, TEXT(' a terminé le donjon « ' + D['name'] + ' » !', 'gold')])])
    w(f'dg/{key}/reset', [f'# {D["name"]} : remis à zéro (plus personne)', f'scoreboard players set $od{di} mg.st 0', f'scoreboard players set $odw{di} mg.st 0',
                          f'execute as @e[tag=mg.oldg{di}] run kill @s', f'bossbar set mg:oldg{di} players', f'execute in {DIM} run function mg:{P}/dg/{key}/close'])
    SECOND.append(f'function mg:{P}/dg/{key}/tick')
    SETUP += [f'bossbar add mg:oldg{di} {js(TEXT("☠ Alpha : " + D["alpha"], "dark_red"))}', f'bossbar set mg:oldg{di} color red', f'bossbar set mg:oldg{di} style notched_10',
              f'bossbar set mg:oldg{di} players', f'scoreboard players set $od{di} mg.st 0', f'scoreboard players set $odw{di} mg.st 0']
    CLEAR += [f'bossbar remove mg:oldg{di}']
# vague : une espèce tirée au sort de la région ×$g
for r in W.ORDER:
    ks = M.REG_KINDS[r]
    w(f'dg/spawn_{r}', [f'# Vague de donjon ({r}) : $g monstres', 'execute store result score $r mg.st run random value 0..' + str(len(ks) - 1)] +
      [f'execute if score $r mg.st matches {j} run function mg:{P}/m/{k}' for j, k in enumerate(ks)] +
      ['tag @e[tag=mg.ollast] add mg.oldgn', 'scoreboard players remove $g mg.st 1',
       f'execute if score $g mg.st matches 1.. positioned ~1 ~ ~0.5 run function mg:{P}/dg/spawn_{r}'])
SECOND.append(f'function mg:{P}/boss/fx_sec')
w('bosses', SECOND)
w('boss/setup', SETUP)
w('boss/clear', CLEAR)
