"""👹 Ombrelune : monstres (bestiaire), apparitions par région, élites, capacités, récompenses des victoires.

Chaque espèce = un mob vanilla nommé, équipé, aux attributs de sa région, marqué mg.olk_<clé>. Une victoire est détectée par
un progrès « player_killed_entity » (prédicat sur le tag), dont la récompense (fonction mg:ombre/k/<clé>) donne XP, or,
matériaux, entrée du bestiaire, et fait avancer quêtes et contrats (mg:ombre/khook, $kk = n° de l'espèce).
"""
import math
import random

import ol_world as W
import ol_structs as S
from ol_core import w, js, P, TEXT, wjson, bit_test

# matériaux : n° -> (score, nom, couleur)
MATS = {1: ('mg.olm1', 'peau de bête', 'gold'), 2: ('mg.olm2', 'soie d\'araignée', 'white'), 3: ('mg.olm3', 'éclat de givre', 'aqua'),
        4: ('mg.olm4', 'fiole de venin', 'dark_green'), 5: ('mg.olm5', 'ambre solaire', 'yellow'), 6: ('mg.olm6', 'écaille de drake', 'red'),
        7: ('mg.olm7', 'minerai de runite', 'blue'), 8: ('mg.olm8', 'essence d\'ombre', 'dark_purple'), 9: ('mg.olm9', 'poussière de lune', 'light_purple')}
REG_MAT = {'w': 1, 'nw': 2, 'n': 3, 'ne': 4, 'e': 5, 'se': 6, 's': 7, 'sw': 8}


def leather(col, *slots):
    return {s: f'{{id:"minecraft:leather_{p}",count:1,components:{{"minecraft:dyed_color":{col}}}}}' for s, p in slots}


def it(i, extra=''):
    return f'{{id:"minecraft:{i}",count:1{extra}}}'


# clé : (mob, nom, couleur, région, PV, dégâts, vitesse, échelle, xp, or, chance matériau %, options)
# options : prov (neutre à provoquer), und (mort-vivant), eq (équipement), nbt (en plus), onhit (effet sur le joueur touché)
K = {}


def kind(key, mob, name, col, reg, hp, dmg, spd, scale, xp, gold, mat, **o):
    K[key] = dict(mob=mob, name=name, col=col, reg=reg, hp=hp, dmg=dmg, spd=spd, scale=scale, xp=xp, gold=gold, mat=mat, **o)


# ---- Valdor
kind('loup', 'wolf', 'Loup gris', 'gray', 'w', 16, 3, 0.34, 1.0, 10, 3, 30, prov=True)
kind('bandit', 'vindicator', 'Brigand', 'red', 'w', 22, 4, 0.33, 1.0, 14, 6, 15, eq={'mainhand': it('iron_axe'), **leather(6704179, ('head', 'helmet'), ('chest', 'chestplate'))})
kind('archer', 'pillager', 'Archer brigand', 'red', 'w', 18, 3, 0.33, 1.0, 14, 6, 15, eq={'mainhand': it('crossbow'), **leather(4473924, ('head', 'helmet'))})
kind('goule', 'zombie', 'Goule', 'dark_green', 'w', 24, 3, 0.25, 1.0, 12, 4, 10, und=True, nbt='CanBreakDoors:0b,')
kind('squelette', 'skeleton', 'Squelette', 'white', 'w', 18, 2, 0.26, 1.0, 12, 4, 10, und=True, eq={'mainhand': it('bow')})
# ---- Sylvanor
kind('araignee', 'spider', 'Araignée sylvestre', 'dark_green', 'nw', 34, 5, 0.32, 1.25, 20, 7, 35, prov=True, onhit='poison 3 0')
kind('tisseuse', 'cave_spider', 'Tisseuse', 'dark_aqua', 'nw', 22, 4, 0.33, 1.4, 18, 6, 35, prov=True)
kind('follet', 'vex', 'Feu follet', 'aqua', 'nw', 16, 4, 0.3, 1.0, 16, 5, 20, nbt='life_ticks:2400,')
kind('elfe', 'illusioner', 'Elfe noir', 'dark_purple', 'nw', 38, 5, 0.33, 1.0, 26, 10, 25, eq={'mainhand': it('bow')})
kind('garou', 'wolf', 'Loup-garou', 'dark_gray', 'nw', 60, 8, 0.36, 1.6, 34, 12, 30, prov=True, nbt='variant:"minecraft:black",')
# ---- Givrecroc
kind('vagabond', 'stray', 'Vagabond gelé', 'aqua', 'n', 40, 6, 0.27, 1.0, 30, 10, 25, und=True, eq={'mainhand': it('bow')})
kind('ours', 'polar_bear', 'Ours des glaces', 'white', 'n', 70, 10, 0.3, 1.3, 40, 12, 40, prov=True)
kind('loupneige', 'wolf', 'Loup des neiges', 'white', 'n', 40, 7, 0.36, 1.15, 30, 10, 35, prov=True, nbt='variant:"minecraft:snowy",')
kind('yeti', 'zombie', 'Yéti', 'white', 'n', 95, 11, 0.27, 1.7, 55, 18, 40, nbt='CanBreakDoors:0b,', onhit='slowness 3 1',
     eq=leather(15790320, ('head', 'helmet'), ('chest', 'chestplate'), ('legs', 'leggings'), ('feet', 'boots')))
# ---- Fangebrume
kind('sorciere', 'witch', 'Sorcière des marais', 'dark_purple', 'ne', 60, 6, 0.27, 1.0, 45, 16, 35)
kind('noye', 'drowned', 'Noyé', 'dark_aqua', 'ne', 58, 10, 0.27, 1.05, 42, 14, 30, und=True, eq={'mainhand': it('trident')})
kind('embourbe', 'bogged', 'Embourbé', 'dark_green', 'ne', 50, 8, 0.27, 1.0, 42, 14, 30, und=True, eq={'mainhand': it('bow')})
kind('vase', 'slime', 'Vase putride', 'green', 'ne', 40, 7, 0.4, 1.0, 36, 10, 40, nbt='Size:2,')
kind('sangsue', 'silverfish', 'Sangsue géante', 'dark_red', 'ne', 34, 7, 0.33, 1.8, 36, 10, 40, onhit='poison 3 0')
# ---- Azhar
kind('momie', 'husk', 'Momie', 'gold', 'e', 80, 12, 0.26, 1.1, 60, 20, 30, und=True, nbt='CanBreakDoors:0b,')
kind('scorpion', 'cave_spider', 'Scorpion des sables', 'gold', 'e', 70, 11, 0.32, 2.3, 60, 20, 35, prov=True, onhit='poison 4 1')
kind('desseche', 'parched', 'Archer desséché', 'yellow', 'e', 64, 9, 0.27, 1.0, 58, 18, 30, und=True, eq={'mainhand': it('bow')})
kind('djinn', 'breeze', 'Djinn des vents', 'aqua', 'e', 70, 10, 0.3, 1.2, 62, 22, 35)
kind('pillard', 'vindicator', 'Pillard du désert', 'gold', 'e', 84, 13, 0.33, 1.0, 64, 24, 30,
     eq={'mainhand': it('golden_axe'), 'head': it('golden_helmet'), 'chest': it('golden_chestplate')})
# ---- Pyrecendre
kind('drake', 'beast:drake', 'Drake des braises', 'gold', 'se', 150, 15, 0.32, 1.0, 90, 30, 50)
kind('feu', 'blaze', 'Élémentaire de feu', 'gold', 'se', 90, 12, 0.3, 1.0, 80, 26, 35)
kind('magma', 'magma_cube', 'Cube de magma', 'red', 'se', 80, 12, 0.4, 1.0, 76, 24, 40, nbt='Size:2,')
kind('brute', 'piglin_brute', 'Brute calcinée', 'dark_red', 'se', 130, 17, 0.35, 1.05, 96, 32, 35, nbt='IsImmuneToZombification:1b,',
     eq={'mainhand': it('golden_axe')})
kind('calcine', 'wither_skeleton', 'Chevalier calciné', 'dark_red', 'se', 120, 16, 0.3, 1.0, 94, 30, 35, und=True, eq={'mainhand': it('stone_sword')})
# ---- Khazgarde
kind('nain', 'vindicator', 'Nain renégat', 'gray', 's', 130, 17, 0.32, 0.8, 110, 36, 35,
     eq={'mainhand': it('iron_axe'), 'head': it('iron_helmet'), 'chest': it('iron_chestplate')})
kind('arbaletrier', 'pillager', 'Arbalétrier nain', 'gray', 's', 110, 13, 0.31, 0.8, 104, 34, 35, eq={'mainhand': it('crossbow'), 'head': it('iron_helmet')})
kind('gardien', 'iron_golem', 'Gardien runique', 'blue', 's', 200, 20, 0.27, 1.0, 140, 46, 50, prov=True, nbt='PlayerCreated:0b,')
kind('troggo', 'zombie', 'Troggoïde', 'dark_gray', 's', 140, 16, 0.27, 1.25, 110, 36, 35, nbt='CanBreakDoors:0b,',
     eq=leather(5592405, ('chest', 'chestplate'), ('legs', 'leggings')))
kind('rampant', 'cave_spider', 'Rampant des profondeurs', 'dark_gray', 's', 100, 14, 0.33, 1.9, 104, 32, 35, prov=True, onhit='poison 3 1')
# ---- Ombre
kind('chevnoir', 'wither_skeleton', 'Chevalier noir', 'dark_purple', 'sw', 180, 22, 0.3, 1.1, 150, 50, 35, und=True, onhit='wither 3 0',
     eq={'mainhand': it('netherite_sword'), 'chest': it('netherite_chestplate')})
kind('necro', 'evoker', 'Nécromancien', 'dark_purple', 'sw', 150, 10, 0.3, 1.0, 150, 50, 40)
kind('spectre', 'phantom', 'Spectre', 'dark_aqua', 'sw', 70, 14, 0.3, 1.2, 120, 40, 35, und=True, nbt='size:2,')
kind('errant', 'enderman', 'Ombre errante', 'dark_purple', 'sw', 160, 20, 0.32, 1.0, 140, 46, 40, prov=True, onhit='darkness 3 0')
kind('cultiste', 'vindicator', 'Cultiste de Malveth', 'dark_purple', 'sw', 160, 22, 0.33, 1.0, 150, 50, 35,
     eq={'mainhand': it('netherite_axe'), **leather(3289650, ('head', 'helmet'), ('chest', 'chestplate'))})
# ---- alphas des donjons (ne réapparaissent pas d'eux-mêmes)
kind('a_crypte', 'zombie', 'Seigneur des cryptes', 'dark_red', 'w', 320, 8, 0.27, 1.5, 300, 120, 100, und=True, alpha=True, nbt='CanBreakDoors:0b,',
     eq={'mainhand': it('iron_sword'), 'head': it('golden_helmet'), 'chest': it('chainmail_chestplate')})
kind('a_tisseuse', 'spider', 'Tisseuse alpha', 'dark_red', 'nw', 480, 10, 0.33, 2.2, 450, 180, 100, alpha=True, prov=True, onhit='poison 4 1')
kind('a_wendigo', 'stray', 'Wendigo des glaces', 'dark_red', 'n', 640, 14, 0.3, 1.7, 600, 240, 100, und=True, alpha=True, onhit='slowness 3 2',
     eq={'mainhand': it('iron_axe'), 'head': it('skeleton_skull')})
kind('a_noye', 'drowned', 'Gardien noyé', 'dark_red', 'ne', 820, 16, 0.3, 1.7, 760, 300, 100, und=True, alpha=True,
     eq={'mainhand': it('trident'), 'head': it('turtle_helmet')})
kind('a_momie', 'husk', 'Momie royale', 'dark_red', 'e', 1000, 18, 0.27, 1.7, 900, 360, 100, und=True, alpha=True,
     eq={'mainhand': it('golden_sword'), 'head': it('golden_helmet'), 'chest': it('golden_chestplate')})
kind('a_forgeron', 'wither_skeleton', 'Forgeron calciné', 'dark_red', 'se', 1200, 20, 0.3, 1.5, 1050, 420, 100, und=True, alpha=True,
     eq={'mainhand': it('netherite_axe')})
kind('a_contremaitre', 'vindicator', 'Contremaître maudit', 'dark_red', 's', 1400, 22, 0.33, 1.1, 1200, 480, 100, alpha=True,
     eq={'mainhand': it('diamond_axe'), 'head': it('diamond_helmet'), 'chest': it('diamond_chestplate')})
kind('a_ames', 'wither_skeleton', 'Gardien des âmes', 'dark_red', 'sw', 1700, 26, 0.3, 1.7, 1400, 560, 100, und=True, alpha=True,
     eq={'mainhand': it('netherite_sword'), 'head': it('wither_skeleton_skull')})
# ---- serviteurs des boss
kind('arachneen', 'cave_spider', 'Rejeton', 'dark_green', 'nw', 14, 3, 0.34, 1.0, 6, 2, 10, prov=True, minion=True)
kind('ossement', 'skeleton', 'Garde squelette', 'white', 'sw', 90, 14, 0.3, 1.0, 40, 10, 10, und=True, minion=True, eq={'mainhand': it('stone_sword')})

KINDS = list(K)
KIDX = {k: i for i, k in enumerate(KINDS)}
REG_KINDS = {r: [k for k in KINDS if K[k]['reg'] == r and not K[k].get('alpha') and not K[k].get('minion')] for r in W.ORDER}
UNDEAD = [k for k in KINDS if K[k].get('und')]
PROV = [k for k in KINDS if K[k].get('prov')]


def bitobj(i):
    return ('mg.olbs', i) if i < 30 else ('mg.olbs2', i - 30)


# ================================================================ apparition d'une espèce (à la position courante)
def attrs(hp, dmg, spd, scale, follow=40, kb=None, armor=None):
    a = [f'{{id:"minecraft:max_health",base:{hp}}}', f'{{id:"minecraft:attack_damage",base:{dmg}}}', f'{{id:"minecraft:movement_speed",base:{spd}}}',
         f'{{id:"minecraft:follow_range",base:{follow}}}', f'{{id:"minecraft:scale",base:{scale}}}', '{id:"minecraft:step_height",base:1.1}']
    if kb is not None:
        a.append(f'{{id:"minecraft:knockback_resistance",base:{kb}}}')
    if armor is not None:
        a.append(f'{{id:"minecraft:armor",base:{armor}}}')
    return 'attributes:[' + ','.join(a) + ']'


for k, d in K.items():
    tags = f'"mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_{k}"' + (',"mg.olund"' if d.get('und') else '') + (',"mg.olprov"' if d.get('prov') else '') + \
        (',"mg.olalpha"' if d.get('alpha') else '')
    name = js(TEXT(d['name'], d['col']))
    if d['mob'].startswith('beast:'):
        b = d['mob'].split(':')[1]
        w(f'm/{k}', [f'# {d["name"]} (créature articulée)', f'function mg:{P}/beast/{b}',
                     f'tag @e[tag=mg.ollast] add mg.olk_{k}', 'tag @e[tag=mg.ollast] add mg.olm',
                     f'execute as @e[tag=mg.ollast] run data merge entity @s {{CustomName:{name}}}'])
        continue
    eq = d.get('eq') or {}
    eqs = ''
    if eq:
        eqs = 'equipment:{' + ','.join(f'{s}:{v}' for s, v in eq.items()) + '},drop_chances:{' + ','.join(f'{s}:0f' for s in eq) + '},'
    kb = 0.6 if d.get('alpha') else None
    res = 'active_effects:[{id:"minecraft:resistance",amplifier:0,duration:-1,show_particles:0b}],' if d['hp'] > 1150 else ''
    w(f'm/{k}', [f'# {d["name"]} ({d["mob"]}, région {d["reg"]})', 'tag @e[tag=mg.ollast] remove mg.ollast',
                 f'summon minecraft:{d["mob"]} ~ ~ ~ {{Tags:[{tags}],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,'
                 f'CustomName:{name},CustomNameVisible:0b,Health:{min(d["hp"], 1024)}f,{eqs}{d.get("nbt", "")}{res}{attrs(min(d["hp"], 1024), d["dmg"], d["spd"], d["scale"], kb=kb)}}}',
                 'scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st', 'tag @e[tag=mg.oln] remove mg.oln'])

# ================================================================ élites
w('m/elite', ['# @s devient une élite : PV ×2,5, contour doré, affixe, butin à sa mort',
              'tag @s add mg.olelite', 'attribute @s minecraft:max_health modifier add mg:olelite 1.5 add_multiplied_total',
              'attribute @s minecraft:attack_damage modifier add mg:olelite 0.3 add_multiplied_base',
              'execute store result entity @s Health float 1 run attribute @s minecraft:max_health get',
              'data merge entity @s {Glowing:1b,CustomNameVisible:1b}', 'team join mg_olel @s',
              'execute store result score $r mg.st run random value 1..4',
              'execute if score $r mg.st matches 1 run effect give @s minecraft:speed infinite 1 true',
              'execute if score $r mg.st matches 2 run attribute @s minecraft:scale modifier add mg:olelite 0.3 add_multiplied_base',
              'execute if score $r mg.st matches 2 run attribute @s minecraft:knockback_resistance base set 1',
              'execute if score $r mg.st matches 3 run effect give @s minecraft:regeneration infinite 1 true',
              'execute if score $r mg.st matches 4 run effect give @s minecraft:resistance infinite 0 true',
              'tag @s add mg.olelnm'])

# ================================================================ points d'apparition (marqueurs de la session)
rs = random.Random(5150)
SPAWN_PTS = {r: [] for r in W.ORDER}
for r in W.ORDER:
    x0, z0, x1, z1 = W.rect(r)
    tries = 0
    while len(SPAWN_PTS[r]) < 46 and tries < 20000:
        tries += 1
        x, z = rs.randrange(x0 + 8, x1 - 8), rs.randrange(z0 + 8, z1 - 8)
        if W.COL[(x, z)][2]:
            continue
        fl = W.flat_at(x, z)
        if fl and fl[1] > 0:
            continue
        d, key, dc, outer = W.border_info(x, z)
        if d < 14:
            continue
        if any(math.hypot(x - a, z - b) < 12 for a, y_, b in SPAWN_PTS[r]):
            continue
        SPAWN_PTS[r].append((x, W.ground(x, z), z))

# ================================================================ population : un groupe par seconde près des joueurs
REG_IDX = {r: i + 1 for i, r in enumerate(W.ORDER)}
POP = ['# Une région par seconde (cycle de 8 s) : groupe de monstres si elle a des joueurs et de la place']
for r in W.ORDER:
    i = REG_IDX[r]
    POP.append(f'execute if score $olcy mg.st matches {i} if entity @a[tag=mg.olw,scores={{mg.olrg={i}}}] run function mg:{P}/m/pop_{r}')
w('m/pop', POP)
for r in W.ORDER:
    i = REG_IDX[r]
    ks = REG_KINDS[r]
    L = [f'# Région {W.REGIONS[r][1]} : 10 monstres + 4 par joueur présent (22 au plus)',
         f'execute store result score $n mg.st if entity @e[tag=mg.olm,tag=mg.olr_{r}]',
         f'execute store result score $cap mg.st if entity @a[tag=mg.olw,scores={{mg.olrg={i}}}]',
         'scoreboard players operation $cap mg.st *= #4 mg.st', 'scoreboard players add $cap mg.st 10',
         'execute if score $cap mg.st matches 23.. run scoreboard players set $cap mg.st 22',
         'execute if score $n mg.st >= $cap mg.st run return 0',
         'tag @e[tag=mg.olok] remove mg.olok',
         f'execute as @e[type=minecraft:marker,tag=mg.olsp_{r}] at @s if entity @a[tag=mg.olw,distance=22..70] unless entity @a[tag=mg.olw,distance=..18] run tag @s add mg.olok',
         f'execute as @e[tag=mg.olok,sort=random,limit=1] at @s run function mg:{P}/m/grp_{r}', 'tag @e[tag=mg.olok] remove mg.olok']
    w(f'm/pop_{r}', L)
    G = [f'# Groupe de la région {r} : une espèce tirée au sort, 1 à 3 individus', f'execute store result score $r mg.st run random value 0..{len(ks) - 1}',
         'execute store result score $g mg.st run random value 1..3']
    for j, k in enumerate(ks):
        G.append(f'execute if score $r mg.st matches {j} run function mg:{P}/m/grp_one {{k:"{k}"}}')
    G += [f'tag @e[tag=mg.olnew] add mg.olr_{r}',
          'execute if predicate mg:tv_c10 as @e[tag=mg.olnew,sort=random,limit=1] run function mg:ombre/m/elite',
          'execute as @e[tag=mg.olnew,tag=mg.olprov] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..64]',
          'tag @e[tag=mg.olnew] remove mg.olnew']
    w(f'm/grp_{r}', G)
w('m/grp_one', ['# $(k) ×$g ici', '$function mg:ombre/m/$(k)', 'tag @e[tag=mg.ollast] add mg.olnew', 'scoreboard players remove $g mg.st 1',
                '$execute if score $g mg.st matches 1.. positioned ~1.5 ~ ~1 run function mg:ombre/m/grp_one {k:"$(k)"}'])

# ================================================================ chaque seconde : provocation des neutres, capacités, nettoyage
w('m/second', ['# Chaque seconde : monstres neutres provoqués, capacités, noms des élites, nettoyage au loin',
               'scoreboard players add $olcy mg.st 1', 'execute if score $olcy mg.st matches 9.. run scoreboard players set $olcy mg.st 1',
               f'function mg:{P}/m/pop',
               '# toutes les 3 s : un neutre sans proie proche « flaire » un joueur à 20 blocs',
               'execute if score $olq60 mg.st matches 0 as @e[tag=mg.olprov] at @s unless entity @a[tag=mg.olw,distance=..5] if entity @a[tag=mg.olw,gamemode=adventure,distance=..20] run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..20]',
               'execute as @e[tag=mg.olelnm] run function mg:ombre/m/elite_name',
               'execute if score $olq60 mg.st matches 20 as @e[tag=mg.olm,tag=!mg.olboss,tag=!mg.olalpha,tag=!mg.oldg] at @s unless entity @a[tag=mg.olw,distance=..100] run kill @s',
               '# capacités',
               'execute as @e[tag=mg.olk_yeti] at @s if entity @a[tag=mg.olw,gamemode=adventure,distance=..3] if predicate mg:tv_c20 run function mg:ombre/m/ab_slam',
               'execute as @e[tag=mg.olk_drake] at @s if entity @a[tag=mg.olw,gamemode=adventure,distance=3..9] if predicate mg:tv_c33 run function mg:ombre/m/ab_breath',
               'execute as @e[tag=mg.olk_garou] at @s if entity @a[tag=mg.olw,gamemode=adventure,distance=3..8] if predicate mg:tv_c20 run function mg:ombre/m/ab_pounce',
               'execute as @e[tag=mg.olk_gardien] at @s if entity @a[tag=mg.olw,gamemode=adventure,distance=..4] if predicate mg:tv_c20 run function mg:ombre/m/ab_slam',
               'execute as @e[tag=mg.olk_a_tisseuse] at @s if entity @a[tag=mg.olw,gamemode=adventure,distance=..10] if predicate mg:tv_c20 run function mg:ombre/m/ab_web'])
w('m/elite_name', ['# Nom de l\'élite (une fois)', 'tag @s remove mg.olelnm', 'data modify storage mg:ombre en set from entity @s CustomName.text',
                   'function mg:ombre/m/elite_name_m with storage mg:ombre'])
w('m/elite_name_m', ['$data merge entity @s {CustomName:{"text":"★ $(en)","color":"gold","bold":true}}'])
w('m/ab_slam', ['# Coup au sol : onde autour du monstre', 'particle minecraft:explosion ~ ~0.5 ~ 1.5 0.2 1.5 0 6',
                'playsound minecraft:entity.generic.explode hostile @a ~ ~ ~ 0.8 0.7',
                'execute as @a[tag=mg.olw,gamemode=adventure,distance=..4] run damage @s 6 minecraft:mob_attack by @e[tag=mg.olm,limit=1,sort=nearest]',
                'effect give @a[tag=mg.olw,gamemode=adventure,distance=..4] minecraft:slowness 2 1'])
w('m/ab_breath', ['# Drake : souffle de braises en cône', 'scoreboard players set @s mg.olat 10',
                  'playsound minecraft:entity.blaze.shoot hostile @a ~ ~ ~ 1 0.6',
                  'execute facing entity @p[tag=mg.olw,gamemode=adventure] eyes positioned ^ ^1 ^1.5 run particle minecraft:flame ^ ^ ^2 0.6 0.3 0.6 0.04 40 force',
                  'execute facing entity @p[tag=mg.olw,gamemode=adventure] eyes positioned ^ ^1 ^4 as @a[tag=mg.olw,gamemode=adventure,distance=..3] run function mg:ombre/m/burn'])
w('m/burn', ['damage @s 5 minecraft:in_fire', 'execute unless score @s mg.olfire matches 1.. run effect give @s minecraft:wither 2 0 true'])
w('m/ab_pounce', ['# Loup-garou : bond sur sa proie',
                  'execute facing entity @p[tag=mg.olw,gamemode=adventure] feet rotated ~ -18 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:ombre/vec {d:1.1}',
                  'function mg:ombre/push', 'playsound minecraft:entity.wolf.growl hostile @a ~ ~ ~ 1.2 0.6'])
w('m/ab_web', ['# Tisseuse alpha : toile sous le joueur le plus proche (3 s)',
               'execute as @p[tag=mg.olw,gamemode=adventure,distance=..10] at @s run function mg:ombre/m/web_at'])
w('m/web_at', ['execute if block ~ ~ ~ minecraft:air run summon minecraft:marker ~ ~ ~ {Tags:["mg.ol","mg.olweb"]}',
               'execute if block ~ ~ ~ minecraft:air run setblock ~ ~ ~ minecraft:cobweb', 'scoreboard players set @e[tag=mg.olweb,distance=..0.5] mg.olst 60'])
w('m/web_tick', ['# Toiles posées par les monstres : retirées après 3 s', 'scoreboard players remove @e[type=minecraft:marker,tag=mg.olweb] mg.olst 1',
                 'execute as @e[type=minecraft:marker,tag=mg.olweb,scores={mg.olst=..0}] at @s run function mg:ombre/m/web_end'])
w('m/web_end', ['execute if block ~ ~ ~ minecraft:cobweb run setblock ~ ~ ~ minecraft:air', 'kill @s'])
w('vec', ['# Marqueur placé au bout du vecteur (contexte : origine, orientation voulue)', '$tp @s ^ ^ ^$(d)', 'tag @s add mg.olv'])
w('push', ['# @s : élan = vecteur du marqueur mg.olv', 'data modify entity @s Motion set from entity @e[type=minecraft:marker,tag=mg.olv,limit=1] Pos',
           'kill @e[type=minecraft:marker,tag=mg.olv]'])

# effets au toucher (joueur blessé par une espèce à effet)
HURT = ['# @s (joueur) vient d\'être blessé : effet de l\'attaquant, animation des créatures', 'scoreboard players set @s mg.oldt 0',
        'execute on attacker if entity @s[tag=mg.olbd] run scoreboard players set @s mg.olat 8']
for k, d in K.items():
    if d.get('onhit'):
        e, s, a = d['onhit'].split()
        HURT.append(f'execute if function mg:{P}/m/att_{k} run effect give @s minecraft:{e} {s} {a}')
        w(f'm/att_{k}', [f'# L\'attaquant de @s est-il un(e) {d["name"]} ?', f'execute on attacker if entity @s[tag=mg.olk_{k}] run return 1', 'return 0'])
w('m/hurt', HURT)

# ================================================================ victoires : progrès, récompenses, bestiaire
for i, k in enumerate(KINDS):
    d = K[k]
    wjson(f'advancement/{P}/k/{k}.json', {'criteria': {'k': {'trigger': 'minecraft:player_killed_entity', 'conditions': {'entity': [
        {'condition': 'minecraft:entity_properties', 'entity': 'this', 'predicate': {'nbt': '{Tags:["mg.olk_' + k + '"]}'}}]}}},
        'rewards': {'function': f'mg:{P}/k/{k}'}})
    mat = REG_MAT[d['reg']]
    mo, mn, mc = MATS[mat]
    o, b = bitobj(i)
    L = [f'# @s a vaincu : {d["name"]}', f'advancement revoke @s only mg:{P}/k/{k}', 'execute unless entity @s[tag=mg.olw] run return 0',
         'scoreboard players add @s mg.olkt 1', f'scoreboard players add @s mg.olg {d["gold"]}',
         f'function mg:{P}/xpk {{n:{d["xp"]}}}',
         f'execute store result score $r mg.st run random value 1..100',
         f'execute if score $r mg.st matches ..{d["mat"]} run scoreboard players add @s {mo} 1',
         'scoreboard players set @s mg.olal 30',
         f'execute if score $r mg.st matches ..{d["mat"]} run title @s actionbar ' +
         js([TEXT(f'+{d["gold"]} 💰  ', 'gold', bold=True), TEXT(f'+1 {mn}  ', mc), TEXT(d['name'], 'gray')]),
         f'execute unless score $r mg.st matches ..{d["mat"]} run title @s actionbar ' + js([TEXT(f'+{d["gold"]} 💰  ', 'gold', bold=True), TEXT(d['name'], 'gray')])]
    L += bit_test(o, b) + [f'execute if score $b mg.st matches 0 run function mg:{P}/k/new_{k}']
    L += [f'scoreboard players set $kk mg.st {i}', f'function mg:{P}/khook']
    w(f'k/{k}', L)
    w(f'k/new_{k}', [f'# Première victoire sur : {d["name"]} (bestiaire)', f'scoreboard players operation @s {o} += #p{b} mg.st',
                     'tellraw @s ' + js([TEXT('📖 Bestiaire : ', 'aqua'), TEXT(d['name'], d['col'], bold=True), TEXT(' ajouté (+XP)', 'gray')]),
                     f'function mg:{P}/xp {{n:{max(10, d["xp"] // 2)}}}', 'execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3'])
# élites (récompense en plus de l'espèce)
wjson(f'advancement/{P}/k/elite.json', {'criteria': {'k': {'trigger': 'minecraft:player_killed_entity', 'conditions': {'entity': [
    {'condition': 'minecraft:entity_properties', 'entity': 'this', 'predicate': {'nbt': '{Tags:["mg.olelite"]}'}}]}}},
    'rewards': {'function': f'mg:{P}/k/elite'}})
w('k/elite', [f'# @s a vaincu une élite : butin (or, matériaux de la région, gemme, poussière de lune)', f'advancement revoke @s only mg:{P}/k/elite',
              'execute unless entity @s[tag=mg.olw] run return 0', 'scoreboard players add @s mg.olel 1',
              'scoreboard players operation $c mg.st = @s mg.olrg', 'scoreboard players add $c mg.st 1', 'scoreboard players operation $c mg.st *= #40 mg.st',
              'scoreboard players operation @s mg.olg += $c mg.st',
              'tellraw @s [{"text":"📦 Butin d\'élite : +","color":"gold"},{"score":{"name":"$c","objective":"mg.st"},"color":"yellow"},{"text":" 💰","color":"yellow"}]',
              f'function mg:{P}/mat_region {{n:3}}',
              'execute store result score $r mg.st run random value 1..100',
              'execute if score $r mg.st matches ..25 run scoreboard players add @s mg.olsp 1',
              'execute if score $r mg.st matches ..25 run tellraw @s {"text":"  💎 Gemme de lune : +1 point de caractéristique !","color":"light_purple"}',
              'execute if score $r mg.st matches 90.. run scoreboard players add @s mg.olm9 1',
              'execute if score $r mg.st matches 90.. run tellraw @s {"text":"  ✦ +1 poussière de lune (rare)","color":"light_purple"}',
              f'function mg:{P}/xp {{n:60}}', 'execute at @s run playsound minecraft:block.chest.open player @s ~ ~ ~ 0.7 1.2'])
MR = ['# @s : $(n) matériau(x) de la région où il se trouve']
for r, m in REG_MAT.items():
    MR.append(f'$execute if score @s mg.olrg matches {REG_IDX[r]} run scoreboard players add @s {MATS[m][0]} $(n)')
    MR.append(f'$execute if score @s mg.olrg matches {REG_IDX[r]} run tellraw @s {{"text":"  +$(n) {MATS[m][1]}","color":"{MATS[m][2]}"}}')
MR.append('$execute if score @s mg.olrg matches 0 run scoreboard players add @s mg.olm1 $(n)')
w('mat_region', MR)
w('xpk', ['# @s a vaincu un monstre : XP (et la moitié aux joueurs à 24 blocs)', '$function mg:ombre/xp {n:$(n)}',
          '$scoreboard players set $xk mg.st $(n)', 'scoreboard players operation $xk mg.st /= #2 mg.st',
          'execute store result storage mg:ombre s.n int 1 run scoreboard players get $xk mg.st',
          'execute at @s as @a[tag=mg.olw,distance=0.1..24] run function mg:ombre/xpm with storage mg:ombre s'])
w('xpm', ['$function mg:ombre/xp {n:$(n)}'])

# bestiaire (liste)
BL = ['# @s : bestiaire dans le chat', 'tellraw @s ' + js(TEXT('\n📖 Bestiaire d\'Ombrelune', 'aqua', bold=True))]
for i, k in enumerate(KINDS):
    d = K[k]
    if d.get('minion'):
        continue
    o, b = bitobj(i)
    BL += bit_test(o, b)
    BL.append('execute if score $b mg.st matches 1 run tellraw @s ' + js([TEXT(' ✔ ', 'green'), TEXT(d['name'], d['col'], bold=True),
                                                                       TEXT(f'  {W.REGIONS[d["reg"]][1]}', 'dark_gray')]))
    BL.append('execute if score $b mg.st matches 0 run tellraw @s ' + js([TEXT(' ✖ ??? ', 'dark_gray'), TEXT(f' {W.REGIONS[d["reg"]][1]}', 'dark_gray')]))
w('bestiary', BL)
N_BEST = len([k for k in KINDS if not K[k].get('minion')])
