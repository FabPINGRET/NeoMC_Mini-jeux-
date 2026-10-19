"""🎬 Ombrelune : cinématiques (introduction, ouverture de chaque région, boss, fin) et indicateur d'objectif.
Même moteur que Terra Nova (tv_cine.py) : caméra item_display posée à chaque tick sur une courbe de Catmull-Rom, joueur en spectateur.
Scores : mg.olcs (n° de la cinématique), mg.olctk (tick). Tag mg.olcine pendant la cinématique.
"""
import math

import ol_world as W
import ol_structs as S
from ol_core import w, js, P, TEXT, DIM

A = S.ARENAS
CS = 'cs'


def g4(v):
    return f'{round(v, 4):g}'


def look(frm, to):
    dx, dy, dz = to[0] - frm[0], to[1] - frm[1], to[2] - frm[2]
    return round(-math.degrees(math.atan2(dx, dz)), 1), round(-math.degrees(math.atan2(dy, math.hypot(dx, dz))), 1)


def k(t, pos, at, title=None, sub=None, sound=None, cmds=()):
    return {'t': t, 'pos': pos, 'at': at, 'title': title, 'sub': sub, 'sound': sound, 'cmds': list(cmds)}


def gy(x, z, up=0):
    return W.ground(int(x), int(z)) + up if (int(x), int(z)) in W.H else 70 + up


C_ = {}
C_['intro'] = (1, 'spawn', [
    k(0, (-110, 120, 110), (0, 70, 0), 'OMBRELUNE', 'Il y a cent ans, la Pierre-Lune fut brisée…', 'minecraft:block.portal.travel'),
    k(60, (-60, 105, 80), (0, 72, 0), None, '…et le royaume sombra dans un crépuscule sans fin.', 'minecraft:ambient.cave'),
    k(120, (40, 98, 70), (0, 72, -10), None, 'Havreclair, la cité-refuge, tient encore debout.'),
    k(180, (80, 92, -10), (0, 75, -36), None, 'Ses remparts protègent les derniers hommes libres.', 'minecraft:block.bell.use'),
    k(240, (20, 90, -80), (-34, 80, -34), None, 'Dans la tour des mages, l\'archimagesse Liora attend…'),
    k(300, (-20, 82, -14), (-34, 72, -34), None, '…le Porteur de l\'Aube. Toi.', 'minecraft:block.amethyst_block.resonate'),
    k(350, (-6, 70, 4), (0, 68, 14), None, None),
    k(380, (-6, 70, 4), (0, 68, 14), None, None),
])
REG_TXT = {'w': 'Plaines de Valdor', 'nw': 'Forêt de Sylvanor', 'n': 'Pics de Givrecroc', 'ne': 'Marais de Fangebrume', 'e': 'Sables d\'Azhar',
           'se': 'Pyrecendre', 's': 'Khazgarde', 'sw': 'Terres d\'Ombre'}
FROM = {'w': 'hub', 'nw': 'w', 'n': 'nw', 'ne': 'n', 'e': 'ne', 'se': 'e', 's': 'se', 'sw': 's'}
for i, r in enumerate(W.ORDER):
    a, b = FROM[r], r
    key = (a, b) if (a, b) in W.PASS_AT else (b, a)
    px, pz = W.PASS_AT[key]
    x0, z0, x1, z1 = W.rect(r)
    cx, cz = (x0 + x1) / 2, (z0 + z1) / 2
    py = gy(px, pz)
    ins = (px + (cx - px) * 0.25, pz + (cz - pz) * 0.25)
    C_['open_' + r] = (10 + i, 'back', [
        k(0, (px - (cx - px) * 0.15, py + 16, pz - (cz - pz) * 0.15), (px, py + 4, pz), REG_TXT[r].upper(), 'Une nouvelle région s\'ouvre', 'minecraft:event.mob_effect.raid_omen'),
        k(60, (ins[0], py + 24, ins[1]), (cx, gy(cx, cz, 4), cz), None, f'Niveaux conseillés {W.REGIONS[r][3][0]} à {W.REGIONS[r][3][1]}'),
        k(120, (cx + (px - cx) * 0.3, gy(cx, cz, 34), cz + (pz - cz) * 0.3), (cx, gy(cx, cz, 2), cz), None, None),
        k(140, (cx + (px - cx) * 0.3, gy(cx, cz, 34), cz + (pz - cz) * 0.3), (cx, gy(cx, cz, 2), cz), None, None)])
BOSS_TXT = {'brennic': ('BRENNIC', 'Seigneur des brigands'), 'ystar': ('YSH\'TAR', 'La reine-araignée'), 'hrimgar': ('HRIMGAR', 'Le géant du givre'),
            'morvaine': ('MORVAINE', 'La mère-sorcière'), 'sethkar': ('SETHKAR', 'Le pharaon-liche'), 'ignarok': ('IGNAROK', 'Dragon de feu'),
            'colosse': ('LE COLOSSE DE RUNES', 'Gardien de Khazgarde'), 'malveth': ('MALVETH', 'L\'archimage de la Lune Noire'),
            'nyxar': ('NYXAR', 'Dragon de la Lune Noire')}
for i, (b, (t1, t2)) in enumerate(BOSS_TXT.items()):
    (cx, cy, cz), r = A[b]['c'], A[b]['r']
    h = A[b].get('home', (cx, cy, cz))
    big = b in ('ignarok', 'nyxar', 'colosse', 'hrimgar', 'ystar')
    up = 6 if big else 3
    C_['boss_' + b] = (30 + i, 'back', [
        k(0, (h[0] + r * 0.9, h[1] + up + 6, h[2] + r * 0.9), (h[0], h[1] + up, h[2]), None, None, 'minecraft:entity.warden.heartbeat'),
        k(50, (h[0] + r * 0.45, h[1] + up, h[2] + r * 0.45), (h[0], h[1] + up, h[2]), t1, t2, 'minecraft:entity.ender_dragon.growl' if big else 'minecraft:event.raid.horn'),
        k(100, (h[0] + r * 0.35, h[1] + up - 1, h[2] + r * 0.3), (h[0], h[1] + up + 1, h[2]), None, None),
        k(115, (h[0] + r * 0.35, h[1] + up - 1, h[2] + r * 0.3), (h[0], h[1] + up + 1, h[2]), None, None)])
C_['finale'] = (50, 'spawn', [
    k(0, (0, 110, 90), (0, 70, 0), 'L\'AUBE SE LÈVE', 'La Pierre-Lune est reformée', 'minecraft:ui.toast.challenge_complete'),
    k(70, (90, 104, 0), (0, 70, 0), None, 'Les éclats ont retrouvé leur lumière, le ciel s\'éclaircit…'),
    k(140, (0, 100, -90), (0, 70, 0), None, '…et Havreclair célèbre le Porteur de l\'Aube.', 'minecraft:entity.firework_rocket.twinkle'),
    k(210, (-90, 98, 0), (0, 70, 0), None, 'Ombrelune, une aventure NeoMC. Merci d\'avoir joué !'),
    k(280, (-30, 80, 20), (0, 68, 0), None, 'Contrats, donjons, grimoire et trésors t\'attendent encore.'),
    k(320, (-30, 80, 20), (0, 68, 0), None, None),
])


def catmull(p0, p1, p2, p3, f):
    f2, f3 = f * f, f * f * f
    return tuple(0.5 * (2 * p1[q] + (-p0[q] + p2[q]) * f + (2 * p0[q] - 5 * p1[q] + 4 * p2[q] - p3[q]) * f2 + (-p0[q] + 3 * p1[q] - 3 * p2[q] + p3[q]) * f3)
                 for q in range(3))


def pose_at(keys, t):
    n = len(keys)
    for i in range(n - 1):
        a_, b_ = keys[i], keys[i + 1]
        if a_['t'] <= t <= b_['t']:
            f = (t - a_['t']) / max(1, b_['t'] - a_['t'])
            k0, k3 = keys[max(0, i - 1)], keys[min(n - 1, i + 2)]
            return catmull(k0['pos'], a_['pos'], b_['pos'], k3['pos'], f), catmull(k0['at'], a_['at'], b_['at'], k3['at'], f)
    return keys[-1]['pos'], keys[-1]['at']


RUN = ['# @s (en cinématique) : tick suivant', 'scoreboard players add @s mg.olctk 1', 'scoreboard players operation $own mg.st = @s mg.olpid']
for name, (cid, end, keys) in C_.items():
    last = keys[-1]['t']
    p0 = keys[0]['pos']
    y0, pit0 = look(p0, keys[0]['at'])
    w(f'{CS}/{name}', [f'# @s commence la cinématique « {name} »', 'execute if entity @s[tag=mg.olcine] run return 0',
                       f'function mg:{P}/save_pos', f'scoreboard players set @s mg.olcs {cid}', 'scoreboard players set @s mg.olctk 0', 'tag @s add mg.olcine',
                       'scoreboard players operation $own mg.st = @s mg.olpid',
                       f'execute in {DIM} run summon minecraft:item_display {g4(p0[0])} {g4(p0[1])} {g4(p0[2])} {{Tags:["mg.ol","mg.olcam","mg.olcamn"],Rotation:[{y0}f,{pit0}f],teleport_duration:2}}',
                       'scoreboard players operation @e[tag=mg.olcamn] mg.olo = $own mg.st', 'tag @e[tag=mg.olcamn] remove mg.olcamn',
                       'gamemode spectator @s', 'title @s times 10 50 10', f'function mg:{P}/{CS}/lock'])
    T = [f'# Cinématique « {name} » : un tick']
    for i, e in enumerate(keys):
        L = [f'# image {i}']
        if e['title']:
            L.append(f'title @s title {js(TEXT(e["title"], "gold", bold=True))}')
            if not e['sub']:
                L.append('title @s subtitle ""')
        if e['sub']:
            L.append(f'title @s subtitle {js(TEXT(e["sub"], "white"))}')
            if not e['title']:
                L.append('title @s title ""')
        if e['sound']:
            L.append(f'execute at @s run playsound {e["sound"]} master @s ~ ~ ~ 1 1')
        L += e['cmds']
        if len(L) > 1:
            w(f'{CS}/{name}/k{i}', L)
            T.append(f'execute if score @s mg.olctk matches {e["t"] + 1} run function mg:{P}/{CS}/{name}/k{i}')
    for b0 in range(0, last + 1, 20):
        Bl = [f'# {name} : ticks {b0 + 1} à {b0 + 20}']
        for t in range(b0, min(last, b0 + 19) + 1):
            pos, at = pose_at(keys, t)
            yw, pt = look(pos, at)
            Bl.append(f'execute if score @s mg.olctk matches {t + 1} run return run execute in {DIM} as @e[tag=mg.olcam] if score @s mg.olo = $own mg.st '
                      f'run tp @s {g4(pos[0])} {g4(pos[1])} {g4(pos[2])} {yw} {pt}')
        w(f'{CS}/{name}/p{b0 // 20}', Bl)
        T.append(f'execute if score @s mg.olctk matches {b0 + 1}..{b0 + 20} run function mg:{P}/{CS}/{name}/p{b0 // 20}')
    T.append(f'execute if score @s mg.olctk matches {last + 2}.. run function mg:{P}/{CS}/end_{end}')
    w(f'{CS}/{name}/t', T)
    RUN.append(f'execute if score @s mg.olcs matches {cid} run return run function mg:{P}/{CS}/{name}/t')
w(f'{CS}/run', RUN)
w(f'{CS}/lock', ['tag @s add mg.olcsme', 'execute as @e[tag=mg.olcam] if score @s mg.olo = $own mg.st run spectate @s @a[tag=mg.olcsme,limit=1]', 'tag @s remove mg.olcsme'])
END = ['scoreboard players operation $own mg.st = @s mg.olpid', 'spectate', 'execute as @e[tag=mg.olcam] if score @s mg.olo = $own mg.st run kill @s',
       'tag @s remove mg.olcine', 'scoreboard players set @s mg.olcs 0', 'gamemode adventure @s', 'title @s clear']
w(f'{CS}/end_back', ['# fin de cinématique : retour à l\'endroit de départ'] + END +
  ['execute store result storage mg:ombre d.x int 1 run scoreboard players get @s mg.olsx', 'execute store result storage mg:ombre d.y int 1 run scoreboard players get @s mg.olsy',
   'execute store result storage mg:ombre d.z int 1 run scoreboard players get @s mg.olsz', f'function mg:{P}/back with storage mg:ombre d'])
w(f'{CS}/end_spawn', ['# fin de cinématique : sur la place de Havreclair'] + END + [f'execute in {DIM} run tp @s 0.5 65 9.5 180 0', f'function mg:{P}/q/say'])
w(f'{CS}/stop', ['# @s quitte Ombrelune pendant une cinématique', 'execute unless entity @s[tag=mg.olcine] run return 0'] + END)

# ---------------------------------------------------------------- indicateur d'objectif (faisceau, flèche, distance)
w('ind', ['# @s (toutes les 10 ticks) : faisceau sur l\'objectif + flèche devant soi (visibles par lui seul), distance',
          'execute store result score $px mg.st run data get entity @s Pos[0]', 'execute store result score $pz mg.st run data get entity @s Pos[2]',
          'scoreboard players operation $px mg.st -= @s mg.olox', 'scoreboard players operation $pz mg.st -= @s mg.oloz',
          'execute if score $px mg.st matches ..-1 run scoreboard players operation $px mg.st *= #m1 mg.st',
          'execute if score $pz mg.st matches ..-1 run scoreboard players operation $pz mg.st *= #m1 mg.st',
          'scoreboard players operation @s mg.olod = $px mg.st', 'scoreboard players operation @s mg.olod > $pz mg.st',
          'scoreboard players operation $mn mg.st = $px mg.st', 'scoreboard players operation $mn mg.st < $pz mg.st',
          'scoreboard players operation $mn mg.st *= #2 mg.st', 'scoreboard players operation $mn mg.st /= #5 mg.st',
          'scoreboard players operation @s mg.olod += $mn mg.st', 'execute if score @s mg.olod matches ..4 run return 0',
          'execute store result storage mg:ombre o.x int 1 run scoreboard players get @s mg.olox', 'execute store result storage mg:ombre o.y int 1 run scoreboard players get @s mg.oloy',
          'execute store result storage mg:ombre o.z int 1 run scoreboard players get @s mg.oloz', f'function mg:{P}/ind_m with storage mg:ombre o'])
w('ind_m', ['$particle minecraft:end_rod $(x).5 $(y).5 $(z).5 0.08 0.6 0.08 0.02 8 force @s',
            '$execute positioned $(x).5 $(y) $(z).5 run particle minecraft:end_rod ~ ~8 ~ 0.08 7 0.08 0 30 force @s',
            '$execute positioned $(x).5 $(y) $(z).5 run particle minecraft:end_rod ~ ~22 ~ 0.08 7 0.08 0 20 force @s',
            '$execute positioned $(x).5 $(y) $(z).5 run particle minecraft:dust{color:[0.75,0.5,1.0],scale:3} ~ ~1 ~ 0.3 0.3 0.3 0 4 force @s',
          ] + [f'$execute anchored eyes positioned ^ ^-0.5 ^ facing $(x) $(y) $(z) positioned ^ ^ ^{d / 2} run particle minecraft:dust{{color:[0.8,0.55,1.0],scale:{max(0.5, 1.3 - d / 40):.2f}}} ~ ~ ~ 0 0 0 0 1 force @s'
               for d in range(4, 33, 2)])   # traînée de 2 à 16 blocs vers l'objectif
