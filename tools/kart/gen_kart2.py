"""Génère le circuit 2 du kart, le Royaume Koopa : python gen_kart2.py ../../data/mg [apercu.png]

Île à z 19000 (401 x 301 blocs). Tour d'environ 1,5 km : départ en ville (tribunes, maisons Toad), Plage Koopa (lagune,
Cheep Cheep qui sautent, saut au-dessus d'un bras de mer), jungle (pont de bois, plantes Piranha, Goombas), désert
(pyramide traversée par un tunnel, Pokeys, sables mouvants), montée vers le château de Bowser (Thwomps, barres de feu,
Podoboos, canaux de lave), pont au-dessus de la lave avec un Chomp, descente et grand saut au-dessus d'une douve de lave.

Sortie : data/mg/function/kart/t2/*.mcfunction (le moteur appelle ces tables via les fonctions d'aiguillage de kart/).
"""
import math, os, random, sys, zlib, struct

OUT = os.path.join(sys.argv[1], 'function', 'kart', 't2')
os.makedirs(OUT, exist_ok=True)
PF = 'mg:kart/t2/'
ZC = 19000
HX, HZ = 250, 185
YB, ROAD, SEA = 40, 64, 62
HW = 6.5
WALLD = HW + 1.2
random.seed(62)

def W(z): return ZC + z

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kart2_track_part.py'), encoding='utf-8').read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kart2_terrain_part.py'), encoding='utf-8').read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kart2_deco_part.py'), encoding='utf-8').read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kart2_places_part.py'), encoding='utf-8').read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kart2_hazards_part.py'), encoding='utf-8').read())

# ------------------------------------------------------------------ tables de jeu
K = int(LENGTH / 10)
CPS = []
for k in range(K):
    i = int(k * NP / K)
    for g in (GAPL, GAPW):
        if abs(sdist(g, i)) <= GAPH + 2: i = (g + int((GAPH + 4) * 2)) % NP
    x, z = pts[i]; tx, tz = tangent(i)
    CPS.append((round(x, 1), RY(i) + 1, round(z, 1), yaw_of(tx, tz)))

def write(name, lines):
    with open(os.path.join(OUT, name + '.mcfunction'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')

write('cp_check', [f'# Royaume Koopa : point de passage attendu (mg.kcp) atteint ? ({K} points par tour)'] +
      [f'execute if score @s mg.kcp matches {k} positioned {x} {y} {W(0) + z} if entity @e[type=minecraft:block_display,tag=mg.kk,distance=..9] run return run function mg:kart/cp_pass'
       for k, (x, y, z, yw) in enumerate(CPS)])
write('cp_tp', ['# Royaume Koopa : remise en piste (@s = kart) au point de passage $ki'] +
      [f'execute if score $ki mg.st matches {k} run return run tp @s {x} {y} {W(0) + z} {yw} 0' for k, (x, y, z, yw) in enumerate(CPS)])
write('bill_step', ['# Royaume Koopa : Bill Balle (@s = kart) file vers le point de passage $ki (suit les montées)'] +
      [f'execute if score $ki mg.st matches {k} facing {x} {y} {W(0) + z} run return run tp @s ^ ^ ^1.6 ~ 0' for k, (x, y, z, yw) in enumerate(CPS)])
sx, sz, tx, tz, nx, nz, ry = frame(START)
yaw0 = yaw_of(tx, tz)
grid = ['# Royaume Koopa : place le kart @s sur la grille (n° $gi, 1..16)']
for g in range(16):
    row, colm = g // 2, g % 2
    back = 4 + row * 4
    side = -2.5 if colm == 0 else 2.5
    x, z = sx - tx * back + nx * side, sz - tz * back + nz * side
    grid.append(f'execute if score $gi mg.st matches {g + 1} run return run tp @s {round(x, 1)} {ry + 1} {round(W(0) + z, 1)} {yaw0} 0')
write('grid_tp', grid)
gate_on, gate_off = ['# Portillon de départ fermé'], ['# Portillon ouvert']
for b in range(-6, 7):
    x, z = round(sx - tx * 1.5 + nx * b), round(sz - tz * 1.5 + nz * b)
    gate_on.append(f'fill {x} {ry + 1} {W(z)} {x} {ry + 2} {W(z)} minecraft:barrier')
    gate_off.append(f'fill {x} {ry + 1} {W(z)} {x} {ry + 2} {W(z)} minecraft:air')
write('gate_on', gate_on); write('gate_off', gate_off)
boxes = ['# Royaume Koopa : boîtes à objets (6 rangées de 5)', 'kill @e[type=minecraft:item_display,tag=mg.kbox]', 'kill @e[type=minecraft:text_display,tag=mg.kboxq]']
for i in ITEMROWS:
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    for b in (-3.6, -1.8, 0, 1.8, 3.6):
        x, z = cx + nx2 * b, cz + nz2 * b
        boxes.append(f'summon minecraft:item_display {round(x, 1)} {ry2 + 2} {round(W(0) + z, 1)} {{Tags:["mg.kbox","mg.kspin","mg.fx"],item:{{id:"minecraft:yellow_stained_glass"}},'
                     f'transformation:{{translation:[0f,0f,0f],{T0},scale:[1.1f,1.1f,1.1f]}},interpolation_duration:10}}')
        boxes.append(f'summon minecraft:text_display {round(x, 1)} {ry2 + 1.7} {round(W(0) + z, 1)} {{Tags:["mg.kboxq","mg.fx"],billboard:"center",text:[{{"text":"?","color":"gold","bold":true}}],background:0,'
                     f'transformation:{{translation:[0f,0f,0f],{T0},scale:[1.5f,1.5f,1.5f]}}}}')
write('boxes', boxes)
write('hazards', spawn)
write('track_tick', tick)
write('hz_hit', ['# @s = kart touché par un danger : son pilote part en tête-à-queue (sauf s\'il tourne déjà)',
                 'scoreboard players operation $ko mg.st = @s mg.ri',
                 'execute as @a[tag=mg.play] if score @s mg.ri = $ko mg.st unless score @s mg.khi matches 1.. run function mg:kart/hit'])
write('hz_big', ['# @s = kart écrasé (Thwomp, Chomp) : grand tête-à-queue',
                 'scoreboard players operation $ko mg.st = @s mg.ri',
                 'execute as @a[tag=mg.play] if score @s mg.ri = $ko mg.st unless score @s mg.khi matches 1.. run function mg:kart/hit_big'])
write('goo_squash', ['# Goomba (@s) percuté : le kart part en tête-à-queue, le Goomba est aplati 5 s',
                     f'execute as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.4] run function {PF}hz_hit',
                     'tag @s add mg.kdead', 'scoreboard players set @s mg.t 100',
                     'data merge entity @s {start_interpolation:0,interpolation_duration:3,transformation:{scale:[1.4f,0.25f,1.4f]}}',
                     'playsound minecraft:entity.slime.squish master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 1.4'])
write('goo_wait', ['scoreboard players remove @s mg.t 1', 'execute if score @s mg.t matches 1.. run return 0', 'tag @s remove mg.kdead',
                   'data merge entity @s {start_interpolation:0,interpolation_duration:6,transformation:{scale:[1.2f,1.2f,1.2f]}}'])

HXF = [(-HX, -126), (-125, -1), (0, 124), (125, HX)]
write('fl_add', ['# Royaume Koopa : zone chargée (4 bandes, forceload limité à 256 chunks par commande)'] +
      [f'forceload add {a} {W(-HZ)} {b} {W(HZ)}' for a, b in HXF])
write('fl_remove', ['# Royaume Koopa : zone libérée, puis zones permanentes rétablies'] +
      [f'forceload remove {a} {W(-HZ)} {b} {W(HZ)}' for a, b in HXF] + ['function mg:core/forceloads'])

clear = ['# Royaume Koopa : nettoyage de la zone']
for x in range(-HX, HX + 1, 16):
    for z in range(-HZ, HZ + 1, 16):
        clear.append(f'fill {x} {YB} {W(z)} {min(x + 15, HX)} {ROAD + 56} {W(min(z + 15, HZ))} minecraft:air')
q4 = (len(clear) + 3) // 4
parts = [clear[k:k + q4] for k in range(0, len(clear), q4)]
CH = 3000
for i in range(0, len(terrain), CH):
    parts.append(['# Royaume Koopa : terrain'] + terrain[i:i + CH])
allb = struct_ + TUNNEL + walls + castle + deco
for i in range(0, len(allb), CH):
    parts.append(['# Royaume Koopa : décor'] + allb[i:i + CH])
parts.append(['# Royaume Koopa : fin', f'function {PF}fl_remove', 'data modify storage mg:kart built2 set value 1b',
              'execute unless data storage mg:kart built3 run schedule function mg:kart/t3/build 3s',
              'tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Circuit Royaume Koopa construit.","color":"green"}]'])
write('build', ['# (OP) Construit le Royaume Koopa : zone chargée, puis construction dès que tous ses chunks sont prêts',
                f'function {PF}fl_add', 'scoreboard players set $kbw2 mg.st 0', f'schedule function {PF}build_wait 20t'])
write('build_wait', ['# Attend que toute la zone soit chargée et générée (5 min au plus), puis construit',
                     f'execute if function {PF}loaded_all run return run function {PF}build_1',
                     'scoreboard players add $kbw2 mg.st 1',
                     'execute if score $kbw2 mg.st matches 300.. run return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Royaume Koopa : zone toujours pas chargée, construction annulée.","color":"red"}]',
                     f'schedule function {PF}build_wait 20t'])
lo = ['# Vrai si toute la zone du Royaume Koopa est chargée']
for x in list(range(-HX, HX + 1, 32)) + [HX]:
    for z in list(range(-HZ, HZ + 1, 32)) + [HZ]:
        lo.append(f'execute store success score $kld mg.st unless block {x} {ROAD} {W(z)} minecraft:bedrock')
        lo.append('execute if score $kld mg.st matches 0 run return fail')
lo.append('return 1')
write('loaded_all', lo)
for k, p in enumerate(parts, 1):
    if k < len(parts): p = p + [f'schedule function {PF}build_{k + 1} 2t']
    write(f'build_{k}', p)
for f in os.listdir(OUT):
    if f.startswith('build_') and f[6:-11].isdigit() and int(f[6:-11]) > len(parts): os.remove(os.path.join(OUT, f))

# seules les constantes #km* restent, pour la parité avec data/, lues par rien
MMC, MMR = 24, 15
write('const', ['# Constantes du Royaume Koopa (générées)', f'scoreboard players set $kK mg.st {K}', 'scoreboard players set $kLaps mg.st 3',
                f'scoreboard players set #kmx0 mg.st {HX}', f'scoreboard players set #kmz0 mg.st {ZC - HZ}', f'scoreboard players set #kmc mg.st {MMC}',
                f'scoreboard players set #kmw mg.st {2 * HX + 1}', f'scoreboard players set #kmr mg.st {MMR}', f'scoreboard players set #kmh mg.st {2 * HZ + 1}'] +
      [f'scoreboard players set #h{T} mg.st {T}' for T in sorted(consts)])
write('perch', ['# Perchoir des spectateurs du Royaume Koopa (kart/perch, appelé par kart/prepare)',
                'scoreboard players set $px mg.st 0', f'scoreboard players set $py mg.st {ROAD + 50}', f'scoreboard players set $pz mg.st {ZC}'])
print('points de passage', K, '| terrain', len(terrain), '| décor', len(allb), '| étapes', len(parts), '| dangers', HID[0], '| lignes tick', len(tick), '| entités', len(spawn))

# ------------------------------------------------------------------ aperçu PNG
if len(sys.argv) > 2:
    w, hgt, sc = (2 * HX + 1), (2 * HZ + 1), 3
    px = bytearray(w * sc * hgt * sc * 3)
    def rect(x1, y1, x2, y2, rgb):
        for yy in range(max(0, y1), min(hgt * sc, y2 + 1)):
            for xx in range(max(0, x1), min(w * sc, x2 + 1)):
                k = (yy * w * sc + xx) * 3; px[k:k + 3] = bytes(rgb)
    COL = {'grass_block': (95, 160, 60), 'moss_block': (80, 140, 50), 'podzol': (110, 80, 40), 'sand': (225, 210, 150), 'red_sand': (200, 110, 50),
           'stone': (125, 125, 125), 'snow_block': (245, 250, 255), 'blackstone': (45, 40, 50), 'basalt': (70, 70, 75), 'magma_block': (160, 70, 20),
           'black_concrete': (20, 20, 20), 'white_concrete': (235, 235, 235), 'orange_glazed_terracotta': (240, 140, 20), 'lime_concrete': (120, 220, 40),
           'soul_sand': (90, 70, 50), 'spruce_planks': (120, 85, 50), 'nether_bricks': (60, 30, 35)}
    for (x, z), c in col.items():
        if c['liq'] == 'water': rgb = (40, 110, 200)
        elif c['liq'] == 'lava': rgb = (230, 90, 10)
        elif (x, z) in ROADSET: rgb = COL.get(c['top'], (90, 90, 95))
        else: rgb = COL.get(c['top'], (150, 150, 150))
        if c['wall']: rgb = (120, 60, 30)
        if c.get('roof') and (x, z) not in ROADSET: rgb = (60, 30, 35)
        f = 1 + (c['h'] - ROAD) * 0.02
        rgb = tuple(max(0, min(255, int(v * f))) for v in rgb)
        X, Z = (x + HX) * sc, (z + HZ) * sc
        rect(X, Z, X + sc - 1, Z + sc - 1, rgb)
    for (x, z) in occ:
        if (x, z) in col and col[(x, z)]['d'] > WALLD + 1 and not col[(x, z)]['liq']:
            X, Z = (x + HX) * sc, (z + HZ) * sc; rect(X, Z, X + 1, Z + 1, (30, 70, 30))
    for (x, y, z, yw) in CPS:
        X, Z = int((x + HX) * sc), int((z + HZ) * sc); rect(X - 1, Z - 1, X + 1, Z + 1, (255, 255, 0))
    for i in ITEMROWS:
        X, Z = int((pts[i][0] + HX) * sc), int((pts[i][1] + HZ) * sc); rect(X - 3, Z - 3, X + 3, Z + 3, (255, 220, 0))
    raw = b''.join(bytes([0]) + bytes(px[y * w * sc * 3:(y + 1) * w * sc * 3]) for y in range(hgt * sc))
    def chunk(t, d): return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    with open(sys.argv[2], 'wb') as f:
        f.write(bytes([137, 80, 78, 71, 13, 10, 26, 10]) + chunk(b'IHDR', struct.pack('>IIBBBBB', w * sc, hgt * sc, 8, 2, 0, 0, 0))
                + chunk(b'IDAT', zlib.compress(raw, 6)) + chunk(b'IEND', b''))
    print('aperçu', sys.argv[2])
