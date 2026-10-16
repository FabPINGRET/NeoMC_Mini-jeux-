"""🌀 Labyrinthe géant — id 241. Course : le premier à traverser le labyrinthe (100 × 100 blocs) gagne. Z 41100.

    python tools/arcade/gen_maze.py .

- 33 × 33 cases (couloirs de 2, haies de 3 blocs : on ne saute pas par-dessus), entrée au milieu du côté ouest,
  sortie (or) au milieu du côté est. 3 labyrinthes générés à l'avance (graine fixe), tiré au hasard à chaque partie ;
  quelques murs en moins pour créer des boucles.
- Bonus (objets flottants, reviennent après 30 s) : ⚡ vitesse 10 s, 🧭 boussole vers la sortie 30 s, 🦅 vue d'aigle
  (6 s en spectateur 30 blocs au-dessus, puis retour à sa place).
- Pièges : toiles d'araignée, cases piégées invisibles (lenteur + aveuglement, ou retour au départ),
  téléporteurs (dalle d'obsidienne pleureuse : envoie vers sa jumelle), grilles qui se ferment et s'ouvrent (toutes les 8 s).
- 5 min max : le plus proche de la sortie gagne. Seul : entraînement (chrono, match nul).
- La grande zone n'est chargée (forceload) que pendant la partie ; construite 2 s après le lancement, pendant le compte à
  rebours (les joueurs attendent dans le sas de départ, ouvert au GO). Préfixe : mg.j*, fonctions mg:maze/*.
"""
import random
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
GID = 241
Z = 41100
N = 33                      # cases par côté
S = 3 * N + 1               # 100 blocs
XM, ZM = -50, Z - 50        # coin nord-ouest
FY = 65                     # pieds (sol y 64), haies y 65..67
MID = N // 2                # rangée de l'entrée et de la sortie
EB = 3 * MID + 1            # b de l'ouverture (2 blocs)
LIMIT = 6000
SEEDS = [4101, 4102, 4103]
PL = '@a[tag=mg.play]'
XS1, XS2, ZS1, ZS2 = XM - 7, XM - 1, ZM + EB - 3, ZM + EB + 4     # sas de départ
XE1, XE2 = XM + S, XM + S + 6                                       # salle de sortie


def ccx(i):
    return XM + 3 * i + 2      # centre (entre les 2 blocs) d'une case


def ccz(j):
    return ZM + 3 * j + 2


START = (XM - 4, ZM + EB + 1)   # centre du sas (x, z) : blocs xm-4, z au milieu de l'ouverture


def make_maze(seed):
    rnd = random.Random(seed)
    wall = [[(a % 3 == 0 or b % 3 == 0) for b in range(S)] for a in range(S)]

    def open_between(i, j, i2, j2):
        if i2 != i:
            a = 3 * max(i, i2)
            for b in (3 * j + 1, 3 * j + 2):
                wall[a][b] = False
        else:
            b = 3 * max(j, j2)
            for a in (3 * i + 1, 3 * i + 2):
                wall[a][b] = False

    seen = {(0, 0)}
    stack = [(0, 0)]
    passages = []
    while stack:
        i, j = stack[-1]
        nb = [(i + di, j + dj) for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)) if 0 <= i + di < N and 0 <= j + dj < N and (i + di, j + dj) not in seen]
        if not nb:
            stack.pop()
            continue
        n = rnd.choice(nb)
        open_between(i, j, *n)
        passages.append(((i, j), n))
        seen.add(n)
        stack.append(n)
    # boucles : ~7 % des murs intérieurs restants ouverts
    extra = []
    for i in range(N):
        for j in range(N):
            for di, dj in ((1, 0), (0, 1)):
                i2, j2 = i + di, j + dj
                if i2 < N and j2 < N and rnd.random() < 0.07:
                    a, b = (3 * i2, 3 * j + 1) if di else (3 * i + 1, 3 * j2)
                    if wall[a][b]:
                        open_between(i, j, i2, j2)
                        extra.append(((i, j), (i2, j2)))
    for b in (EB, EB + 1):
        wall[0][b] = False
        wall[S - 1][b] = False
    # degré de chaque case (impasses)
    deg = {}
    for i in range(N):
        for j in range(N):
            d = 0
            if i > 0 and not wall[3 * i][3 * j + 1]:
                d += 1
            if i < N - 1 and not wall[3 * i + 3][3 * j + 1]:
                d += 1
            if j > 0 and not wall[3 * i + 1][3 * j]:
                d += 1
            if j < N - 1 and not wall[3 * i + 1][3 * j + 3]:
                d += 1
            deg[(i, j)] = d
    return rnd, wall, passages + extra, deg


def runs(cells):
    """[(début, fin)] des suites consécutives d'indices"""
    out, st, prev = [], None, None
    for c in cells:
        if st is None:
            st = prev = c
        elif c == prev + 1:
            prev = c
        else:
            out.append((st, prev))
            st = prev = c
    if st is not None:
        out.append((st, prev))
    return out


def gate_fill(p, blk):
    (i, j), (i2, j2) = p
    if i2 != i:
        x = XM + 3 * max(i, i2)
        return f'fill {x} {FY} {ZM + 3 * j + 1} {x} {FY + 2} {ZM + 3 * j + 2} minecraft:{blk}', (x, ZM + 3 * j + 1, 0, 1)
    z = ZM + 3 * max(j, j2)
    return f'fill {XM + 3 * i + 1} {FY} {z} {XM + 3 * i + 2} {FY + 2} {z} minecraft:{blk}', (XM + 3 * i + 1, z, 1, 0)


for v, seed in enumerate(SEEDS, 1):
    rnd, wall, passages, deg = make_maze(seed)
    L = [f'# 🌀 Labyrinthe géant n° {v} (graine {seed}) : haies']
    for a in range(0, S, 3):
        L += [f'fill {XM + a} {FY} {ZM + b1} {XM + a} {FY + 2} {ZM + b2} minecraft:moss_block' for b1, b2 in runs([b for b in range(S) if wall[a][b]])]
    for b in range(0, S, 3):
        L += [f'fill {XM + a1} {FY} {ZM + b} {XM + a2} {FY + 2} {ZM + b} minecraft:moss_block' for a1, a2 in runs([a for a in range(S) if wall[a][b]])]
    L.append(f'fill {XM} {FY + 2} {ZM} {XM + S - 1} {FY + 2} {ZM + S - 1} minecraft:flowering_azalea_leaves[persistent=true] replace minecraft:moss_block')
    # cases spéciales : loin du départ (i ≥ 3), jamais deux fois la même
    cells = [(i, j) for i in range(3, N) for j in range(N) if (i, j) != (N - 1, MID)]
    rnd.shuffle(cells)
    dead = [c for c in cells if deg[c] == 1]
    other = [c for c in cells if deg[c] != 1]
    bonus, dead = dead[:12], dead[12:]
    traps = other[:10]
    tele = other[10:16]
    webs = other[16:30]
    # toiles : un bloc de toile dans le couloir
    L += [f'setblock {ccx(i) - 1 + rnd.randint(0, 1)} {FY} {ccz(j) - 1 + rnd.randint(0, 1)} minecraft:cobweb' for (i, j) in webs]
    # téléporteurs : sol en obsidienne pleureuse
    L += [f'fill {ccx(i) - 1} {FY - 1} {ccz(j) - 1} {ccx(i)} {FY - 1} {ccz(j)} minecraft:crying_obsidian' for (i, j) in tele]
    # grilles : 12 passages intérieurs, groupes A / B
    inner = [p for p in passages if p[0][0] >= 2 and p[1][0] >= 2]
    rnd.shuffle(inner)
    gates = inner[:12]
    GA, GB = gates[0::2], gates[1::2]
    L += [gate_fill(p, 'iron_bars')[0] for p in GA]
    w(f'maze/walls_{v}', L)
    E = [f'# Labyrinthe n° {v} : marqueurs des bonus, pièges, téléporteurs']
    for k, (i, j) in enumerate(bonus):
        E.append(f'summon minecraft:marker {ccx(i)} {FY} {ccz(j)} {{Tags:["mg.jent","mg.jbm","mg.jb{k % 3 + 1}"]}}')
    for k, (i, j) in enumerate(traps):
        E.append(f'summon minecraft:marker {ccx(i)} {FY} {ccz(j)} {{Tags:["mg.jent","mg.jtr","mg.jt{1 if k >= 3 else 2}"]}}')
    for k, (i, j) in enumerate(tele):
        E += [f'summon minecraft:marker {ccx(i)} {FY} {ccz(j)} {{Tags:["mg.jent","mg.jtp","mg.jtpn"]}}',
              f'scoreboard players set @e[type=minecraft:marker,tag=mg.jtpn] mg.jp {k}', 'tag @e[tag=mg.jtpn] remove mg.jtpn']
    w(f'maze/ents_{v}', E)

    def toggle(close, open_):
        T = []
        for p in close:
            cmd, (x, z, dx, dz) = gate_fill(p, 'iron_bars')
            T.append(f'execute unless entity @a[gamemode=!spectator,x={x},y={FY},z={z},dx={dx},dy=2,dz={dz}] run {cmd}')
        T += [gate_fill(p, 'air')[0] for p in open_]
        return T
    w(f'maze/gates_a_{v}', ['# Grilles : A fermées, B ouvertes'] + toggle(GA, GB))
    w(f'maze/gates_b_{v}', ['# Grilles : B fermées, A ouvertes'] + toggle(GB, GA))
    print(f'labyrinthe {v} : {len(L)} commandes, {len(bonus)} bonus, {len(traps)} pièges, {len(tele)} téléporteurs, {len(gates)} grilles')

# ------------------------------------------------------------------ sas, construction
SAS = [f'# Sas de départ (chargé en permanence) : x {XS1}..{XS2}, z {ZS1}..{ZS2}',
       f'fill {XS1 - 1} {FY - 1} {ZS1 - 1} {XS2} {FY + 3} {ZS2 + 1} minecraft:air',
       f'fill {XS1 - 1} {FY - 1} {ZS1 - 1} {XS2} {FY - 1} {ZS2 + 1} minecraft:polished_andesite',
       f'fill {XS1 - 1} {FY} {ZS1 - 1} {XS2} {FY + 3} {ZS1 - 1} minecraft:glass', f'fill {XS1 - 1} {FY} {ZS2 + 1} {XS2} {FY + 3} {ZS2 + 1} minecraft:glass',
       f'fill {XS1 - 1} {FY} {ZS1} {XS1 - 1} {FY + 3} {ZS2} minecraft:glass', f'fill {XS1 - 1} {FY + 4} {ZS1 - 1} {XS2} {FY + 4} {ZS2 + 1} minecraft:glass',
       f'fill {XS2} {FY} {ZS1} {XS2} {FY + 3} {ZS2} minecraft:glass',
       f'fill {XS2} {FY} {ZM + EB} {XS2} {FY + 2} {ZM + EB + 1} minecraft:red_stained_glass']
w('maze/sas', SAS)
B = ['# 🌀 Labyrinthe géant : construction (zone chargée ?)',
     f'execute unless loaded {XM} 64 {ZM} run return run schedule function mg:maze/build 10t',
     f'execute unless loaded {XE2} 64 {ZM + S} run return run schedule function mg:maze/build 10t',
     f'execute unless loaded 0 64 {Z} run return run schedule function mg:maze/build 10t',
     f'kill @e[type=!minecraft:player,x={XM},y=55,z={ZM},dx={XE2 - XM},dy=40,dz={S}]']
B += [f'fill {XM} {y} {ZM} {XM + S - 1} {y} {ZM + S - 1} minecraft:air' for y in range(FY, FY + 6)]
B += [f'fill {XM} {FY - 2} {ZM} {XM + S - 1} {FY - 2} {ZM + S - 1} minecraft:dirt', f'fill {XM} {FY - 1} {ZM} {XM + S - 1} {FY - 1} {ZM + S - 1} minecraft:grass_block',
      # salle de sortie (or)
      f'fill {XE1} {FY - 1} {ZM + EB - 3} {XE2} {FY + 4} {ZM + EB + 4} minecraft:air',
      f'fill {XE1} {FY - 1} {ZM + EB - 3} {XE2} {FY - 1} {ZM + EB + 4} minecraft:gold_block',
      f'fill {XE1} {FY} {ZM + EB - 3} {XE2} {FY + 3} {ZM + EB - 3} minecraft:glass', f'fill {XE1} {FY} {ZM + EB + 4} {XE2} {FY + 3} {ZM + EB + 4} minecraft:glass',
      f'fill {XE2} {FY} {ZM + EB - 2} {XE2} {FY + 3} {ZM + EB + 3} minecraft:glass',
      f'setblock {XE1 + 3} {FY + 3} {ZM + EB + 1} minecraft:glowstone']
B += [f'execute if score $jv mg.st matches {v} run function mg:maze/walls_{v}' for v in (1, 2, 3)]
B += [f'execute if score $jv mg.st matches {v} run function mg:maze/ents_{v}' for v in (1, 2, 3)]
B += ['scoreboard players set $jg mg.st 0', 'scoreboard players set $jok mg.st 1',
      f'summon minecraft:text_display {XE1 + 3} {FY + 2.5} {ZM + EB + 1} {{Tags:["mg.jent"],billboard:"center",text:{js({"text": "🏆 SORTIE", "color": "gold", "bold": True})}}}']
w('maze/build', B)
FL = f'forceload add {XM - 1} {ZM - 1} {XE2 + 1} {ZM + S}'
w('maze/prepare', ['# 🌀 Labyrinthe géant — préparation (le labyrinthe est construit 1 s plus tard, chunks chargés)',
                   FL, 'scoreboard players set $jok mg.st 0', 'execute store result score $jv mg.st run random value 1..3',
                   'function mg:maze/sas', 'schedule function mg:maze/build 20t',
                   f'scoreboard players set $px mg.st 0', f'scoreboard players set $py mg.st {FY + 30}', f'scoreboard players set $pz mg.st {Z}',
                   f'clear {PL}', f'effect clear {PL}', f'gamemode adventure {PL}', f'team join mg_sq {PL}',
                   f'scoreboard players set {PL} mg.jc 0', f'scoreboard players set {PL} mg.je 0', f'scoreboard players set {PL} mg.jk 0',
                   'scoreboard players set $jid mg.st 0', f'execute as {PL} store result score @s mg.jid run scoreboard players add $jid mg.st 1',
                   f'spreadplayers {START[0] + 0.5} {START[1]} 0.5 2 under {FY + 2} false {PL}',
                   f'execute as {PL} at @s run spawnpoint @s ~ ~ ~',
                   'tellraw @a[tag=mg.play] ' + js([{'text': '🌀 LABYRINTHE GÉANT : ', 'color': 'light_purple', 'bold': True},
                                                    {'text': 'traverse le labyrinthe d\'ouest en est, le premier sur l\'or gagne ! Bonus : ⚡ vitesse, 🧭 boussole vers la sortie, '
                                                             '🦅 vue d\'aigle. Méfie-toi des toiles, des grilles qui se ferment, des téléporteurs (obsidienne) et des cases piégées.',
                                             'color': 'gray'}])])
w('maze/go', ['# Départ : le sas s\'ouvre', 'execute unless score $jok mg.st matches 1 run function mg:maze/build',
              f'fill {XS2} {FY} {ZM + EB} {XS2} {FY + 2} {ZM + EB + 1} minecraft:air',
              f'effect give {PL} minecraft:night_vision infinite 0 true', 'scoreboard players set $jtm mg.st 0'])

# ------------------------------------------------------------------ jeu
EXIT = f'x={XE1},y={FY - 1},z={ZM + EB - 3},dx={XE2 - XE1},dy=6,dz=7'
w('maze/tick', [
    '# 🌀 Labyrinthe — tick', 'scoreboard players add $jtm mg.st 1',
    f'execute as @a[tag=mg.play,gamemode=adventure,{EXIT}] run return run function mg:maze/arrive',
    'execute as @e[type=minecraft:marker,tag=mg.jbm] at @s run function mg:maze/bonus_tick',
    'execute as @e[type=minecraft:marker,tag=mg.jtr] at @s as @a[tag=mg.play,gamemode=adventure,distance=..0.9] run function mg:maze/trap',
    'execute as @e[type=minecraft:marker,tag=mg.jtp] at @s as @a[tag=mg.play,gamemode=adventure,distance=..0.8,scores={mg.jc=0}] run function mg:maze/tele',
    'scoreboard players remove @a[scores={mg.jc=1..}] mg.jc 1',
    'execute as @a[tag=mg.play,scores={mg.je=1..}] run function mg:maze/eagle_tick',
    'scoreboard players operation $jq mg.st = $jtm mg.st', 'scoreboard players set #160 mg.st 160', 'scoreboard players operation $jq mg.st %= #160 mg.st',
    'execute if score $jq mg.st matches 0 run function mg:maze/gates',
    'scoreboard players set #20 mg.st 20', 'scoreboard players operation $jq mg.st = $jtm mg.st', 'scoreboard players operation $jq mg.st %= #20 mg.st',
    'execute if score $jq mg.st matches 0 run function mg:maze/second',
    f'execute if score $state mg.st matches 2 if score $jtm mg.st matches {LIMIT}.. run function mg:maze/time_up'])
w('maze/arrive', ['# @s atteint la sortie', 'execute unless score $state mg.st matches 2 run return 0',
                  'scoreboard players operation $js mg.st = $jtm mg.st', 'scoreboard players operation $js mg.st /= #20 mg.st',
                  'tellraw @a [{"text":"🌀 ","color":"light_purple"},{"selector":"@s","color":"yellow","bold":true},{"text":" sort du labyrinthe en ","color":"gray"},{"score":{"name":"$js","objective":"mg.st"},"color":"gold","bold":true},{"text":" s !","color":"gray"}]',
                  'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                  'function mg:core/win_player'])
w('maze/time_up', ['# Temps écoulé : le plus proche de la sortie gagne', 'tellraw @a {"text":"⏱ Temps écoulé ! Le plus proche de la sortie l\'emporte.","color":"gold"}',
                   'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                   f'execute positioned {XE1 + 1} {FY} {ZM + EB + 1} as @a[tag=mg.play,gamemode=adventure,sort=nearest,limit=1] run return run function mg:core/win_player',
                   'function mg:core/draw'])
w('maze/gates', ['# Toutes les 8 s : les grilles A et B s\'échangent', 'scoreboard players add $jg mg.st 1', 'execute if score $jg mg.st matches 2.. run scoreboard players set $jg mg.st 0'] +
  [f'execute if score $jv mg.st matches {v} if score $jg mg.st matches 0 run function mg:maze/gates_a_{v}' for v in (1, 2, 3)] +
  [f'execute if score $jv mg.st matches {v} if score $jg mg.st matches 1 run function mg:maze/gates_b_{v}' for v in (1, 2, 3)] +
  [f'playsound minecraft:block.iron_door.close master @a[tag=mg.play] {XM + S // 2} {FY} {Z} 0.01 0.8'])
# bonus
BON = {1: ('sugar', '⚡ Vitesse (10 s)', 'aqua'), 2: ('compass', '🧭 Boussole vers la sortie (30 s)', 'gold'), 3: ('ender_eye', '🦅 Vue d\'aigle (6 s)', 'green')}
w('maze/bonus_tick', ['# @s : emplacement de bonus (mg.jt = temps avant retour)',
                      'execute if score @s mg.jt matches 1.. run return run scoreboard players remove @s mg.jt 1',
                      'execute unless entity @e[type=minecraft:item_display,tag=mg.jbd,distance=..0.5] run function mg:maze/bonus_show',
                      'execute as @a[tag=mg.play,gamemode=adventure,distance=..1.2,limit=1,sort=nearest] run function mg:maze/bonus_take'])
w('maze/bonus_show', [f'execute if entity @s[tag=mg.jb{n}] run summon minecraft:item_display ~ ~0.7 ~ {{Tags:["mg.jent","mg.jbd"],Glowing:1b,billboard:"vertical",'
                      f'item:{{id:"minecraft:{it}",count:1}},transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}}}'
                      for n, (it, _, _) in BON.items()])
w('maze/bonus_take', ['# @s prend le bonus de l\'emplacement le plus proche', 'tag @e[type=minecraft:marker,tag=mg.jbm,sort=nearest,limit=1] add mg.jbt'] +
  [f'execute if entity @e[tag=mg.jbt,tag=mg.jb{n}] run title @s actionbar {js({"text": nm, "color": col, "bold": True})}' for n, (_, nm, col) in BON.items()] +
  ['execute if entity @e[tag=mg.jbt,tag=mg.jb1] run effect give @s minecraft:speed 10 1 true',
   'execute if entity @e[tag=mg.jbt,tag=mg.jb2] run function mg:maze/compass',
   'execute if entity @e[tag=mg.jbt,tag=mg.jb3] run function mg:maze/eagle',
   'execute at @e[tag=mg.jbt] run kill @e[type=minecraft:item_display,tag=mg.jbd,distance=..1]',
   'scoreboard players set @e[tag=mg.jbt] mg.jt 600', 'tag @e[tag=mg.jbt] remove mg.jbt',
   'playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.3'])
w('maze/compass', ['clear @s minecraft:compass', 'scoreboard players set @s mg.jk 30',
                   f'item replace entity @s hotbar.0 with minecraft:compass[lodestone_tracker={{target:{{pos:[I;{XE1 + 1},{FY},{ZM + EB + 1}],dimension:"minecraft:overworld"}},tracked:false}},'
                   'custom_name=' + js({'text': '🧭 Vers la sortie', 'color': 'gold', 'italic': False}) + ']'])
w('maze/eagle', ['# @s : vue d\'aigle 6 s (spectateur 30 blocs au-dessus, puis retour à cette place)',
                 'execute if score @s mg.je matches 1.. run return 0',
                 'execute at @s run summon minecraft:marker ~ ~ ~ {Tags:["mg.jent","mg.jeg","mg.jegn"]}',
                 'scoreboard players operation @e[type=minecraft:marker,tag=mg.jegn] mg.jid = @s mg.jid', 'tag @e[tag=mg.jegn] remove mg.jegn',
                 'scoreboard players set @s mg.je 120', 'gamemode spectator @s', 'execute at @s run tp @s ~ ~30 ~ ~ 90'])
w('maze/eagle_tick', ['scoreboard players remove @s mg.je 1', 'execute if score @s mg.je matches 1.. run return 0',
                      'scoreboard players operation $jx mg.st = @s mg.jid',
                      'execute as @e[type=minecraft:marker,tag=mg.jeg] if score @s mg.jid = $jx mg.st run tag @s add mg.jsel',
                      'tp @s @e[type=minecraft:marker,tag=mg.jsel,limit=1]', 'kill @e[type=minecraft:marker,tag=mg.jsel]',
                      'gamemode adventure @s', 'title @s actionbar {"text":"🦅 Retour au sol","color":"green"}'])
# pièges, téléporteurs
w('maze/trap', ['# @s marche sur une case piégée (marqueur le plus proche)',
                'execute if entity @e[type=minecraft:marker,tag=mg.jtr,tag=mg.jt1,distance=..1] run function mg:maze/trap_slow',
                'execute if entity @e[type=minecraft:marker,tag=mg.jtr,tag=mg.jt2,distance=..1] run function mg:maze/trap_back'])
w('maze/trap_slow', ['execute if entity @s[nbt={active_effects:[{id:"minecraft:slowness"}]}] run return 0',
                     'effect give @s minecraft:slowness 5 2 true', 'effect give @s minecraft:blindness 2 0 true',
                     'title @s actionbar {"text":"🕸 Piège : englué !","color":"red"}', 'playsound minecraft:block.honey_block.slide master @s ~ ~ ~ 1 0.6'])
w('maze/trap_back', [f'spreadplayers {START[0] + 0.5} {START[1]} 0.5 2 under {FY + 2} false @s',
                     'title @s title {"text":"↩ Retour au départ !","color":"red","bold":true}',
                     'tellraw @a[tag=mg.play] [{"text":"🌀 ","color":"light_purple"},{"selector":"@s","color":"yellow"},{"text":" est tombé dans un piège : retour au départ !","color":"gray"}]',
                     'playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 1 0.6'])
w('maze/tele', ['# @s sur un téléporteur (marqueur le plus proche) : vers sa jumelle (0↔1, 2↔3, 4↔5)',
                'scoreboard players operation $jx mg.st = @e[type=minecraft:marker,tag=mg.jtp,sort=nearest,limit=1] mg.jp',
                'scoreboard players set #2 mg.st 2', 'scoreboard players operation $jy mg.st = $jx mg.st', 'scoreboard players operation $jy mg.st %= #2 mg.st',
                'execute if score $jy mg.st matches 0 run scoreboard players add $jx mg.st 1',
                'execute if score $jy mg.st matches 1 run scoreboard players remove $jx mg.st 1',
                'execute as @e[type=minecraft:marker,tag=mg.jtp] if score @s mg.jp = $jx mg.st run tag @s add mg.jsel',
                'tp @s @e[type=minecraft:marker,tag=mg.jsel,limit=1]', 'tag @e[tag=mg.jsel] remove mg.jsel', 'scoreboard players set @s mg.jc 60',
                'execute at @s run particle minecraft:portal ~ ~1 ~ 0.4 0.8 0.4 0.5 60', 'execute at @s run playsound minecraft:entity.enderman.teleport master @a ~ ~ ~ 1 1.2',
                'title @s actionbar {"text":"🌀 Téléporté !","color":"light_purple"}'])
w('maze/second', ['# Chaque seconde : boussole, chrono',
                  'scoreboard players remove @a[scores={mg.jk=1..}] mg.jk 1', 'execute as @a[scores={mg.jk=0}] run clear @s minecraft:compass',
                  'scoreboard players set $js mg.st ' + str(LIMIT // 20), 'scoreboard players operation $jq mg.st = $jtm mg.st',
                  'scoreboard players operation $jq mg.st /= #20 mg.st', 'scoreboard players operation $js mg.st -= $jq mg.st',
                  f'execute if score $js mg.st matches 0.. run title @a[tag=mg.play,scores={{mg.je=0}}] actionbar [{{"text":"🌀 ⏱ ","color":"light_purple"}},{{"score":{{"name":"$js","objective":"mg.st"}},"color":"yellow"}},{{"text":" s","color":"gray"}}]',
                  f'kill @e[type=minecraft:item,x={XM},y=55,z={ZM},dx={S},dy=40,dz={S}]'])
w('maze/cleanup', ['# Fin du Labyrinthe géant', 'schedule clear mg:maze/build', f'kill @e[type=!minecraft:player,x={XM},y=55,z={ZM},dx={XE2 - XM},dy=40,dz={S}]',
                   'effect clear @a minecraft:night_vision', 'clear @a minecraft:compass', 'team leave @a[team=mg_sq]',
                   'scoreboard players reset * mg.jid', 'scoreboard players reset * mg.jc', 'scoreboard players reset * mg.je', 'scoreboard players reset * mg.jk',
                   'function mg:maze/sas', FL.replace('forceload add', 'forceload remove')])

C.register([GID], 'maze', [C.announce(GID, '', '🌀 LABYRINTHE GÉANT', 'light_purple', 'le premier à traverser le labyrinthe géant gagne !')])
C.objectives([('mg.jid', 'dummy'), ('mg.jc', 'dummy'), ('mg.je', 'dummy'), ('mg.jk', 'dummy'), ('mg.jt', 'dummy'), ('mg.jp', 'dummy')])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['schedule clear mg:maze/build'])
C.forceload([f'# Labyrinthe géant : sas de départ (z {Z})', f'forceload add {XS1 - 1} {ZS1 - 1} {XS2} {ZS2 + 1}'])
print('Labyrinthe géant OK')
