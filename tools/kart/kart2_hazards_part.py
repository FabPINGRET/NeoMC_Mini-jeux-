# Dangers : entités recréées à chaque course (Thwomps, barres de feu, Podoboos, Chomp, animaux...) : exécuté par gen_kart2.py (exec) dans l'ordre des parts.
# Utilise : C, CA, CB, HW, HX, HZ, NP, PF, QUICK, SEATS, W, WALLD, col, frame, near_wp, occ, pipe, random, ry, sx, sz,
#   take, tangent, yaw_of
# ------------------------------------------------------------------ dangers (entités, recréées à chaque course)
T0 = 'left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]'
FLIP = 'left_rotation:[0f,1f,0f,0f],right_rotation:[0f,0f,0f,1f]'
def tf(s, ty=0.0, flip=True, sy=None):
    return 'transformation:{translation:[0f,%sf,0f],%s,scale:[%sf,%sf,%sf]}' % (round(ty, 3), FLIP if flip else T0, s, sy if sy else s, s)
def P(x, y, z): return f'{round(x, 2)} {round(y, 2)} {round(W(0) + z, 2)}'
def lerp(a, b, t): return tuple(a[k] + (b[k] - a[k]) * t for k in range(3))
HZT = '"mg.khz","mg.fx"'
spawn = ['# Royaume Koopa : dangers et animaux (recréés à chaque course)', 'kill @e[tag=mg.khz]']
tick = ['# Royaume Koopa : dangers (chaque tick de course)']
consts = set()
def phase(T, o):
    consts.add(T)
    tick.extend([f'scoreboard players operation $hp mg.st = $ktime mg.st', f'scoreboard players add $hp mg.st {o}',
                 f'scoreboard players operation $hp mg.st %= #h{T} mg.st'])
def at(p, cmd): tick.append(f'execute if score $hp mg.st matches {p} run {cmd}')
def hit_at(prange, pos, r, big=False):
    tick.append(f'execute if score $hp mg.st matches {prange} positioned {P(*pos)} as @e[type=minecraft:block_display,tag=mg.kart,distance=..{r}] run function {PF}{"hz_big" if big else "hz_hit"}')
HID = [0]
def nid():
    HID[0] += 1; return f'mg.kh{HID[0]}'

def road_pt(i, off, up=0.0):
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    return (cx + nx2 * off, ry2 + 1 + up, cz + nz2 * off)

# Thwomps : 3 rangées de 2 dans le château, en alternance (toujours un côté libre)
for f in (0.18, 0.5, 0.82):
    i = (CA + int(((CB - CA) % NP) * f)) % NP
    for side, o in ((-1, 0), (1, 50)):
        t = nid(); x, y, z = road_pt(i, 2.3 * side)
        bot, top = (x, y + 1.6, z), (x, y + 1.6 + 4.5, z)
        spawn.append(f'summon minecraft:item_display {P(*top)} {{Tags:["mg.kthw","{t}",{HZT}],teleport_duration:2,item:{{id:"minecraft:chiseled_stone_bricks"}},'
                     f'Rotation:[{yaw_of(-tangent(i)[0], -tangent(i)[1])}f,0f],{tf(3.2)}}}')
        phase(100, o)
        at(48, f'tp @e[type=minecraft:item_display,tag={t}] {P(top[0], top[1] + 0.5, top[2])}')
        at(52, f'execute positioned {P(*bot)} run playsound minecraft:block.stone.hit master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 0.5')
        at(60, f'data merge entity @e[type=minecraft:item_display,tag={t},limit=1] {{teleport_duration:2}}')
        at(60, f'tp @e[type=minecraft:item_display,tag={t}] {P(*bot)}')
        at(62, f'execute positioned {P(x, y, z)} run particle minecraft:explosion ~ ~0.3 ~ 1.2 0.2 1.2 0 4')
        at(62, f'execute positioned {P(x, y, z)} run playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..28] ~ ~ ~ 0.8 0.6')
        hit_at('61..84', (x, y, z), 2.3, big=True)
        at(85, f'data merge entity @e[type=minecraft:item_display,tag={t},limit=1] {{teleport_duration:20}}')
        at(85, f'tp @e[type=minecraft:item_display,tag={t}] {P(*top)}')
        at(99, f'data merge entity @e[type=minecraft:item_display,tag={t},limit=1] {{teleport_duration:3}}')
# Barres de feu : 2 dans le château, sens opposés
for f, spd in ((0.34, 7), (0.66, -6)):
    i = (CA + int(((CB - CA) % NP) * f)) % NP
    x, y, z = road_pt(i, 0, 0.7)
    t = nid()
    spawn.append(f'summon minecraft:item_display {P(x, y, z)} {{Tags:["mg.kfbc","{t}",{HZT}],item:{{id:"minecraft:magma_block"}},brightness:{{sky:15,block:15}},{tf(0.9, flip=False)}}}')
    tick.append(f'execute as @e[type=minecraft:item_display,tag={t}] at @s run rotate @s ~{spd} 0')
    for k in range(1, 6):
        tb = f'{t}b{k}'
        spawn.append(f'summon minecraft:item_display {P(x, y, z)} {{Tags:["mg.kfb","{tb}",{HZT}],teleport_duration:1,item:{{id:"minecraft:magma_block"}},brightness:{{sky:15,block:15}},{tf(0.55, flip=False)}}}')
        tick.append(f'execute as @e[type=minecraft:item_display,tag={t}] at @s positioned ^ ^ ^{round(0.85 * k, 2)} run tp @e[type=minecraft:item_display,tag={tb}] ~ ~ ~')
tick.append(f'execute as @e[type=minecraft:item_display,tag=mg.kfb] at @s positioned ~ ~-0.7 ~ as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.05] run function {PF}hz_hit')
tick.append('execute if score $kph mg.st matches 0 as @e[type=minecraft:item_display,tag=mg.kfb] at @s run particle minecraft:flame ~ ~ ~ 0.1 0.1 0.1 0.01 1')
# Sauteurs : Cheep Cheep (plage, par-dessus la chaussée) et Podoboos (château, d'un canal de lave à l'autre)
def leaper(i, item, span, low, o, T=100, sound='entity.salmon.flop', billboard=True):
    t = nid()
    A, E1, M, E2, Bp = (road_pt(i, -span, low), road_pt(i, -5, 0.4), road_pt(i, 0, 1.0), road_pt(i, 5, 0.4), road_pt(i, span, low))
    spawn.append(f'summon minecraft:item_display {P(*A)} {{Tags:["mg.kleap","{t}",{HZT}],teleport_duration:6,item:{{id:"minecraft:{item}"}},'
                 f'billboard:"center",brightness:{{sky:15,block:15}},{tf(1.4, 0.3, flip=False)}}}')
    phase(T, o)
    at(1, f'data merge entity @e[type=minecraft:item_display,tag={t},limit=1] {{teleport_duration:6}}')
    at(1, f'tp @e[type=minecraft:item_display,tag={t}] {P(*E1)}')
    at(1, f'execute positioned {P(*A)} run particle minecraft:{"splash" if "fish" in item else "lava"} ~ ~0.5 ~ 0.4 0.2 0.4 0 12')
    at(1, f'execute positioned {P(*A)} run playsound minecraft:{sound} master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 1')
    at(7, f'data merge entity @e[type=minecraft:item_display,tag={t},limit=1] {{teleport_duration:4}}')
    at(7, f'tp @e[type=minecraft:item_display,tag={t}] {P(*M)}')
    at(11, f'tp @e[type=minecraft:item_display,tag={t}] {P(*E2)}')
    at(15, f'data merge entity @e[type=minecraft:item_display,tag={t},limit=1] {{teleport_duration:6}}')
    at(15, f'tp @e[type=minecraft:item_display,tag={t}] {P(*Bp)}')
    at(21, f'execute positioned {P(*Bp)} run particle minecraft:{"splash" if "fish" in item else "lava"} ~ ~0.5 ~ 0.4 0.2 0.4 0 12')
    at(60, f'data merge entity @e[type=minecraft:item_display,tag={t},limit=1] {{teleport_duration:0}}')
    at(60, f'tp @e[type=minecraft:item_display,tag={t}] {P(*A)}')
    for p in range(7, 16):
        q = lerp(E1, M, (p - 7) / 4) if p <= 11 else lerp(M, E2, (p - 11) / 4)
        hit_at(str(p), (q[0], q[1] - 0.6, q[2]), 1.5)
gi = near_wp(203, 32)
for k, o in enumerate((0, 37, 71)):
    leaper((gi + k * 14) % NP, 'tropical_fish', 12, -1.6, o)
for f, o in ((0.27, 10), (0.6, 55), (0.72, 80)):
    leaper((CA + int(((CB - CA) % NP) * f)) % NP, 'fire_charge', 8.5, -2.2, o, T=90, sound='block.lava.pop')
# Plantes Piranha : dans des tuyaux le long de la jungle, mordent le bord de la piste
PIPES = []
for k, f in enumerate((0.05, 0.2, 0.35, 0.5, 0.65, 0.8, 0.95)):
    a0, a1 = near_wp(170, -140), near_wp(25, -135)
    i = (a0 + int(((a1 - a0) % NP) * f)) % NP
    side = 1 if k % 2 else -1
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    px_, pz_ = round(cx + nx2 * (WALLD + 3) * side), round(cz + nz2 * (WALLD + 3) * side)
    if (px_, pz_) not in col: continue
    PIPES.append((px_, pz_, ry2))
    pipe(px_, pz_, 4, ry2 + 1)
    take(px_, pz_, 3)
    t = nid()
    rest = (px_ + 0.5, ry2 + 6.2, pz_ + 0.5)
    lunge = road_pt(i, (HW - 2.2) * side, 0.9)
    yaw = yaw_of(-nx2 * side, -nz2 * side)
    spawn.append(f'summon minecraft:item_display {P(*rest)} {{Tags:["mg.kpir","{t}",{HZT}],teleport_duration:10,item:{{id:"minecraft:red_mushroom_block"}},Rotation:[{yaw}f,0f],{tf(1.5)}}}')
    phase(70, k * 23)
    at(10, f'tp @e[type=minecraft:item_display,tag={t}] {P(rest[0], rest[1] + 0.4, rest[2])}')
    at(25, f'tp @e[type=minecraft:item_display,tag={t}] {P(*rest)}')
    at(40, f'execute positioned {P(*rest)} run playsound minecraft:entity.ravager.roar master @a[tag=mg.play,distance=..18] ~ ~ ~ 0.4 1.8')
    at(48, f'data merge entity @e[type=minecraft:item_display,tag={t},limit=1] {{teleport_duration:3}}')
    at(48, f'tp @e[type=minecraft:item_display,tag={t}] {P(*lunge)}')
    at(50, f'execute positioned {P(*lunge)} run playsound minecraft:entity.evoker_fangs.attack master @a[tag=mg.play,distance=..18] ~ ~ ~ 1 1.2')
    hit_at('50..55', (lunge[0], lunge[1] - 0.9, lunge[2]), 2.0)
    at(56, f'data merge entity @e[type=minecraft:item_display,tag={t},limit=1] {{teleport_duration:10}}')
    at(56, f'tp @e[type=minecraft:item_display,tag={t}] {P(*rest)}')
# Goombas (jungle) et Pokeys (désert) : traversent la piste en patrouille
def walker(i, item, tag, speed, T, scale, flip_start):
    a, b = road_pt(i, -4.0), road_pt(i, 4.0)
    if flip_start: a, b = b, a
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    yaw = yaw_of(b[0] - a[0], b[2] - a[2])
    t = nid()
    spawn.append(f'summon minecraft:item_display {P(a[0], a[1] + 0.5 * scale, a[2])} {{Tags:["{tag}","mg.kwalk","{t}",{HZT}],teleport_duration:1,item:{{id:"minecraft:{item}"}},'
                 f'Rotation:[{yaw}f,0f],{tf(scale)}}}')
for k, f in enumerate((0.12, 0.3, 0.42, 0.58, 0.74, 0.88)):
    a0, a1 = near_wp(170, -140), near_wp(25, -135)
    walker((a0 + int(((a1 - a0) % NP) * f)) % NP, 'brown_mushroom_block', 'mg.kgoo', 0.12, 66, 1.2, k % 2)
for k, f in enumerate((0.15, 0.35, 0.55, 0.75)):
    a0, a1 = near_wp(-80, -132), near_wp(-224, -95)
    walker((a0 + int(((a1 - a0) % NP) * f)) % NP, 'cactus', 'mg.kpok', 0.12, 66, 1.3, k % 2)
consts.add(66)
tick += ['scoreboard players operation $hw mg.st = $ktime mg.st', 'scoreboard players operation $hw mg.st %= #h66 mg.st',
         'execute as @e[type=minecraft:item_display,tag=mg.kwalk] at @s run tp @s ^ ^ ^0.12',
         'execute if score $hw mg.st matches 0 as @e[type=minecraft:item_display,tag=mg.kwalk] at @s run tp @s ~ ~ ~ ~180 0',
         f'execute as @e[type=minecraft:item_display,tag=mg.kgoo,tag=!mg.kdead] at @s if entity @e[type=minecraft:block_display,tag=mg.kart,distance=..1.4] run function {PF}goo_squash',
         f'execute as @e[type=minecraft:item_display,tag=mg.kpok] at @s positioned ~ ~-0.6 ~ as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.4] run function {PF}hz_hit',
         f'execute as @e[tag=mg.kdead] run function {PF}goo_wait']
# Chomp : bondit d'un bout à l'autre de la piste à la sortie du pont
ci = near_wp(-91, 146)
cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(ci)
side = 1
post = road_pt(ci, (WALLD + 5) * side, 0.0)
restp = road_pt(ci, (WALLD + 2.5) * side, 1.2)
farp = road_pt(ci, -(HW - 1.5) * side, 1.2)
C(f'fill {round(post[0])} {ry2 + 1} {W(round(post[2]))} {round(post[0])} {ry2 + 2} {W(round(post[2]))} minecraft:oak_log')
t = nid()
yaw = yaw_of(-nx2 * side, -nz2 * side)
spawn.append(f'summon minecraft:item_display {P(*restp)} {{Tags:["mg.kchomp","{t}",{HZT}],teleport_duration:3,item:{{id:"minecraft:coal_block"}},Rotation:[{yaw}f,0f],{tf(2.4)}}}')
links = []
for k in range(1, 6):
    tl = f'{t}l{k}'; links.append(tl)
    q = lerp((post[0], post[1] + 1.2, post[2]), restp, k / 6)
    spawn.append(f'summon minecraft:item_display {P(*q)} {{Tags:["mg.kchain","{tl}",{HZT}],teleport_duration:3,item:{{id:"minecraft:iron_block"}},{tf(0.3, flip=False)}}}')
phase(90, 0)
for p_, h_ in ((15, 0.6), (18, 0), (30, 0.6), (33, 0), (45, 0.6), (48, 0)):
    at(p_, f'tp @e[type=minecraft:item_display,tag={t}] {P(restp[0], restp[1] + h_, restp[2])}')
at(52, f'execute positioned {P(*restp)} run playsound minecraft:entity.wolf.growl master @a[tag=mg.play,distance=..24] ~ ~ ~ 1 0.5')
at(58, f'execute positioned {P(*restp)} run playsound minecraft:entity.wolf.ambient master @a[tag=mg.play,distance=..30] ~ ~ ~ 1 0.5')
at(60, f'data merge entity @e[type=minecraft:item_display,tag={t},limit=1] {{teleport_duration:4}}')
at(60, f'tp @e[type=minecraft:item_display,tag={t}] {P(*farp)}')
for k, tl in enumerate(links, 1):
    at(60, f'data merge entity @e[type=minecraft:item_display,tag={tl},limit=1] {{teleport_duration:4}}')
    at(60, f'tp @e[type=minecraft:item_display,tag={tl}] {P(*lerp((post[0], post[1] + 1.2, post[2]), farp, k / 6))}')
    at(72, f'data merge entity @e[type=minecraft:item_display,tag={tl},limit=1] {{teleport_duration:15}}')
    at(72, f'tp @e[type=minecraft:item_display,tag={tl}] {P(*lerp((post[0], post[1] + 1.2, post[2]), restp, k / 6))}')
for k in range(5):
    q = lerp(road_pt(ci, (HW - 0.5) * side, 0), road_pt(ci, -(HW - 1.5) * side, 0), k / 4)
    hit_at('61..70', q, 1.8, big=True)
at(72, f'data merge entity @e[type=minecraft:item_display,tag={t},limit=1] {{teleport_duration:15}}')
at(72, f'tp @e[type=minecraft:item_display,tag={t}] {P(*restp)}')
# Sables mouvants : tourbillon de particules
qx, qy, qz = road_pt(QUICK, -2.0, 0.2)
tick.append(f'execute if score $kph mg.st matches 2 positioned {P(qx, qy, qz)} run particle minecraft:falling_dust{{block_state:"minecraft:sand"}} ~ ~ ~ 2 0.1 4 0 6')
# titre géant au-dessus du départ
spawn.append(f'summon minecraft:text_display {P(sx, ry + 16, sz)} {{Tags:[{HZT}],billboard:"vertical",text:[{{"text":"ROYAUME ","color":"gold","bold":true}},{{"text":"KOOPA","color":"red","bold":true}}],'
             f'background:1342177280,{tf(6, flip=False)}}}')

# animaux et spectateurs (immobiles, invulnérables)
MOB = 'NoAI:1b,Silent:1b,Invulnerable:1b,PersistenceRequired:1b'
def mob(kind, x, y, z, yaw=None, extra=''):
    yaw = random.randint(0, 359) if yaw is None else yaw
    spawn.append(f'summon minecraft:{kind} {P(x, y, z)} {{Tags:[{HZT},"mg.kmob"],{MOB},Rotation:[{yaw}f,0f]{("," + extra) if extra else ""}}}')
for (x, y, z, yw) in random.sample(SEATS, min(30, len(SEATS))):
    prof = random.choice(['farmer', 'librarian', 'cleric', 'fisherman', 'shepherd', 'armorer', 'cartographer', 'butcher'])
    typ = random.choice(['plains', 'desert', 'savanna', 'snow', 'jungle', 'taiga'])
    mob('villager', x, y, z, yw, f'VillagerData:{{profession:"minecraft:{prof}",type:"minecraft:{typ}",level:1}}')
def mob_on(reg, kind, n, dmin=10, water=None, extra=''):
    k = 0
    for _ in range(4000):
        if k >= n: break
        x, z = random.randint(-HX + 8, HX - 8), random.randint(-HZ + 8, HZ - 8)
        c = col.get((x, z))
        if not c or c['reg'] != reg or c['d'] < dmin or c.get('roof'): continue
        if water is None and (c['liq'] or (x, z) in occ): continue
        if water and c['liq'] != water: continue
        y = (c['lvl'] - 0.6 if water == 'water' else c['lvl'] + 0.1) if water else c['h'] + 1
        mob(kind, x + 0.5, y, z + 0.5, extra=extra); k += 1
mob_on('ville', 'cat', 5); mob_on('ville', 'villager', 6); mob_on('ville', 'chicken', 4)
mob_on('plage', 'turtle', 7); mob_on('plage', 'dolphin', 4, water='water'); mob_on('plage', 'tropical_fish', 10, dmin=9, water='water')
mob_on('plage', 'parrot', 4)
mob_on('jungle', 'parrot', 8); mob_on('jungle', 'ocelot', 4); mob_on('jungle', 'panda', 3); mob_on('jungle', 'frog', 5)
mob_on('jungle', 'axolotl', 4, dmin=9, water='water')
mob_on('desert', 'camel', 5); mob_on('desert', 'armadillo', 4); mob_on('desert', 'rabbit', 4)
mob_on('volcan', 'strider', 7, dmin=9, water='lava'); mob_on('volcan', 'magma_cube', 5, extra='Size:0')
mob_on('centre', 'cow', 6); mob_on('centre', 'sheep', 6); mob_on('centre', 'horse', 4); mob_on('centre', 'fox', 3); mob_on('centre', 'goat', 3)
for f in (0.2, 0.5, 0.8):
    i = (CA + int(((CB - CA) % NP) * f)) % NP
    for s_ in (-1, 1):
        x, y, z = road_pt(i, 9 * s_, 5)
        mob('blaze', x, y, z)
