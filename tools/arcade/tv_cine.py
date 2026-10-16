"""🎬 Terra Nova RPG : cinématiques et indicateur d'objectif. Exécuté par tv_rpg.py (même espace de noms).

Cinématique : le joueur passe en spectateur et regarde à travers une « caméra » (item_display invisible, mg.trcam) qui se
déplace d'image clé en image clé ; teleport_duration = durée jusqu'à l'image suivante, le client interpole (mouvement fluide).
Scores : mg.trcs (n° de la cinématique en cours), mg.trct (tick). Tag mg.trcine pendant la cinématique.
Indicateur : faisceau de lumière sur l'objectif + flèche de particules devant le joueur (visibles par lui seul), distance en m.
"""
import math

CS = f"{P}/cs"


def g4(v):
    return f"{round(v, 4):g}"


def look(frm, to):
    dx, dy, dz = to[0] - frm[0], to[1] - frm[1], to[2] - frm[2]
    return round(-math.degrees(math.atan2(dx, dz)), 1), round(-math.degrees(math.atan2(dy, math.hypot(dx, dz))), 1)


def k(t, pos, at, title=None, sub=None, sound=None, cmds=()):
    return {'t': t, 'pos': pos, 'at': at, 'title': title, 'sub': sub, 'sound': sound, 'cmds': list(cmds)}


hc = lambda x, z: H[(x, z)] + 1 if (x, z) in H else 66
SP = (SPAWN[0], SPAWN[1], SPAWN[2])
lx, ly, lz = LAG_C
cx_, cy_, cz_ = CALD
fx_, fy_, fz_ = FORT_C
CINES = {
    'intro': (1, 'spawn', [
        k(0, (-70, 112, -95), (0, 66, 0), 'TERRA NOVA', '85 millions d\'années avant notre ère…', 'minecraft:block.portal.travel'),
        k(55, (-45, 100, -70), (0, 66, -10), None, 'Une poignée d\'humains a traversé la faille du temps…'),
        k(110, (-18, 86, -58), (0, 66, 0), None, '…pour bâtir une colonie au cœur de la jungle.'),
        k(165, (32, 82, -34), (0, 66, 0), None, 'Mais ce monde appartient aux dinosaures.', 'minecraft:entity.ravager.roar'),
        k(220, (58, 74, 18), (20, 66, 40), None, 'Les slashers chassent en meute, les géants arpentent la vallée…', 'minecraft:entity.fox.screech'),
        k(275, (36, 76, 40), (0, 66, 10), None, 'Au-delà des falaises : marais, plaines, canyons… et le volcan.'),
        k(330, (14, 72, -2), (14, 67, -18), None, 'La Commandante Varga t\'attend au QG.', 'minecraft:block.note_block.bell'),
        k(385, (12, 69, -9), (14, 66, -16), None, None),
        k(420, (12, 69, -9), (14, 66, -16), None, None),
    ]),
    'boss_spino': (6, 'back', [
        k(0, (lx - 24, ly + 6, lz + 20), (lx, ly + 2, lz), 'LA REINE DU MARAIS', 'Spinosaure', 'minecraft:entity.generic.splash',
          [f'particle minecraft:splash {lx} {ly + 1} {lz} 3 1 3 0 200 force @s']),
        k(50, (lx - 14, ly + 3, lz + 12), (lx, ly + 4, lz), None, None, 'minecraft:entity.ravager.roar'),
        k(100, (lx - 10, ly + 2, lz + 8), (lx, ly + 5, lz), None, None),
        k(120, (lx - 10, ly + 2, lz + 8), (lx, ly + 5, lz), None, None),
    ]),
    'boss_varek': (8, 'back', [
        k(0, (fx_ + 6, fy_ + 6, fz_ - 4), (fx_ - 9, fy_ + 2, fz_ + 9), 'LIEUTENANT VAREK', 'Chef des Renégats', 'minecraft:event.raid.horn'),
        k(50, (fx_ - 1, fy_ + 3, fz_ + 3), (fx_ - 9, fy_ + 2, fz_ + 9), None, '« Personne ne repart du fort ! »'),
        k(90, (fx_ - 2, fy_ + 3, fz_ + 4), (fx_ - 9, fy_ + 2, fz_ + 9), None, None),
    ]),
    'boss_rex': (7, 'back', [
        k(0, (cx_ + 10, cy_ + 16, cz_ + 12), (cx_, cy_ + 4, cz_ - 4), None, None, 'minecraft:entity.warden.heartbeat'),
        k(50, (cx_ + 4, cy_ + 3, cz_ + 6), (cx_, cy_ + 6, cz_ - 4), 'LE ROI TYRAN', 'Seigneur du Mont Cendre', 'minecraft:entity.ender_dragon.growl'),
        k(100, (cx_ + 2, cy_ + 1.5, cz_ + 3), (cx_, cy_ + 8, cz_ - 4), None, None, 'minecraft:entity.ravager.roar'),
        k(140, (cx_ + 2, cy_ + 1.5, cz_ + 3), (cx_, cy_ + 8, cz_ - 4), None, None),
    ]),
    'rift': (9, 'spawn', [
        k(0, (RIFT[0] + 0.5, RIFT[1] + 2, RIFT[2] + 6), (RIFT[0] + 0.5, RIFT[1] + 3, RIFT[2]), 'LA FAILLE SE REFERME', None, 'minecraft:block.end_portal.spawn',
          [f'particle minecraft:reverse_portal {RIFT[0] + 0.5} {RIFT[1] + 3} {RIFT[2]} 1 2 0.3 0.3 400 force @s']),
        k(55, (RIFT[0] + 0.5, RIFT[1] + 8, RIFT[2] + 16), (RIFT[0] + 0.5, RIFT[1] + 3, RIFT[2]), None, 'Le temps reprend son cours…',
          None, [f'particle minecraft:flash{{color:[1.0,1.0,1.0,1.0]}} {RIFT[0] + 0.5} {RIFT[1] + 3} {RIFT[2]} 0 0 0 0 1 force @s']),
        k(110, (cx_, cy_ + 40, cz_ + 40), (cx_, cy_, cz_), None, 'Le portail de la colonie est sauvé.', 'minecraft:ui.toast.challenge_complete'),
        k(160, (cx_, cy_ + 40, cz_ + 40), (cx_, cy_, cz_), None, None),
    ]),
    'finale': (10, 'back', [
        k(0, (0, 90, -40), (0, 66, 0), 'HÉROS DE TERRA NOVA', 'La colonie te doit sa survie', 'minecraft:ui.toast.challenge_complete'),
        k(55, (40, 86, 0), (0, 66, 0), None, 'Une campagne NeoMC'),
        k(110, (0, 84, 40), (0, 66, 0), None, 'Bestiaire, œufs d\'ambre, donjons et boss t\'attendent encore…'),
        k(165, (-40, 82, 0), (0, 66, 0), None, 'Merci d\'avoir joué !', 'minecraft:entity.firework_rocket.twinkle'),
        k(200, (-40, 82, 0), (0, 66, 0), None, None),
    ]),
}
PASS_NAMES = {'n': ('LE COL NORD EST OUVERT', 2), 'e': ('LE COL EST EST OUVERT', 3), 'w': ('LE COL OUEST EST OUVERT', 4), 's': ('LE COL SUD EST OUVERT', 5)}
for key, (gx, gz) in PASS_GATE.items():
    ax, c = PASSES[key]
    dx, dz = {'n': (0, -1), 's': (0, 1), 'e': (1, 0), 'w': (-1, 0)}[key]
    gy = hc(gx, gz)
    a = (gx - dx * 14, gy + 9, gz - dz * 14)
    b = (gx + dx * 4, gy + 5, gz + dz * 4)
    far = (gx + dx * 60, gy + 4, gz + dz * 60)
    R = REGIONS[key]
    title, n = PASS_NAMES[key]
    CINES['pass_' + key] = (n, 'back', [
        k(0, a, (gx, gy + 3, gz), title, f'{R["name"]} · niveau conseillé {R["lv"]}', 'minecraft:event.mob_effect.raid_omen'),
        k(55, b, far, None, None),
        k(110, (gx + dx * 20, gy + 7, gz + dz * 20), far, None, None),
        k(130, (gx + dx * 20, gy + 7, gz + dz * 20), far, None, None)])

# ---------------------------------------------------------------- génération : départ, images clés, fin
RUN = ['# @s (en cinématique) : tick suivant, image clé, verrouillage de la caméra', 'scoreboard players add @s mg.trct 1',
       'scoreboard players operation $own mg.st = @s mg.tvpid', 'tag @s add mg.trcsme']
def smooth(t):
    return t * t * (3 - 2 * t)


def catmull(p0, p1, p2, p3, f):
    f2, f3 = f * f, f * f * f
    return tuple(0.5 * (2 * p1[q] + (-p0[q] + p2[q]) * f + (2 * p0[q] - 5 * p1[q] + 4 * p2[q] - p3[q]) * f2 + (-p0[q] + 3 * p1[q] - 3 * p2[q] + p3[q]) * f3)
                 for q in range(3))


def pose_at(keys, t):
    """Position et point visé au tick t : courbe de Catmull-Rom par les images clés (mouvement continu, départ et arrivée doux)."""
    n = len(keys)
    for i in range(n - 1):
        a_, b_ = keys[i], keys[i + 1]
        if a_['t'] <= t <= b_['t']:
            f = (t - a_['t']) / max(1, b_['t'] - a_['t'])
            k0, k3 = keys[max(0, i - 1)], keys[min(n - 1, i + 2)]
            return catmull(k0['pos'], a_['pos'], b_['pos'], k3['pos'], f), catmull(k0['at'], a_['at'], b_['at'], k3['at'], f)
    return keys[-1]['pos'], keys[-1]['at']


for name, (cid, end, keys) in CINES.items():
    last = keys[-1]['t']
    p0 = keys[0]['pos']
    y0, pit0 = look(p0, keys[0]['at'])
    w(f'{CS}/{name}', [f'# @s commence la cinématique « {name} »', 'execute if entity @s[tag=mg.trcine] run return 0',
                       'function mg:terra/save_pos', f'scoreboard players set @s mg.trcs {cid}', 'scoreboard players set @s mg.trct 0', 'tag @s add mg.trcine',
                       'scoreboard players operation $own mg.st = @s mg.tvpid',
                       f'execute in {DIM} run summon minecraft:item_display {p0[0]} {p0[1]} {p0[2]} {{Tags:["mg.tv","mg.trcam","mg.trcamn"],Rotation:[{y0}f,{pit0}f],teleport_duration:2}}',
                       'scoreboard players operation @e[tag=mg.trcamn] mg.tvo = $own mg.st', 'tag @e[tag=mg.trcamn] remove mg.trcamn',
                       'gamemode spectator @s', 'title @s times 10 50 10', f'function mg:{CS}/lock'])
    # textes, sons, effets aux images clés
    T = [f'# Cinématique « {name} » : un tick (pose de la caméra par blocs de 20 ticks, textes aux images clés)']
    for i, e in enumerate(keys):
        L = [f'# image {i} (tick {e["t"]})']
        if e['title']:
            L.append(f'title @s title {js(TEXT(e["title"], "gold", bold=True))}')
            if not e['sub']:
                L.append('title @s subtitle ""')
        if e['sub']:
            L += [f'title @s subtitle {js(TEXT(e["sub"], "white"))}']
            if not e['title']:
                L.append('title @s title ""')
        if e['sound']:
            L.append(f'execute at @s run playsound {e["sound"]} master @s ~ ~ ~ 1 1')
        L += e['cmds']
        if len(L) > 1:
            w(f'{CS}/{name}/k{i}', L)
            T.append(f'execute if score @s mg.trct matches {e["t"] + 1} run function mg:{CS}/{name}/k{i}')
    # pose de la caméra à chaque tick (téléportation douce, durée 2)
    for b0 in range(0, last + 1, 20):
        B = [f'# {name} : ticks {b0 + 1} à {b0 + 20}']
        for t in range(b0, min(last, b0 + 19) + 1):
            pos, at = pose_at(keys, t)
            yw, pt = look(pos, at)
            B.append(f'execute if score @s mg.trct matches {t + 1} run return run execute in {DIM} as @e[tag=mg.trcam] if score @s mg.tvo = $own mg.st '
                     f'run tp @s {g4(pos[0])} {g4(pos[1])} {g4(pos[2])} {yw} {pt}')
        w(f'{CS}/{name}/p{b0 // 20}', B)
        T.append(f'execute if score @s mg.trct matches {b0 + 1}..{b0 + 20} run function mg:{CS}/{name}/p{b0 // 20}')
    T.append(f'execute if score @s mg.trct matches {last + 2}.. run function mg:{CS}/end_{end}')
    w(f'{CS}/{name}/t', T)
    RUN.append(f'execute if score @s mg.trcs matches {cid} run function mg:{CS}/{name}/t')
RUN += ['tag @s remove mg.trcsme']
w(f'{CS}/run', RUN)
w(f'{CS}/lock', ['tag @s add mg.trcsme', 'execute as @e[tag=mg.trcam] if score @s mg.tvo = $own mg.st run spectate @s @a[tag=mg.trcsme,limit=1]'])
END = ['scoreboard players operation $own mg.st = @s mg.tvpid', 'spectate', 'execute as @e[tag=mg.trcam] if score @s mg.tvo = $own mg.st run kill @s',
       'tag @s remove mg.trcine', 'scoreboard players set @s mg.trcs 0', 'gamemode adventure @s', 'title @s clear']
w(f'{CS}/end_back', ['# fin de cinématique : retour à l\'endroit de départ'] + END +
  ['execute store result storage mg:terra d.x int 1 run scoreboard players get @s mg.tvx', 'execute store result storage mg:terra d.y int 1 run scoreboard players get @s mg.tvy',
   'execute store result storage mg:terra d.z int 1 run scoreboard players get @s mg.tvz', f'function mg:{CS}/back with storage mg:terra d'])
w(f'{CS}/back', [f'$execute in {DIM} run tp @s $(x).5 $(y) $(z).5'])
w(f'{CS}/end_spawn', ['# fin de cinématique : sur la place de la colonie'] + END + [f'execute in {DIM} run tp @s {SP[0]} {SP[1]} {SP[2]} 180 0'])
w(f'{CS}/stop', ['# @s quitte Terra Nova pendant une cinématique', 'execute unless entity @s[tag=mg.trcine] run return 0'] + END)

# ---------------------------------------------------------------- indicateur d'objectif (faisceau, flèche, distance)
w(f'{P}/ind', ['# @s (toutes les 10 ticks) : faisceau sur l\'objectif + flèche devant soi (visibles par lui seul), distance',
               'execute store result score $px mg.st run data get entity @s Pos[0]', 'execute store result score $pz mg.st run data get entity @s Pos[2]',
               'scoreboard players operation $px mg.st -= @s mg.trox', 'scoreboard players operation $pz mg.st -= @s mg.troz',
               'execute if score $px mg.st matches ..-1 run scoreboard players operation $px mg.st *= #m1 mg.st',
               'execute if score $pz mg.st matches ..-1 run scoreboard players operation $pz mg.st *= #m1 mg.st',
               '# distance ≈ max + min × 0,4',
               'scoreboard players operation @s mg.trod = $px mg.st', 'scoreboard players operation @s mg.trod > $pz mg.st',
               'scoreboard players operation $mn mg.st = $px mg.st', 'scoreboard players operation $mn mg.st < $pz mg.st',
               'scoreboard players operation $mn mg.st *= #2 mg.st', 'scoreboard players operation $mn mg.st /= #5 mg.st',
               'scoreboard players operation @s mg.trod += $mn mg.st',
               'execute if score @s mg.trod matches ..5 run return 0',
               'execute store result storage mg:terra o.x int 1 run scoreboard players get @s mg.trox',
               'execute store result storage mg:terra o.y int 1 run scoreboard players get @s mg.troy',
               'execute store result storage mg:terra o.z int 1 run scoreboard players get @s mg.troz',
               f'function mg:{P}/ind_m with storage mg:terra o'])
w(f'{P}/ind_m', ['# faisceau (haut de 30 blocs) et flèche (macro : x y z de l\'objectif)',
                 '$particle minecraft:end_rod $(x).5 $(y).5 $(z).5 0.08 0.6 0.08 0.02 8 force @s',
                 '$execute positioned $(x).5 $(y) $(z).5 run particle minecraft:end_rod ~ ~8 ~ 0.08 7 0.08 0 30 force @s',
                 '$execute positioned $(x).5 $(y) $(z).5 run particle minecraft:end_rod ~ ~22 ~ 0.08 7 0.08 0 20 force @s',
                 '$execute positioned $(x).5 $(y) $(z).5 run particle minecraft:dust{color:[1.0,0.85,0.2],scale:3} ~ ~1 ~ 0.3 0.3 0.3 0 4 force @s',
                 '$execute anchored eyes positioned ^ ^-0.5 ^ facing $(x) $(y) $(z) positioned ^ ^ ^2 run particle minecraft:dust{color:[1.0,0.8,0.1],scale:1.2} ~ ~ ~ 0 0 0 0 1 force @s',
                 '$execute anchored eyes positioned ^ ^-0.5 ^ facing $(x) $(y) $(z) positioned ^ ^ ^2.6 run particle minecraft:dust{color:[1.0,0.8,0.1],scale:1.0} ~ ~ ~ 0 0 0 0 1 force @s',
                 '$execute anchored eyes positioned ^ ^-0.5 ^ facing $(x) $(y) $(z) positioned ^ ^ ^3.2 run particle minecraft:dust{color:[1.0,0.8,0.1],scale:0.8} ~ ~ ~ 0 0 0 0 1 force @s',
                 '$execute anchored eyes positioned ^ ^-0.5 ^ facing $(x) $(y) $(z) positioned ^0.25 ^ ^2.9 run particle minecraft:dust{color:[1.0,0.8,0.1],scale:0.7} ~ ~ ~ 0 0 0 0 1 force @s',
                 '$execute anchored eyes positioned ^ ^-0.5 ^ facing $(x) $(y) $(z) positioned ^-0.25 ^ ^2.9 run particle minecraft:dust{color:[1.0,0.8,0.1],scale:0.7} ~ ~ ~ 0 0 0 0 1 force @s'])
