"""Génère le spawn (grande île flottante détaillée) : python tools/lobby/gen_lobby.py <racine du dépôt> [aperçu.png]

Île de ~70 blocs de rayon centrée sur 0 64 0 (sol en y = 63), entourée par les 15 plots (jamais touchés : chaque bloc posé est vérifié).
  - centre : rose des vents dorée (point d'apparition), douves avec jets d'eau, grande place pavée ;
  - ouest : l'Armurerie (château à toit de chêne noir, 4 socles d'armes) et le Stand de tir (cibles : le laser y marque les points) ;
  - est : porte du Parkour, puis le parcours au-dessus du vide jusqu'à la Tour céleste (spirale, 3 checkpoints, balise au sommet) ;
  - nord : le Portail des plots (on le traverse pour aller sur son plot) ;
  - sud : le Garage Kart (piste, podium, tuyaux) ;
  - quatre jardins (cerisiers et étang, champignons géants, parc et fontaine, bambous et lanternes), promenade circulaire,
    ponts vers chaque plot, cascades, petites îles volantes ; dessous de l'île en roche avec racines, lichen lumineux et lianes.
Les modèles du resource pack (logo, panneaux, armes, karts, boîtes ?, trophée, cristaux, ballons) sont posés si $rp = 1, sinon des
équivalents vanilla.
Sorties : data/mg/function/lobby/ (build*, deco*, anim, fx, armory_*, pads, laser_hit, portal) et parkour/ (build, fall_check, fall, board_refresh).
"""
import math, os, random, re, sys

R = sys.argv[1]
F = os.path.join(R, 'data', 'mg', 'function')
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lib'))
import mcfn
G = 63
rnd = random.Random(20261007)

# ------------------------------------------------------------------ plots (lus dans plot/build_all : murs = zone interdite)
PLOTS = []
for l in open(os.path.join(F, 'plot', 'build_all.mcfunction'), encoding='utf-8'):
    m = re.search(r'\{n:(\d+),lx:([-\d.]+),lz:([-\d.]+),wx1:(-?\d+),wx2:(-?\d+),wz1:(-?\d+),wz2:(-?\d+)', l)
    if m: PLOTS.append((int(m[1]), float(m[2]), float(m[3])) + tuple(int(v) for v in m.groups()[3:]))
assert len(PLOTS) == 15
def inplot(x, z, mg=0): return any(a - mg <= x <= b + mg and c - mg <= z <= d + mg for _, _, _, a, b, c, d in PLOTS)

W = {}
def put(x, y, z, b):
    assert not inplot(x, z), ('plot !', x, y, z, b)
    W[(x, y, z)] = b
def setif(x, y, z, b):
    if (x, y, z) not in W and not inplot(x, z): W[(x, y, z)] = b
def box(x1, y1, z1, x2, y2, z2, b):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            for z in range(min(z1, z2), max(z1, z2) + 1): put(x, y, z, b)
def get(x, y, z): return W.get((x, y, z))

def h2(i, j, s):
    n = (i * 374761393 + j * 668265263 + s * 2246822519) & 0xffffffff
    n = ((n ^ (n >> 13)) * 1274126177) & 0xffffffff
    return ((n ^ (n >> 16)) & 0xffff) / 65535
def vn(x, z, sc, s):
    fx, fz = x / sc, z / sc
    i, j = math.floor(fx), math.floor(fz)
    tx, tz = fx - i, fz - j
    tx, tz = tx * tx * (3 - 2 * tx), tz * tz * (3 - 2 * tz)
    a, b, c, d = h2(i, j, s), h2(i + 1, j, s), h2(i, j + 1, s), h2(i + 1, j + 1, s)
    return a + (b - a) * tx + (c - a) * tz + (a - b - c + d) * tx * tz

LEAF = lambda t: f'{t}_leaves[persistent=true]'
FLOWERS = ['poppy', 'dandelion', 'cornflower', 'allium', 'azure_bluet', 'oxeye_daisy', 'red_tulip', 'orange_tulip', 'white_tulip', 'pink_tulip',
           'lily_of_the_valley', 'blue_orchid']

# ------------------------------------------------------------------ île : contour, dessus, dessous
def edge(x, z):
    t = math.atan2(z, x)
    return 71 + 1.6 * math.sin(5 * t + 0.7) + 1.2 * math.sin(11 * t + 2.1) + 0.6 * math.sin(23 * t)
ISL = [(x, z) for x in range(-77, 78) for z in range(-77, 78) if math.hypot(x, z) <= edge(x, z)]
ISET = set(ISL)
for (x, z) in ISL: assert not inplot(x, z, 2), ('île trop près d\'un plot', x, z)

TOP = {p: 'grass_block' for p in ISL}
MASK = {p: 'g' for p in ISL}
def paint(x, z, b, m='p'):
    if (x, z) in TOP: TOP[(x, z)] = b; MASK[(x, z)] = m

BOT = {}
for (x, z) in ISL:
    r = math.hypot(x, z); t = min(1.0, r / edge(x, z))
    depth = 6 + 34 * (1 - t * t) ** 0.75 * (0.65 + 0.7 * vn(x, z, 9, 1)) + 4 * vn(x, z, 3.5, 2)
    BOT[(x, z)] = int(G - 1 - depth)
# pointes rocheuses sous l'île
for k in range(9):
    a = rnd.uniform(0, 2 * math.pi); rr = rnd.uniform(0, 34); sx, sz = int(rr * math.cos(a)), int(rr * math.sin(a))
    L, rad = rnd.randint(8, 16), rnd.uniform(2.5, 4.5)
    for (x, z) in ISL:
        d = math.hypot(x - sx, z - sz)
        if d < rad: BOT[(x, z)] = min(BOT[(x, z)], int(BOT[(sx, sz)] - L * (1 - d / rad)))

def shell(x, y, z):
    n = vn(x + y * 3, z - y * 2, 6, 3)
    if y >= 59: return 'dirt' if n < 0.55 else ('coarse_dirt' if n < 0.8 else 'rooted_dirt')
    if y >= 50: return 'stone' if n < 0.45 else ('andesite' if n < 0.7 else ('mossy_cobblestone' if n < 0.85 else 'cobblestone'))
    if y >= 38: return 'stone' if n < 0.4 else ('tuff' if n < 0.65 else ('andesite' if n < 0.85 else 'calcite'))
    return 'deepslate' if n < 0.5 else ('tuff' if n < 0.75 else 'cobbled_deepslate')
ORES = {True: ['coal_ore', 'iron_ore', 'copper_ore', 'gold_ore', 'lapis_ore'], False: ['deepslate_coal_ore', 'deepslate_iron_ore', 'deepslate_diamond_ore',
                                                                                        'deepslate_redstone_ore', 'deepslate_emerald_ore']}
for (x, z) in ISL:
    b0 = BOT[(x, z)]
    nb = [BOT.get((x + dx, z + dz), 999) for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1))]
    for y in range(b0, G):
        exposed = y == b0 or any(v > y for v in nb)
        if not exposed: put(x, y, z, 'dirt' if y >= 59 else 'stone')
        elif y == b0 and y < 57 and rnd.random() < 0.05: put(x, y, z, rnd.choice(ORES[y >= 38]))
        else: put(x, y, z, shell(x, y, z))
    # sous la roche : racines, lichen lumineux, pointes, fleurs suspendues
    u = rnd.random()
    if b0 >= 55 and u < 0.12: put(x, b0 - 1, z, 'hanging_roots')
    elif u < 0.07: put(x, b0 - 1, z, 'glow_lichen[up=true]')
    elif u < 0.10: put(x, b0 - 1, z, 'pointed_dripstone[vertical_direction=down,thickness=tip]')
    elif u < 0.108: put(x, b0 - 1, z, 'spore_blossom')
# lianes sur le pourtour
for (x, z) in ISL:
    for dx, dz, face in ((1, 0, 'west'), (-1, 0, 'east'), (0, 1, 'north'), (0, -1, 'south')):
        nx, nz = x + dx, z + dz
        if (nx, nz) in ISET or rnd.random() > 0.22 or inplot(nx, nz): continue
        for y in range(G - 1, G - 1 - rnd.randint(2, 9), -1):
            if y < BOT[(x, z)]: break
            setif(nx, y, nz, f'vine[{face}=true]')

# ------------------------------------------------------------------ helpers de déco
def lamp(x, z, kind='blackstone', top='lantern'):
    wall = {'blackstone': 'polished_blackstone_wall', 'stone': 'stone_brick_wall', 'andesite': 'andesite_wall'}[kind]
    base = {'blackstone': 'chiseled_polished_blackstone', 'stone': 'chiseled_stone_bricks', 'andesite': 'polished_andesite'}[kind]
    put(x, 64, z, base); put(x, 65, z, wall); put(x, 66, z, wall); put(x, 67, z, wall); put(x, 68, z, top)
def bench(cells, facing):
    for (x, z) in cells: put(x, 64, z, f'spruce_stairs[facing={facing}]')
def hedge(x, z):
    if get(x, 64, z) is None: put(x, 64, z, 'flowering_azalea_leaves[persistent=true]' if rnd.random() < 0.3 else 'azalea_leaves[persistent=true]')
def disc(cx, cz, r):
    return [(x, z) for x in range(int(cx - r) - 1, int(cx + r) + 2) for z in range(int(cz - r) - 1, int(cz + r) + 2) if math.hypot(x - cx, z - cz) <= r]
def facing_of(dx, dz):
    if abs(dx) >= abs(dz): return 'east' if dx > 0 else 'west'
    return 'south' if dz > 0 else 'north'

PETALS = True
JETS = []   # sources d'eau posées sans « strict » à la fin (elles coulent)

# Promenade, place, avenues, armurerie, stand, portails, garage, jardins et ponts (spawn_plaza.py)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spawn_plaza.py'), encoding='utf-8').read())

# Circuit du spawn (kart libre) : spline, tangentes, points de passage (spawn_track.py)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spawn_track.py'), encoding='utf-8').read())

# Décor secret, sommet, arbres, îlots, parkour et éclairage des chemins (spawn_nature.py)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spawn_nature.py'), encoding='utf-8').read())

# ------------------------------------------------------------------ émission des commandes
def is_conn(b):
    n = b.split('[')[0]
    return n.endswith('_fence') or n.endswith('_wall') or n.endswith('_pane') or n == 'iron_bars'
def rects(cells):
    rows = {}
    for (x, z), b in cells.items(): rows.setdefault(x, []).append((z, b))
    out, active = [], {}
    for x in sorted(rows):
        lst = sorted(rows[x]); runs = []
        for z, b in lst:
            if runs and runs[-1][2] == b and runs[-1][1] == z - 1: runs[-1][1] = z
            else: runs.append([z, z, b])
        new = {}
        for z1, z2, b in runs:
            k = (z1, z2, b)
            if k in active and active[k][1] == x - 1: v = active.pop(k); v[1] = x; new[k] = v
            else: new[k] = [x, x]
        for k, v in active.items(): out.append((v[0], v[1], k[0], k[1], k[2]))
        active = new
    for k, v in active.items(): out.append((v[0], v[1], k[0], k[1], k[2]))
    return out
def merge(cells, suffix):
    layers = {}
    for (x, y, z), b in cells.items(): layers.setdefault(y, {})[(x, z)] = b
    boxes, active = [], {}
    for y in sorted(layers):
        new = {}
        for r in rects(layers[y]):
            if r in active and active[r][1] == y - 1: v = active.pop(r); v[1] = y; new[r] = v
            else: new[r] = [y, y]
        for r, v in active.items(): boxes.append((r, v[0], v[1]))
        active = new
    for r, v in active.items(): boxes.append((r, v[0], v[1]))
    boxes.sort(key=lambda t: (t[1], t[0][0], t[0][2]))
    cmds = []
    for (x1, x2, z1, z2, b), y1, y2 in boxes:
        ys = y1
        step = max(1, 32768 // ((x2 - x1 + 1) * (z2 - z1 + 1)))
        while ys <= y2:
            ye = min(y2, ys + step - 1)
            if x1 == x2 and z1 == z2 and ys == ye: cmds.append(f'setblock {x1} {ys} {z1} minecraft:{b}{suffix}')
            else: cmds.append(f'fill {x1} {ys} {z1} {x2} {ye} {z2} minecraft:{b}{suffix}')
            ys = ye + 1
    return cmds

clear = []
xs = {}
for x in range(-77, 78):
    zz = [z for z in range(-77, 78) if math.hypot(x, z) <= 76.5]
    if zz: clear.append(f'fill {x} 64 {min(zz)} {x} 122 {max(zz)} minecraft:air strict')
clear.append('fill 18 63 -8 125 80 6 minecraft:air strict')        # ancien parkour
for (x, z) in ISL: assert not inplot(x, z)
strict = {k: v for k, v in W.items() if not is_conn(v)}
conn = {k: v for k, v in W.items() if is_conn(v)}
CMDS = clear + merge(strict, ' strict') + merge(conn, '')
print('blocs', len(W), '| commandes', len(CMDS), '| arbres', len(TREES))

wr = mcfn.Fn(F).write

old = [f for f in os.listdir(os.path.join(F, 'lobby')) if re.match(r'build_\d+\.mcfunction$', f)]
for f in old: os.remove(os.path.join(F, 'lobby', f))
PART = 3000
parts = [CMDS[i:i + PART] for i in range(0, len(CMDS), PART)]
for i, p in enumerate(parts, 1):
    nxt = f'mg:lobby/build_{i + 1}' if i < len(parts) else 'mg:lobby/build_end'
    wr(f'lobby/build_{i}', [f'# Spawn, partie {i}/{len(parts)} (généré par tools/lobby/gen_lobby.py)'] + p + [f'schedule function {nxt} 1t'])
wr('lobby/build', ['# Spawn : grande île flottante (générée par tools/lobby/gen_lobby.py), construite en plusieurs ticks',
                   'kill @e[type=minecraft:text_display,tag=mg.deco]',
                   'forceload add -80 -80 80 80', 'forceload add 81 -32 144 32', 'forceload add -115 81 115 225',
                   'tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Construction du spawn (quelques secondes)...","color":"gray"}]',
                   'schedule function mg:lobby/build_1 5s'])
wr('lobby/build_end', ['# Fin de la construction du spawn : eau qui coule, décor, chargement des zones'] +
   [f'setblock {x} {y} {z} minecraft:water' for (x, y, z) in JETS] +
   ['function mg:lobby/deco', 'function mg:lobby/armory_build', 'function mg:parkour/build',
    'forceload remove -80 -80 80 80', 'forceload remove 81 -32 144 32', 'forceload remove -115 81 115 225', 'function mg:core/forceloads', 'data modify storage mg:lobby v6 set value 1b',
    'tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Spawn construit.","color":"green"}]'])

# Entités de décor, tick de l'armurerie et fonctions du parkour (spawn_deco.py)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spawn_deco.py'), encoding='utf-8').read())

# Circuit du spawn : tables du moteur kart (t4) et mode kart libre (lobkart) (spawn_kart.py)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spawn_kart.py'), encoding='utf-8').read())

# Succès cachés du spawn, détection et terrier secret (spawn_secrets.py)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spawn_secrets.py'), encoding='utf-8').read())

# ------------------------------------------------------------------ aperçu (vue de dessus)
if len(sys.argv) > 2:
    import struct, zlib
    COL = {'grass': (92, 160, 60), 'water': (50, 110, 220), 'leaves': (60, 130, 50), 'cherry_leaves': (240, 170, 200), 'stone_brick': (130, 130, 130),
           'andesite': (150, 150, 150), 'diorite': (215, 215, 215), 'quartz': (235, 230, 225), 'gold': (250, 210, 60), 'blackstone': (50, 45, 50),
           'deepslate': (80, 80, 88), 'dark_oak': (70, 50, 30), 'spruce': (110, 80, 50), 'concrete': None, 'purpur': (170, 120, 170), 'obsidian': (30, 20, 50),
           'amethyst': (150, 100, 210), 'dirt_path': (160, 130, 80), 'mud': (140, 110, 90), 'mushroom': (200, 40, 40), 'bamboo': (120, 170, 60),
           'birch': (215, 210, 190), 'log': (100, 75, 45), 'lapis': (40, 70, 180), 'emerald': (40, 200, 90), 'ice': (160, 200, 250), 'snow': (245, 250, 255),
           'nether': (130, 40, 40), 'end_stone': (225, 225, 170), 'calcite': (225, 225, 225), 'diamond': (100, 230, 230)}
    CC = {'red': (190, 40, 40), 'white': (235, 235, 235), 'black': (25, 25, 30), 'gray': (80, 80, 85), 'light_gray': (150, 150, 150), 'green': (70, 110, 30),
          'lime': (110, 190, 30), 'yellow': (240, 200, 40), 'cyan': (30, 140, 150)}
    def col(b):
        n = b.split('[')[0]
        if n.endswith('_concrete') or n.endswith('_wool'):
            return CC.get(n.rsplit('_', 1)[0], (150, 150, 150))
        for k, v in COL.items():
            if k in n and v: return v
        h = sum(ord(c) * (i + 1) for i, c in enumerate(n))
        return (90 + h % 120, 90 + (h // 7) % 120, 90 + (h // 49) % 120)
    X0, X1_, Z0, Z1_ = -115, 140, -80, 225
    S = 3
    hm = {}
    for (x, y, z), b in W.items():
        if b.startswith('light') or b == 'air': continue
        if (x, z) not in hm or y > hm[(x, z)][0]: hm[(x, z)] = (y, b)
    w, h = (X1_ - X0 + 1) * S, (Z1_ - Z0 + 1) * S
    img = [[(18, 22, 40)] * w for _ in range(h)]
    for (x, z), (y, b) in hm.items():
        if not (X0 <= x <= X1_ and Z0 <= z <= Z1_): continue
        c = col(b); f = max(0.55, min(1.35, 0.8 + (y - 63) * 0.025))
        c = tuple(min(255, int(v * f)) for v in c)
        for dy in range(S):
            for dx in range(S): img[(z - Z0) * S + dy][(x - X0) * S + dx] = c
    for (_, _, _, a, b, c2, d) in PLOTS:
        for x in range(a, b + 1):
            for z in range(c2, d + 1):
                if X0 <= x <= X1_ and Z0 <= z <= Z1_ and (x in (a, b) or z in (c2, d)):
                    for dy in range(S):
                        for dx in range(S): img[(z - Z0) * S + dy][(x - X0) * S + dx] = (255, 60, 60)
    raw = b''.join(b'\0' + b''.join(bytes(p) for p in r) for r in img)
    def ch(t, dd): return struct.pack('>I', len(dd)) + t + dd + struct.pack('>I', zlib.crc32(t + dd) & 0xffffffff)
    open(sys.argv[2], 'wb').write(b'\x89PNG\r\n\x1a\n' + ch(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0)) + ch(b'IDAT', zlib.compress(raw)) + ch(b'IEND', b''))
    print('aperçu :', sys.argv[2])

# panneaux du spawn à orientation fixe : décor recréé une fois sur les mondes existants (témoin mg:lobby deco3)
def _patch(rel, anchor, line):
    pth = os.path.join(R, 'data/mg/function', rel + '.mcfunction'); t = open(pth, encoding='utf-8').read()
    if line in t: return
    assert anchor in t, (rel, anchor)
    open(pth, 'w', encoding='utf-8', newline='\n').write(t.replace(anchor, anchor + '\n' + line, 1))
_patch('core/load', 'execute unless score $rp mg.st matches 0.. run function mg:core/rp_default',
       'execute if score $setup mg.st matches 1 unless data storage mg:lobby deco3 run schedule function mg:lobby/deco 6s')
_patch('desinstaller', 'data remove storage mg:lobby beacon1', 'data remove storage mg:lobby deco3\ndata remove storage mg:lobby deco2')
