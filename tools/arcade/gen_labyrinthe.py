"""🙈 Labyrinthe aveugle — id 225. Par équipes de 2 : un marcheur aveugle dans le labyrinthe, son guide au-dessus qui voit tout.

    python tools/arcade/gen_labyrinthe.py .

- Les joueurs sont mis par paires au hasard (nombre impair : le dernier devient 2ᵉ guide d'une paire ; 8 paires max,
  les suivants deviennent guides en plus). Chaque paire a sa copie du même labyrinthe (couloirs de 8 en x, z 38200).
- Marcheur : écran noir (petit trou au centre, resource pack) + aveuglement + obscurité, pas de saut par-dessus les murs (plafond invisible). Guide : sur une dalle invisible 8 blocs
  au-dessus, vision nocturne, enfermé au-dessus de son labyrinthe : il parle (vocal) pour guider.
- 3 labyrinthes 18×18 (couloirs de 1, beaucoup d'impasses) tirés au hasard ; entrée au nord-ouest, sortie (or) au sud-est.
- Premier marcheur sur l'or : sa paire gagne (marcheur + guide crédités). 4 min max, sinon match nul.
- Seul : entraînement (aveugle, sans guide), fin au temps ou à la sortie, match nul.
"""
import random
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
GID = 225
Z = C.param('Z', 38200)
N = 18                     # cellules par côté (couloirs de 1)
S = 2 * N + 1              # 37 blocs
LANES = 8
DX = 42                    # écart entre les couloirs
LIMIT = 4800
GY = 12                    # hauteur de la dalle du guide au-dessus du sol (relative)


def maze(seed):
    """Labyrinthe parfait N×N, couloirs de 1 : arbre croissant (70 % dernier ajouté, 30 % au hasard) → long chemin + impasses."""
    r = random.Random(seed)
    wall = [[True] * S for _ in range(S)]
    for i in range(N):
        for j in range(N):
            wall[1 + 2 * i][1 + 2 * j] = False
    seen = {(0, 0)}
    live = [(0, 0)]
    while live:
        k = len(live) - 1 if r.random() < 0.7 else r.randrange(len(live))
        i, j = live[k]
        nb = [(i + di, j + dj, di, dj) for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1))
              if 0 <= i + di < N and 0 <= j + dj < N and (i + di, j + dj) not in seen]
        if not nb:
            live.pop(k)
            continue
        ni, nj, di, dj = r.choice(nb)
        wall[1 + 2 * i + di][1 + 2 * j + dj] = False
        seen.add((ni, nj))
        live.append((ni, nj))
    return wall


def fills(wall):
    out = []
    for x in range(S):
        z = 0
        while z < S:
            if wall[x][z]:
                z2 = z
                while z2 + 1 < S and wall[x][z2 + 1]:
                    z2 += 1
                out.append(f'fill ~{x} ~ ~{z} ~{x} ~2 ~{z2} minecraft:polished_deepslate')
                z = z2 + 1
            else:
                z += 1
    return out


MAZES = [maze(s) for s in (2511, 7302, 9148)]
for k, m in enumerate(MAZES):
    w(f'lab/maze_{k}', [f'# Labyrinthe {k} (relatif : coin nord-ouest au sol)', f'fill ~ ~ ~ ~{S - 1} ~2 ~{S - 1} minecraft:air'] + fills(m) +
      [f'fill ~ ~2 ~ ~{S - 1} ~2 ~{S - 1} minecraft:deepslate_tiles replace minecraft:polished_deepslate',
       f'setblock ~{S - 2} ~-1 ~{S - 2} minecraft:gold_block',
       'setblock ~1 ~-1 ~1 minecraft:lime_concrete'])
w('lab/lane', ['# Un couloir (relatif : coin nord-ouest au sol) : sol, plafond invisible, dalle et cage du guide',
               f'fill ~-2 ~-1 ~-2 ~{S + 1} ~{GY + 6} ~{S + 1} minecraft:air',
               f'fill ~ ~-1 ~ ~{S - 1} ~-1 ~{S - 1} minecraft:smooth_sandstone',
               f'fill ~ ~3 ~ ~{S - 1} ~3 ~{S - 1} minecraft:barrier',
               f'fill ~-1 ~{GY} ~-1 ~{S} ~{GY} ~{S} minecraft:barrier',
               f'fill ~-1 ~{GY + 1} ~-1 ~{S} ~{GY + 5} ~-1 minecraft:barrier', f'fill ~-1 ~{GY + 1} ~{S} ~{S} ~{GY + 5} ~{S} minecraft:barrier',
               f'fill ~-1 ~{GY + 1} ~-1 ~-1 ~{GY + 5} ~{S} minecraft:barrier', f'fill ~{S} ~{GY + 1} ~-1 ~{S} ~{GY + 5} ~{S} minecraft:barrier',
               f'fill ~-1 ~{GY + 6} ~-1 ~{S} ~{GY + 6} ~{S} minecraft:barrier'])
B = ['# 🙈 Labyrinthe aveugle : 8 couloirs, labyrinthe $lbm (0..2)']
XMAX = (LANES - 1) * DX + S + 3
for x0 in range(-3, XMAX + 1, 32):          # zone entière vidée (aussi les restes d'anciennes versions)
    B.append(f'fill {x0} 62 {Z - 3} {min(x0 + 31, XMAX)} 84 {Z + S + 3} minecraft:air')
for k in range(LANES):
    B += [f'execute positioned {k * DX} 64 {Z} run function mg:lab/lane']
    for m in range(len(MAZES)):
        B.append(f'execute if score $lbm mg.st matches {m} positioned {k * DX} 64 {Z} run function mg:lab/maze_{m}')
w('lab/build', B)

PL = '@a[tag=mg.play]'
COLORS = [16711680, 3368703, 16766720, 6750054, 16738740, 10053375, 16777215, 4210752]
CN = ['rouge', 'bleue', 'jaune', 'verte', 'rose', 'violette', 'blanche', 'grise']
w('lab/prepare', ['# 🙈 Labyrinthe aveugle — préparation : labyrinthe au hasard, paires, téléportation',
                  'execute store result score $lbm mg.st run random value 0..2', 'function mg:lab/build',
                  f'scoreboard players set $px mg.st {LANES * DX // 2}', f'scoreboard players set $py mg.st {64 + GY + 12}', f'scoreboard players set $pz mg.st {Z + S // 2}',
                  f'clear {PL}', f'effect clear {PL}', f'gamemode adventure {PL}', f'team join mg_sq {PL}',
                  'tag @a remove mg.lbw', 'tag @a remove mg.lbg', 'tag @a remove mg.lbx', f'scoreboard players reset * mg.lbp',
                  'scoreboard players set $lbn mg.st 0',
                  'function mg:lab/pair',
                  f'execute as {PL} run function mg:lab/place'])
w('lab/pair', ['# Forme les paires au hasard (récursif) : un marcheur puis un guide ; reste impair → guide en plus ; 8 paires max',
               'execute unless entity @a[tag=mg.play,tag=!mg.lbx] run return 0',
               f'execute if score $lbn mg.st matches {LANES}.. run return run execute as @a[tag=mg.play,tag=!mg.lbx] run function mg:lab/extra_one',
               'execute store result score $u mg.st if entity @a[tag=mg.play,tag=!mg.lbx]',
               'execute if score $u mg.st matches 1 if score $lbn mg.st matches 1.. run return run execute as @a[tag=mg.play,tag=!mg.lbx] run function mg:lab/extra_one',
               'scoreboard players add $lbn mg.st 1',
               'execute as @a[tag=mg.play,tag=!mg.lbx,sort=random,limit=1] run function mg:lab/set_walker',
               'execute as @a[tag=mg.play,tag=!mg.lbx,sort=random,limit=1] run function mg:lab/set_guide',
               'function mg:lab/pair'])
w('lab/set_walker', ['tag @s add mg.lbx', 'tag @s add mg.lbw', 'scoreboard players operation @s mg.lbp = $lbn mg.st'])
w('lab/set_guide', ['tag @s add mg.lbx', 'tag @s add mg.lbg', 'scoreboard players operation @s mg.lbp = $lbn mg.st'])
w('lab/extra_one', ['# @s : guide en plus d\'une paire au hasard', 'tag @s add mg.lbx', 'tag @s add mg.lbg',
                    'execute store result score @s mg.lbp run random value 0..999',
                    'scoreboard players operation @s mg.lbp %= $lbn mg.st', 'scoreboard players add @s mg.lbp 1'])
lines = ['# @s : dans son couloir (marcheur à l\'entrée, guide sur sa dalle), couleur de la paire']
for k in range(LANES):
    ox = k * DX
    col = COLORS[k]
    lines += [f'execute if score @s mg.lbp matches {k + 1} if entity @s[tag=mg.lbw] run tp @s {ox + 1}.5 64 {Z + 1}.5 -45 10',
              f'execute if score @s mg.lbp matches {k + 1} if entity @s[tag=mg.lbg] run tp @s {ox + S // 2}.5 {64 + GY + 1} {Z + S // 2}.5 0 75',
              f'execute if score @s mg.lbp matches {k + 1} run item replace entity @s armor.head with minecraft:leather_helmet[dyed_color={col},unbreakable={{}}]',
              f'execute if score @s mg.lbp matches {k + 1} run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color={col},unbreakable={{}}]']
lines += ['execute at @s run spawnpoint @s ~ ~ ~']
w('lab/place', lines)
w('lab/go', ['# Départ', 'scoreboard players set $lbt mg.st 0',
             'effect give @a[tag=mg.lbw] minecraft:blindness infinite 0 true',
             'effect give @a[tag=mg.lbw] minecraft:darkness infinite 0 true',
             'effect give @a[tag=mg.lbg] minecraft:night_vision infinite 0 true',
             'effect give @a[tag=mg.lbw] minecraft:glowing infinite 0 true',
             f'bossbar add mg:lab {js({"text": "🙈 Labyrinthe aveugle", "color": "light_purple"})}', 'bossbar set mg:lab color purple',
             f'bossbar set mg:lab max {LIMIT}', f'bossbar set mg:lab players {PL}',
             'execute as @a[tag=mg.lbw] run function mg:lab/brief'])
w('lab/brief', ['# @s = marcheur : message à sa paire',
                'execute store result storage mg:lab b.p int 1 run scoreboard players get @s mg.lbp', 'function mg:lab/brief_m with storage mg:lab b'])
w('lab/brief_m', ['$title @a[tag=mg.lbw,scores={mg.lbp=$(p)}] title {"text":"🙈 Tu es AVEUGLE","color":"light_purple","bold":true}',
                  '$title @a[tag=mg.lbw,scores={mg.lbp=$(p)}] subtitle {"text":"écoute ton guide, trouve l\'or","color":"gray"}',
                  '$title @a[tag=mg.lbg,scores={mg.lbp=$(p)}] title {"text":"👁 Tu es le GUIDE","color":"aqua","bold":true}',
                  '$title @a[tag=mg.lbg,scores={mg.lbp=$(p)}] subtitle {"text":"mène ton marcheur jusqu\'à l\'or (au vocal !)","color":"gray"}',
                  '$tellraw @a[scores={mg.lbp=$(p)},tag=mg.play] [{"text":"🙈 Paire $(p) : ","color":"light_purple","bold":true},'
                  '{"text":"marcheur ","color":"gray"},{"selector":"@a[tag=mg.lbw,scores={mg.lbp=$(p)}]","color":"yellow"},'
                  '{"text":" — guide ","color":"gray"},{"selector":"@a[tag=mg.lbg,scores={mg.lbp=$(p)}]","color":"aqua"},'
                  '{"text":". Le premier marcheur sur le bloc d\'or fait gagner sa paire !","color":"gray"}]'])
w('lab/blind', ['# Écran noir du marcheur (glyphe du resource pack, renvoyé en titre toutes les secondes ; sans pack : aveuglement seul)',
                'execute unless score $rp mg.st matches 1 run return 0',
                'title @a[tag=mg.lbw,tag=mg.play] times 0 30 0',
                'title @a[tag=mg.lbw,tag=mg.play] title {"text":"\\ue300","font":"mg:lab"}'])
w('lab/tick', ['# 🙈 Labyrinthe aveugle — tick', 'scoreboard players add $lbt mg.st 1',
               'scoreboard players operation $q mg.st = $lbt mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $q mg.st %= #20 mg.st',
               'execute if score $q mg.st matches 5 if score $lbt mg.st matches 60.. run function mg:lab/blind',
               'execute store result bossbar mg:lab value run scoreboard players get $lbt mg.st',
               'execute if score $state mg.st matches 2 as @a[tag=mg.lbw,tag=mg.play] at @s if block ~ ~-0.5 ~ minecraft:gold_block run return run function mg:lab/win',
               f'execute if score $state mg.st matches 2 if score $lbt mg.st matches {LIMIT}.. run function mg:lab/timeout'])
w('lab/win', ['# @s (marcheur) sur l\'or : sa paire gagne',
              'scoreboard players operation $p mg.st = @s mg.lbp',
              'execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] {"text":"🙈 Sortie trouvée ! (entraînement)","color":"yellow"}',
              'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
              'function mg:core/win_player',
              'execute as @a[tag=mg.lbg,tag=mg.play] if score @s mg.lbp = $p mg.st run function mg:lab/win_guide'])
w('lab/win_guide', ['tag @s add mg.win', 'scoreboard players add @s mg.wins 1',
                    'tellraw @a [{"text":"★ ","color":"gold"},{"text":"guidé par ","color":"yellow"},{"selector":"@s","color":"gold","bold":true}]'])
w('lab/timeout', ['tellraw @a[tag=mg.play] {"text":"⏰ Temps écoulé : personne n\'a trouvé la sortie !","color":"red"}', 'function mg:core/draw'])
w('lab/cleanup', ['bossbar remove mg:lab', 'tag @a remove mg.lbw', 'tag @a remove mg.lbg', 'tag @a remove mg.lbx',
                  'scoreboard players reset * mg.lbp', 'team leave @a[team=mg_sq]',
                  'effect clear @a[tag=mg.play] minecraft:blindness', 'effect clear @a[tag=mg.play] minecraft:night_vision',
                  'effect clear @a[tag=mg.play] minecraft:glowing', 'effect clear @a[tag=mg.play] minecraft:darkness', 'title @a reset', 'title @a clear'])

C.register([GID], 'lab', [C.announce(GID, '', '🙈 LABYRINTHE AVEUGLE', 'light_purple',
                                     'par paires : le marcheur est aveugle, son guide le dirige d\'en haut !')])
C.objectives([('mg.lbp', 'dummy')])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['bossbar remove mg:lab', 'data remove storage mg:lab b'])
C.forceload([f'# Labyrinthe aveugle (z {Z})', f'forceload add -3 {Z - 3} {XMAX} {Z + S + 3}'])
print('Labyrinthe aveugle OK :', len(MAZES), 'labyrinthes,', LANES, 'couloirs')
