"""🦖 Terra Nova : fonctions des dinosaures (apparition, modèle articulé, animation). Exécuté par gen_terranova.py (exec) :
utilise w, js, attrs, INVIS, TR et le module tv_dinos (T)."""
import tv_dinos as T

# clé : (mob, tags, attributs, nbt du mob, PV)
MOBS = {
    'raptor': ('vindicator', '"mg.tvhos","mg.tvraptor"', attrs(hp=18, spd=0.46, fol=48, dmg=5, scale=0.85, step=1.1),
               'CanPickUpLoot:0b,', 18),
    'carno': ('hoglin', '"mg.tvhos","mg.tvcarno"', attrs(hp=160, spd=0.33, fol=40, dmg=12, scale=1.5, step=1.1, kb=0.8, akb=1.5),
              'IsImmuneToZombification:1b,CannotBeHunted:1b,', 160),
    'rex': ('ravager', '"mg.tvhos","mg.tvboss","mg.tvrex","mg.tvbig"', attrs(hp=900, spd=0.31, fol=64, dmg=20, scale=1.9, step=1.6, kb=1.0, akb=1.2),
            'CanJoinRaid:0b,PatrolLeader:0b,', 900),
    'dilo': ('zombie_villager', '"mg.tvhos","mg.tvdilo"', attrs(hp=26, spd=0.3, fol=40, dmg=4, scale=1.05, step=1.1),
             'CanPickUpLoot:0b,CanBreakDoors:0b,VillagerData:{profession:"minecraft:none",level:1,type:"minecraft:swamp"},', 26),
    'spino': ('piglin_brute', '"mg.tvhos","mg.tvboss","mg.tvspino","mg.tvbig"', attrs(hp=650, spd=0.36, fol=56, dmg=16, scale=2.3, step=1.6, kb=1.0, akb=1.0),
              'IsImmuneToZombification:1b,CanPickUpLoot:0b,', 650),
    'compy': ('silverfish', '"mg.tvhos","mg.tvcompy"', attrs(hp=5, spd=0.34, fol=32, dmg=1.5, scale=1.0), '', 5),
    'galli': ('pig', '"mg.tvherb","mg.tvgalli"', attrs(hp=14, spd=0.32, scale=1.15, step=1.1), '', 14),
    'pachy': ('goat', '"mg.tvherb","mg.tvpachy"', attrs(hp=24, spd=0.32, scale=1.2), 'HasLeftHorn:0b,HasRightHorn:0b,IsScreamingGoat:0b,', 24),
    'trike': ('iron_golem', '"mg.tvherb","mg.tvdef","mg.tvtrike"', attrs(hp=90, spd=0.25, dmg=9, scale=1.05, kb=1.0, step=1.1),
              'PlayerCreated:0b,', 90),
    'stego': ('polar_bear', '"mg.tvherb","mg.tvdef","mg.tvstego"', attrs(hp=70, spd=0.24, dmg=7, scale=1.5, kb=0.9, step=1.1), '', 70),
    'ankylo': ('panda', '"mg.tvherb","mg.tvdef","mg.tvankylo"', attrs(hp=90, spd=0.2, dmg=8, scale=1.6, kb=1.0, step=1.1, armor=14),
               'MainGene:"aggressive",HiddenGene:"aggressive",', 90),
    'brachio': ('camel', '"mg.tvherb","mg.tvbig","mg.tvbrach"', attrs(hp=120, spd=0.11, scale=2.0, kb=1.0, jump=0.5), '', 120),
    'ptera': ('phantom', '"mg.tvhos","mg.tvptera"', attrs(hp=16, scale=1.3, dmg=4), 'Size:1,', 16),
}
# tags des kills (statistique minecraft.killed:<mob>) : utilisés par les primes
KILL_OBJ = {m[0]: k for k, m in MOBS.items()}


def f4(v):
    return f'{round(v, 4):g}f'


def tr(pos, q, s):
    return (f'transformation:{{translation:[{f4(pos[0])},{f4(pos[1])},{f4(pos[2])}],left_rotation:[{f4(q[0])},{f4(q[1])},{f4(q[2])},{f4(q[3])}],'
            f'right_rotation:[0f,0f,0f,1f],scale:[{f4(s)},{f4(s)},{f4(s)}]}}')


def box_tr(pos, q, b):
    x1, y1, z1, x2, y2, z2, _ = b
    t = T.vadd(pos, T.qrot(q, (x1, y1, z1)))
    return (f'transformation:{{translation:[{f4(t[0])},{f4(t[1])},{f4(t[2])}],left_rotation:[{f4(q[0])},{f4(q[1])},{f4(q[2])},{f4(q[3])}],'
            f'right_rotation:[0f,0f,0f,1f],scale:[{f4(x2 - x1)},{f4(y2 - y1)},{f4(z2 - z1)}]}}')


# ---------------------------------------------------------------- pose d'un os : position de l'articulation + lacet / tangage / roulis
# Chaque os du modèle 3D est une item_display posée SUR son articulation (translation nulle) : l'animation se fait par
# « tp @s ^x ^y ^z ~lacet tangage » (le client interpole position et rotation), bien moins coûteux qu'un « data merge »
# (≈ 20 fois plus lent : l'entité est entièrement resérialisée). L'entité d'affichage tourne selon Ry(-lacet)·Rx(tangage) ;
# le roulis restant (ailes, collerette) est porté par la transformation (data merge seulement pour ces os-là).
import math


def yxz(q):
    """Quaternion -> (a, b, c) en degrés avec q = Ry(a)·Rx(b)·Rz(c)."""
    x, y, z, w_ = q
    m02 = 2 * (x * z + w_ * y)
    m12 = 2 * (y * z - w_ * x)
    m22 = 1 - 2 * (x * x + y * y)
    m10 = 2 * (x * y + w_ * z)
    m11 = 1 - 2 * (x * x + z * z)
    b = math.asin(max(-1.0, min(1.0, -m12)))
    return math.degrees(math.atan2(m02, m22)), math.degrees(b), math.degrees(math.atan2(m10, m11))


def g4(v):
    return f'{round(v, 4):g}'


PT = '"mg.tv","mg.tvp","mg.tvn","mg.tvok"'
BONE_ID = {}                                  # (espèce, os) -> n° unique (score mg.tvab de l'item_display)
for key, sp in T.SPECIES.items():
    for b in sp.bones:
        BONE_ID[(key, b.name)] = len(BONE_ID) + 1
ROLL = {}                                     # os dont le roulis varie (animé aussi par data merge)
POSE = {}                                     # (espèce, os) -> {(état, image): (pos, lacet, tangage, roulis)}
for key, sp in T.SPECIES.items():
    for si, st in enumerate(T.STATES):
        for f in range(T.FRAMES):
            P = T.poses(sp, st, f)
            for b in sp.bones:
                pos, q = P[b.name]
                a, bb, c = yxz(q)
                POSE.setdefault((key, b.name), {})[(si, f)] = (pos, a, bb, c)
    for b in sp.bones:
        cs = [v[3] for v in POSE[(key, b.name)].values()]
        if max(cs) - min(cs) > 6:                  # roulis réel (ailes, collerette) : les petits roulis de bout de queue sont ignorés
            ROLL[(key, b.name)] = True


def rollq(c):
    return T.qaxis('z', c)


def leaf(key, bn, si, f):
    pos, a, b, c = POSE[(key, bn)][(si, f)]
    L = [f'tp @s ^{g4(pos[0])} ^{g4(pos[1])} ^{g4(pos[2])} ~{g4(-a)} {g4(b)}']
    if (key, bn) in ROLL:
        q = rollq(c)
        L.append(f'data merge entity @s {{start_interpolation:0,interpolation_duration:2,transformation:{{left_rotation:[{f4(q[0])},{f4(q[1])},{f4(q[2])},{f4(q[3])}]}}}}')
    return L


for key, sp in T.SPECIES.items():
    mob, tags, at, nbt, hp = MOBS[key]
    big = max(T.bone_extent(b) for b in sp.bones) * 2 > 6
    vr = 'view_range:2.5f,' if big else ''
    rest = T.poses(sp, 'idle', 0)
    w(f'terra/dino/{key}', [
        f'# Dinosaure : {sp.label} ({mob} invisible + modèle articulé, lié par mg.tvid)',
        'tag @e[tag=mg.tvlast] remove mg.tvlast', 'scoreboard players add $tvid mg.st 1',
        f'summon minecraft:{mob} ~ ~ ~ {{Tags:["mg.tv","mg.tvd","mg.tvtg","mg.tvn","mg.tvlast","mg.tvs_{key}",{tags}],PersistenceRequired:1b,Silent:1b,'
        f'DeathLootTable:"minecraft:empty",Health:{hp}f,CustomName:{js({"text": sp.label, "color": sp.color})},CustomNameVisible:0b,{nbt}{INVIS},{at}}}',
        f'execute if score $rp mg.st matches 1 run function mg:terra/dino/{key}_rp',
        f'execute unless score $rp mg.st matches 1 run function mg:terra/dino/{key}_bd',
        'scoreboard players operation @e[tag=mg.tvn] mg.tvid = $tvid mg.st',
        'scoreboard players operation @e[tag=mg.tvn] mg.tvses = $tvses mg.st',
        'scoreboard players set #3 mg.st 3', 'scoreboard players operation @e[tag=mg.tvn,tag=mg.tvd] mg.tvph = $tvid mg.st',
        'scoreboard players operation @e[tag=mg.tvn,tag=mg.tvd] mg.tvph %= #3 mg.st',
        'tag @e[tag=mg.tvn] remove mg.tvn',
        'execute as @e[tag=mg.tvlast,limit=1] at @s run function mg:terra/dsync'])
    RP = [f'# {sp.label} : os du modèle 3D (resource pack), posés sur leurs articulations, n° d\'os dans mg.tvab',
          'tag @e[tag=mg.tvn,tag=mg.tvd] add mg.tvrp', 'scoreboard players set @e[tag=mg.tvn,tag=mg.tvd] mg.tvak 0']
    for b in sp.bones:
        pos, a, bb, c = POSE[(key, b.name)][(0, 0)]
        RP.append(f'summon minecraft:item_display ~ ~ ~ {{Tags:[{PT},"mg.tvnb"],teleport_duration:1,{vr}'
                  f'item:{{id:"minecraft:paper",count:1,components:{{"minecraft:item_model":"mg:dino/{key}_{b.name}"}}}},'
                  f'{tr((0, 0, 0), rollq(c), T.bone_scale(b))}}}')
        RP += [f'scoreboard players set @e[tag=mg.tvnb] mg.tvab {BONE_ID[(key, b.name)]}', 'tag @e[tag=mg.tvnb] remove mg.tvnb']
    w(f'terra/dino/{key}_rp', RP)
    BD = [f'# {sp.label} : modèle en blocs (sans resource pack, pose fixe)']
    for b in sp.bones:
        pos, q = rest[b.name]
        for bx in b.boxes:
            BD.append(f'summon minecraft:block_display ~ ~ ~ {{Tags:[{PT}],teleport_duration:1,{vr}'
                      f'block_state:{{Name:"minecraft:{sp.mats[bx[6]][2]}"}},{box_tr(pos, q, bx)}}}')
    w(f'terra/dino/{key}_bd', BD)
    # animation : une fonction par image (état × 8 + image), appelée pour chaque os du dinosaure (une ligne par os)
    seen = {}
    for si, st in enumerate(T.STATES):
        F = []
        for f in range(T.FRAMES):
            L = []
            for b in sp.bones:
                lf = leaf(key, b.name, si, f)
                bid = BONE_ID[(key, b.name)]
                if len(lf) == 1:
                    L.append(f'execute if score @s mg.tvab matches {bid} run return run {lf[0]}')
                else:
                    w(f'terra/an/{key}/r{bid}_{si}_{f}', lf)
                    L.append(f'execute if score @s mg.tvab matches {bid} run return run function mg:terra/an/{key}/r{bid}_{si}_{f}')
            k = tuple(L)
            if k not in seen:
                seen[k] = f'terra/an/{key}/f{si * 8 + f}'
                w(seen[k], [f'# {sp.label} : @s (os) posé pour l’état {st}, image {f}'] + L)
            # pas de « return run » devant un execute à plusieurs entités : il s'arrêterait après la première
            F.append(f'execute if score $tvak mg.st matches {si * 8 + f} as @e[tag=mg.tvc,distance=..16] run function mg:{seen[k]}')
        w(f'terra/an/{key}/s{si}', [f'# {sp.label}, état {st} : image $tvak'] + F)
    w(f'terra/an/{key}/go', [f'# {sp.label} (contexte : position et cap du dinosaure) : pose de ses os marqués mg.tvc'] +
      [f'execute if score $tvak mg.st matches {si * 8}..{si * 8 + 7} run return run function mg:terra/an/{key}/s{si}' for si in range(len(T.STATES))])

w('terra/an_sp', ['# @s (dinosaure à modèle 3D) : pose des os selon l’espèce'] +
  [f'execute if entity @s[tag=mg.tvs_{k}] run return run function mg:terra/an/{k}/go' for k in T.SPECIES])
w('terra/an_state', ['# @s (dinosaure à modèle 3D) : état (0 repos, 1 marche, 2 attaque, 3 rugissement) et image suivante -> mg.tvak',
                     'scoreboard players set $tvas mg.st 0',
                     'execute if predicate mg:tv_moving run scoreboard players set $tvas mg.st 1',
                     'execute if score @s mg.tvat matches 1.. run scoreboard players set $tvas mg.st 2',
                     'execute if score @s mg.tvat matches 1.. if entity @s[tag=mg.tvroar] run scoreboard players set $tvas mg.st 3',
                     'scoreboard players remove @s[scores={mg.tvat=1..}] mg.tvat 2',
                     'execute if score @s mg.tvat matches ..0 run tag @s remove mg.tvroar',
                     '# au repos : une image sur deux (balancement lent)',
                     '# rythme indépendant de la fréquence des mises à jour : une image toutes les 2 ticks (4 au repos)',
                     'execute unless score $tvas mg.st matches 0 if score $tvq2b mg.st matches 0 run scoreboard players add @s mg.tvaf 1',
                     'execute if score $tvas mg.st matches 0 if score $tvq4b mg.st matches 0 run scoreboard players add @s mg.tvaf 1',
                     'execute if score @s mg.tvaf matches 8.. run scoreboard players set @s mg.tvaf 0',
                     'scoreboard players operation @s mg.tvak = $tvas mg.st', 'scoreboard players operation @s mg.tvak *= #8 mg.st',
                     'scoreboard players operation @s mg.tvak += @s mg.tvaf'])
w('terra/dsync', ['# @s (dinosaure, à sa position) : son modèle le suit. Os du modèle 3D posés sur leurs articulations (image mg.tvak),',
                  '# modèle en blocs simplement déplacé. Chaque tick à moins de 32 blocs d’un joueur, toutes les 3 ticks jusqu’à 64, 2 fois par seconde au loin.',
                  'scoreboard players operation $tvi mg.st = @s mg.tvid',
                  'execute if entity @s[tag=mg.tvrp] if entity @a[tag=mg.tvw,distance=..48] run function mg:terra/an_state',
                  'scoreboard players operation $tvak mg.st = @s mg.tvak',
                  'execute as @e[tag=mg.tvp,distance=..16] if score @s mg.tvid = $tvi mg.st run tag @s add mg.tvc',
                  '# téléporté (repoussé hors de la colonie…) : modèle cherché partout',
                  'execute unless entity @e[tag=mg.tvc,distance=..16,limit=1] as @e[tag=mg.tvp] if score @s mg.tvid = $tvi mg.st run tp @s ~ ~ ~',
                  'execute unless entity @e[tag=mg.tvc,distance=..16,limit=1] as @e[tag=mg.tvp,distance=..16] if score @s mg.tvid = $tvi mg.st run tag @s add mg.tvc',
                  'tag @e[tag=mg.tvc,distance=..16] add mg.tvok',
                  'execute if entity @s[tag=mg.tvrp] rotated ~ 0 run function mg:terra/an_sp',
                  'execute as @e[tag=mg.tvc,distance=..16] unless score @s mg.tvab matches 1.. run tp @s ~ ~ ~ ~ 0',
                  'tag @e[tag=mg.tvc,distance=..16] remove mg.tvc'])
