# Bombardier, neo_city.json, carte de Neo GTA, étapes de construction, boom : exécuté par gen_bomber.py (exec), à sa place dans l'ordre d'origine.
# Utilise : AIRFIELD, ARMORY, BANK, C, CMDS, GROUND, HX, NX, NY, NZ, PAL, PLACES, SHOPS, SHOP_NAMES, SHOWROOM, Y0, grid, json,
#   math, os, w.

# ---------------------------------------------------------------- Neo GTA : lieux (tools/arcade/neo_city.json) et carte (police mg:gta_map)
import struct, zlib
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'neo_city.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump({'shops': [[(sx + ex) // 2, sz, nm, col] for (sx, sz, ex, ez), (nm, col) in zip(SHOPS, SHOP_NAMES)],
               'bank': list(BANK), 'armory': list(ARMORY), 'showroom': list(SHOWROOM), 'airfield': list(AIRFIELD), 'places': PLACES},
              f, ensure_ascii=False, indent=1)
    f.write('\n')


def map_color(n, y):
    if n in ('polished_blackstone', 'white_concrete_powder'): return (52, 52, 58)
    if n == 'smooth_stone': return (138, 138, 142)
    if n == 'grass_block': return (86, 146, 64)
    if n in ('dirt_path', 'gray_carpet', 'white_carpet', 'yellow_carpet', 'black_carpet'): return (120, 120, 110)
    if n == 'water': return (58, 110, 196)
    if n == 'sand': return (206, 196, 146)
    if n.endswith('_leaves') or n.endswith('_log') or n == 'mossy_cobblestone': return (52, 112, 46)
    if 'glass' in n: base = (104, 150, 186)
    elif any(k in n for k in ('brick', 'terracotta', 'granite')): base = (162, 92, 72)
    elif any(k in n for k in ('black', 'deepslate', 'gray_concrete')): base = (74, 74, 84)
    else: base = (196, 192, 182)
    f = 0.75 + min(1.0, (y - 65) / 90) * 0.45
    return tuple(min(255, int(c * f)) for c in base)


img = [[(30, 30, 36, 255)] * NX for _ in range(NZ)]
for zz in range(NZ):
    for xx in range(NX):
        for yy in range(NY - 2, -1, -1):
            v = grid[(yy * NZ + zz) * NX + xx]
            if v:
                img[zz][xx] = map_color(PAL[v], yy + Y0) + (255,)
                break


def mark_rect(a, b, c, d, col):
    for zz in range(b, d + 1):
        for xx in range(a, c + 1):
            edge = zz in (b, d) or xx in (a, c)
            img[zz + HX][xx + HX] = (255, 255, 255, 255) if edge else col + (255,)


for _k, _c in (('hospital', (235, 235, 235)), ('police', (40, 70, 200)), ('casino', (250, 215, 40)), ('club', (210, 60, 210))):
    _p = PLACES[_k]
    _x, _z = (_p[0], _p[1] - 2) if isinstance(_p, list) else ((_p['door'][0], _p['door'][1]) if 'door' in _p else ((_p['box'][0] + _p['box'][2]) // 2, _p['box'][1]))
    mark_rect(_x - 4, _z, _x + 4, _z + 6, _c)
mark_rect(*ARMORY, (200, 40, 40)); mark_rect(*BANK, (232, 186, 36)); mark_rect(*SHOWROOM, (150, 70, 200))
for k in range(7):                                  # flèche vers Neo Hills (domaine au nord, en haut de la carte, avenue 20)
    for xx in range(20 - k, 21 + k):
        img[k][xx + HX] = (40, 200, 220, 255)
for (sx, sz, ex, ez) in SHOPS:
    mark_rect((sx + ex) // 2 - 2, sz, (sx + ex) // 2 + 2, sz + 4, (245, 140, 30))
raw = b''.join(b'\0' + b''.join(bytes(px) for px in row) for row in img)
ch = lambda t, d: struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
mp = os.path.join(C.R, 'resourcepack', 'assets', 'mg', 'textures', 'font', 'gta_map.png')
os.makedirs(os.path.dirname(mp), exist_ok=True)
open(mp, 'wb').write(b'\x89PNG\r\n\x1a\n' + ch(b'IHDR', struct.pack('>IIBBBBB', NX, NZ, 8, 6, 0, 0, 0)) + ch(b'IDAT', zlib.compress(raw, 9)) + ch(b'IEND', b''))

# ---------------------------------------------------------------- construction par étapes
NPART = 80
per = math.ceil(len(CMDS) / NPART)
parts = [CMDS[i:i + per] for i in range(0, len(CMDS), per)]
NPART = len(parts)
_bd = os.path.join(C.F, 'bomber', 'b')
if os.path.isdir(_bd):                          # étapes périmées (le nombre d'étapes peut changer)
    for _f in os.listdir(_bd):
        os.remove(os.path.join(_bd, _f))
for i, p in enumerate(parts, 1):
    w(f'bomber/b/p{i}', [f'# Ville du Bombardier, étape {i}/{NPART} (généré par tools/arcade/gen_bomber.py)'] + p)
gper = math.ceil(len(GROUND) / 40)
gparts = [GROUND[i:i + gper] for i in range(0, len(GROUND), gper)]
for i, p in enumerate(gparts, 1):
    w(f'bomber/b/g{i}', [f'# Sol, fleuve et plancher du Bombardier, étape {i}/{len(gparts)}'] + p)
NG = len(gparts)
step = ['# Une étape de construction par tick ($bbs : 1..40 sol si absent, puis la ville). Planifiée par bomber/prepare.',
        'scoreboard players add $bbs mg.st 1']
step += [f'execute if score $bbs mg.st matches {i} run function mg:bomber/b/g{i}' for i in range(1, NG + 1)]
step += [f'execute if score $bbs mg.st matches {NG} run data modify storage mg:bomber v1 set value 1b']
step += [f'execute if score $bbs mg.st matches {NG + i} run function mg:bomber/b/p{i}' for i in range(1, NPART + 1)]
step += [f'execute if score $bbs mg.st matches ..{NG + NPART - 1} run schedule function mg:bomber/build_step 1t']
w('bomber/build_step', step)

# ---------------------------------------------------------------- explosions : sphère de fills
def boom(r):
    L = [f'# Explosion de rayon {r} à la position courante : $bk blocs, $bb blocs bonus détruits',
         'scoreboard players set $bk mg.st 0', 'scoreboard players set $bb mg.st 0']
    for dy in range(-r, r + 1):
        h = int(math.sqrt(r * r - dy * dy) + 0.35)
        k = max(0, round(h * 0.5))
        boxes = [(h, k), (k, h)] if h != k else [(h, h)]
        for (a, b) in boxes:
            for tag, var in (('bomb_bonus', '$bb'), ('bomb_city', '$bk')):
                L.append(f'execute store result score $bt mg.st run fill ~-{a} ~{dy} ~-{b} ~{a} ~{dy} ~{b} minecraft:air replace #mg:{tag}')
                L.append(f'scoreboard players operation {var} mg.st += $bt mg.st')
    return L


for r in (2, 3, 4, 6, 12, 22):   # 4, 6, 12, 22 = Bombardier (rayons doublés) ; 2 et 3 = Neo GTA (roquette, épave)
    w(f'bomber/boom/r{r}', boom(r))
