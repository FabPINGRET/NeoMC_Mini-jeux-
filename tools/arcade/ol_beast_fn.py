"""🐉 Ombrelune : fonctions des créatures articulées (apparition, modèle 3D, animation). Même technique que tv_dino_fn.py
(un item_display par os, posé sur son articulation par « tp ^x ^y ^z lacet tangage », roulis des ailes par data merge).
Module importé par gen_ombrelune.py.

Scores : mg.olid (lien corps <-> os), mg.olab (n° d'os), mg.olak (image), mg.olaf (n° d'image), mg.olat (attaque en cours).
Tags : mg.olbd (corps), mg.olbp (os), mg.olbc (os du corps en cours de pose).
"""
import math

import ol_beasts as T
from ol_core import w, js, P

INVIS = 'active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}]'


def f4(v):
    return f'{round(v, 4):g}f'


def g4(v):
    return f'{round(v, 4):g}'


def tr(pos, q, s):
    return (f'transformation:{{translation:[{f4(pos[0])},{f4(pos[1])},{f4(pos[2])}],left_rotation:[{f4(q[0])},{f4(q[1])},{f4(q[2])},{f4(q[3])}],'
            f'right_rotation:[0f,0f,0f,1f],scale:[{f4(s)},{f4(s)},{f4(s)}]}}')


def box_tr(pos, q, b):
    x1, y1, z1, x2, y2, z2, _ = b
    t = T.T.vadd(pos, T.T.qrot(q, (x1, y1, z1)))
    return (f'transformation:{{translation:[{f4(t[0])},{f4(t[1])},{f4(t[2])}],left_rotation:[{f4(q[0])},{f4(q[1])},{f4(q[2])},{f4(q[3])}],'
            f'right_rotation:[0f,0f,0f,1f],scale:[{f4(x2 - x1)},{f4(y2 - y1)},{f4(z2 - z1)}]}}')


def yxz(q):
    x, y, z, w_ = q
    m02 = 2 * (x * z + w_ * y)
    m12 = 2 * (y * z - w_ * x)
    m22 = 1 - 2 * (x * x + y * y)
    m10 = 2 * (x * y + w_ * z)
    m11 = 1 - 2 * (x * x + z * z)
    b = math.asin(max(-1.0, min(1.0, -m12)))
    return math.degrees(math.atan2(m02, m22)), math.degrees(b), math.degrees(math.atan2(m10, m11))


PT = '"mg.ol","mg.olbp","mg.oln"'
BONE_ID = {}
for key, sp in T.SPECIES.items():
    for b in sp.bones:
        BONE_ID[(key, b.name)] = len(BONE_ID) + 1
ROLL, POSE = {}, {}
for key, sp in T.SPECIES.items():
    for si, st in enumerate(T.STATES):
        for f in range(T.FRAMES):
            Pz = T.poses(sp, st, f)
            for b in sp.bones:
                pos, q = Pz[b.name]
                a, bb, c = yxz(q)
                POSE.setdefault((key, b.name), {})[(si, f)] = (pos, a, bb, c)
    for b in sp.bones:
        cs = [v[3] for v in POSE[(key, b.name)].values()]
        if max(cs) - min(cs) > 6:
            ROLL[(key, b.name)] = True


def rollq(c):
    return T.T.qaxis('z', c)


def leaf(key, bn, si, f):
    """Même convention que tv_dino_fn (item_display tourné de 180° autour de y : lacet + 180, tangage et roulis inversés)."""
    pos, a, b, c = POSE[(key, bn)][(si, f)]
    L = [f'tp @s ^{g4(pos[0])} ^{g4(pos[1])} ^{g4(pos[2])} ~{g4(180 - a)} {g4(-b)}']
    if (key, bn) in ROLL:
        q = rollq(-c)
        L.append(f'data merge entity @s {{start_interpolation:0,interpolation_duration:2,transformation:{{left_rotation:[{f4(q[0])},{f4(q[1])},{f4(q[2])},{f4(q[3])}]}}}}')
    return L


# corps : (mob vanilla, tags, attributs, nbt)
def attrs(**a):
    names = {'hp': 'max_health', 'spd': 'movement_speed', 'fol': 'follow_range', 'dmg': 'attack_damage', 'scale': 'scale',
             'step': 'step_height', 'kb': 'knockback_resistance', 'akb': 'attack_knockback', 'armor': 'armor'}
    return 'attributes:[' + ','.join(f'{{id:"minecraft:{names[k]}",base:{v}}}' for k, v in a.items()) + ']'


BODY = {
    'ignarok': ('ravager', '"mg.olm","mg.olboss","mg.olignarok","mg.olbig"', attrs(hp=1024, spd=0.3, fol=64, dmg=20, scale=1.9, step=1.6, kb=1.0, akb=1.2, armor=10),
                'CanJoinRaid:0b,PatrolLeader:0b,', 1024),
    'nyxar': ('ravager', '"mg.olm","mg.olboss","mg.olnyxar","mg.olbig"', attrs(hp=1024, spd=0.32, fol=64, dmg=24, scale=2.2, step=1.6, kb=1.0, akb=1.4, armor=14),
              'CanJoinRaid:0b,PatrolLeader:0b,', 1024),
    'drake': ('hoglin', '"mg.olm","mg.oldrake"', attrs(hp=150, spd=0.32, fol=40, dmg=15, scale=1.0, step=1.1, kb=0.6),
              'IsImmuneToZombification:1b,CannotBeHunted:1b,', 150),
}

RES = {'ignarok': 1, 'nyxar': 2}  # PV plafonnés à 1024 : résistance II / III
for key, sp in T.SPECIES.items():
    mob, tags, at, nbt, hp = BODY[key]
    rest = T.poses(sp, 'idle', 0)
    w(f'beast/{key}', [
        f'# Créature : {sp.label} ({mob} invisible + modèle articulé, lié par mg.olid)',
        'tag @e[tag=mg.ollast] remove mg.ollast', 'scoreboard players add $olid mg.st 1',
        f'summon minecraft:{mob} ~ ~ ~ {{Tags:["mg.ol","mg.olbd","mg.oln","mg.ollast","mg.olbs_{key}",{tags}],PersistenceRequired:1b,Silent:1b,'
        f'DeathLootTable:"minecraft:empty",Health:{hp}f,CustomName:{js({"text": sp.label, "color": sp.color})},CustomNameVisible:0b,{nbt}{INVIS},{at}}}',
        *([f'effect give @e[tag=mg.ollast] minecraft:resistance infinite {RES[key]} true'] if key in RES else []),
        f'execute if score $rp mg.st matches 1 run function mg:{P}/beast/{key}_rp',
        f'execute unless score $rp mg.st matches 1 run function mg:{P}/beast/{key}_bd',
        'scoreboard players operation @e[tag=mg.oln] mg.olid = $olid mg.st',
        'scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st',
        'tag @e[tag=mg.oln] remove mg.oln',
        f'execute as @e[tag=mg.ollast,limit=1] at @s run function mg:{P}/bsync'])
    RP = [f'# {sp.label} : os du modèle 3D (resource pack), posés sur leurs articulations, n° d\'os dans mg.olab',
          'tag @e[tag=mg.oln,tag=mg.olbd] add mg.olrp', 'scoreboard players set @e[tag=mg.oln,tag=mg.olbd] mg.olak 0']
    for b in sp.bones:
        pos, a, bb, c = POSE[(key, b.name)][(0, 0)]
        RP.append(f'summon minecraft:item_display ~ ~ ~ {{Tags:[{PT},"mg.olnb"],teleport_duration:1,view_range:3f,'
                  f'item:{{id:"minecraft:paper",count:1,components:{{"minecraft:item_model":"mg:beast/{key}_{b.name}"}}}},'
                  f'{tr((0, 0, 0), rollq(-c), T.bone_scale(b))}}}')
        RP += [f'scoreboard players set @e[tag=mg.olnb] mg.olab {BONE_ID[(key, b.name)]}', 'tag @e[tag=mg.olnb] remove mg.olnb']
    w(f'beast/{key}_rp', RP)
    BD = [f'# {sp.label} : modèle en blocs (sans resource pack, pose fixe)']
    for b in sp.bones:
        pos, q = rest[b.name]
        for bx in b.boxes:
            BD.append(f'summon minecraft:block_display ~ ~ ~ {{Tags:[{PT}],teleport_duration:1,view_range:3f,'
                      f'block_state:{{Name:"minecraft:{sp.mats[bx[6]][2]}"}},{box_tr(pos, q, bx)}}}')
    w(f'beast/{key}_bd', BD)
    seen = {}
    for si, st in enumerate(T.STATES):
        F = []
        for f in range(T.FRAMES):
            L = []
            for b in sp.bones:
                lf = leaf(key, b.name, si, f)
                bid = BONE_ID[(key, b.name)]
                if len(lf) == 1:
                    L.append(f'execute if score @s mg.olab matches {bid} run return run {lf[0]}')
                else:
                    w(f'an/{key}/r{bid}_{si}_{f}', lf)
                    L.append(f'execute if score @s mg.olab matches {bid} run return run function mg:{P}/an/{key}/r{bid}_{si}_{f}')
            k = tuple(L)
            if k not in seen:
                seen[k] = f'an/{key}/f{si * 8 + f}'
                w(seen[k], [f'# {sp.label} : @s (os) posé pour l\'état {st}, image {f}'] + L)
            F.append(f'execute if score $olak mg.st matches {si * 8 + f} as @e[tag=mg.olbc,distance=..24] run function mg:{P}/{seen[k]}')
        w(f'an/{key}/s{si}', [f'# {sp.label}, état {st} : image $olak'] + F)
    w(f'an/{key}/go', [f'# {sp.label} (contexte : position et cap de la créature) : pose de ses os marqués mg.olbc'] +
      [f'execute if score $olak mg.st matches {si * 8}..{si * 8 + 7} run return run function mg:{P}/an/{key}/s{si}' for si in range(len(T.STATES))])

w('an_sp', ['# @s (créature à modèle 3D) : pose des os selon l\'espèce'] +
  [f'execute if entity @s[tag=mg.olbs_{k}] run return run function mg:{P}/an/{k}/go' for k in T.SPECIES])
w('an_state', ['# @s (créature à modèle 3D) : état (0 repos, 1 marche, 2 attaque, 3 rugissement) et image suivante -> mg.olak',
               'scoreboard players set $olas mg.st 0',
               'execute if predicate mg:tv_moving run scoreboard players set $olas mg.st 1',
               'execute if score @s mg.olat matches 1.. run scoreboard players set $olas mg.st 2',
               'execute if score @s mg.olat matches 1.. if entity @s[tag=mg.olroar] run scoreboard players set $olas mg.st 3',
               'scoreboard players remove @s[scores={mg.olat=1..}] mg.olat 2',
               'execute if score @s mg.olat matches ..0 run tag @s remove mg.olroar',
               'execute unless score $olas mg.st matches 0 if score $olq2 mg.st matches 0 run scoreboard players add @s mg.olaf 1',
               'execute if score $olas mg.st matches 0 if score $olq4 mg.st matches 0 run scoreboard players add @s mg.olaf 1',
               'execute if score @s mg.olaf matches 8.. run scoreboard players set @s mg.olaf 0',
               'scoreboard players operation @s mg.olak = $olas mg.st', 'scoreboard players operation @s mg.olak *= #8 mg.st',
               'scoreboard players operation @s mg.olak += @s mg.olaf'])
w('bsync', ['# @s (créature, à sa position) : son modèle la suit (os posés sur leurs articulations, image mg.olak)',
            'scoreboard players operation $oli mg.st = @s mg.olid',
            'execute if entity @s[tag=mg.olrp] run function mg:ombre/an_state',
            'scoreboard players operation $olak mg.st = @s mg.olak',
            'execute as @e[tag=mg.olbp,distance=..24] if score @s mg.olid = $oli mg.st run tag @s add mg.olbc',
            'execute unless entity @e[tag=mg.olbc,distance=..24,limit=1] as @e[tag=mg.olbp] if score @s mg.olid = $oli mg.st run tp @s ~ ~ ~',
            'execute unless entity @e[tag=mg.olbc,distance=..24,limit=1] as @e[tag=mg.olbp,distance=..24] if score @s mg.olid = $oli mg.st run tag @s add mg.olbc',
            'execute if entity @s[tag=mg.olrp] rotated ~ 0 run function mg:ombre/an_sp',
            'execute as @e[tag=mg.olbc,distance=..24] unless score @s mg.olab matches 1.. run tp @s ~ ~ ~ ~ 0',
            'tag @e[tag=mg.olbc,distance=..24] remove mg.olbc'])
w('bclean', ['# Os orphelins (créature morte) : retirés (chaque seconde)',
             'execute as @e[type=minecraft:item_display,tag=mg.olbp] run function mg:ombre/bclean_one',
             'execute as @e[type=minecraft:block_display,tag=mg.olbp] run function mg:ombre/bclean_one'])
w('bclean_one', ['scoreboard players operation $oli mg.st = @s mg.olid', 'tag @s add mg.olorph',
                 'execute as @e[tag=mg.olbd] if score @s mg.olid = $oli mg.st run tag @e[tag=mg.olorph] remove mg.olorph',
                 'execute if entity @s[tag=mg.olorph] run kill @s'])
