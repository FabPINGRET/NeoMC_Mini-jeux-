"""✷ TNT Run sur la glace — id 244 (Glacier, même taille que la tour de laine) et 245 (Grand glacier, un peu plus grand).

    python tools/arcade/gen_tntice.py .

Même jeu que le TNT Run (mg:tntrun) : 3 étages, le sol s'efface sous les pas, dernier debout gagne. Mais en glace :
la glace compacte glisse, le bloc piétiné devient de la glace bleue (glisse encore plus), puis du verre bleu, puis disparaît.
Glacier : étages 29 / 25 / 21 ; Grand glacier : 35 / 31 / 27 (centre 0 ~ 41700, étages y 84 / 74 / 64).
"""
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
GS, GB = 244, 245
Z = 41700
YS = [84, 74, 64]
HS = {GS: [14, 12, 10], GB: [17, 15, 13]}
HMAX = 18
FRESH, MARK, WARN = 'packed_ice', 'blue_ice', 'light_blue_stained_glass'


def build(g):
    L = [f'# Étages du {"Glacier" if g == GS else "Grand glacier"}']
    for y, h in zip(YS, HS[g]):
        L.append(f'fill {-h} {y} {Z - h} {h} {y} {Z + h} minecraft:{FRESH}')
    h = HS[g][0] + 1
    L += [f'fill {-h} 50 {Z - h} {h} 95 {Z - h} minecraft:barrier', f'fill {-h} 50 {Z + h} {h} 95 {Z + h} minecraft:barrier',
          f'fill {-h} 50 {Z - h + 1} {-h} 95 {Z + h - 1} minecraft:barrier', f'fill {h} 50 {Z - h + 1} {h} 95 {Z + h - 1} minecraft:barrier']
    return L


w('tntice/build_s', build(GS))
w('tntice/build_b', build(GB))
w('tntice/build', ['# ✷ TNT Run glace : remise à neuf', f'fill {-HMAX - 1} 50 {Z - HMAX - 1} {HMAX + 1} 95 {Z + HMAX + 1} minecraft:air',
                   f'execute if score $game mg.st matches {GS} run function mg:tntice/build_s',
                   f'execute if score $game mg.st matches {GB} run function mg:tntice/build_b'])
w('tntice/prepare', ['# ✷ TNT Run glace — préparation', 'function mg:tntice/build',
                     f'kill @e[type=minecraft:item,x={-HMAX - 1},y=50,z={Z - HMAX - 1},dx={2 * HMAX + 2},dy=50,dz={2 * HMAX + 2}]',
                     'scoreboard players set $px mg.st 0', 'scoreboard players set $py mg.st 92', f'scoreboard players set $pz mg.st {Z}',
                     'scoreboard players set $dk mg.st 9', 'gamemode adventure @a[tag=mg.play]',
                     f'execute as @a[tag=mg.play] run spawnpoint @s 0 92 {Z}',
                     f'execute if score $game mg.st matches {GS} run spreadplayers 0 {Z} 4 13 under 86 false @a[tag=mg.play]',
                     f'execute if score $game mg.st matches {GB} run spreadplayers 0 {Z} 4 16 under 86 false @a[tag=mg.play]'])
w('tntice/go', ['tellraw @a[tag=mg.play] ' + js({'text': '✷ COURS ! La glace glisse et s\'efface sous tes pas — 3 étages avant le vide. Dernier debout = gagnant !', 'color': 'aqua'})])
MK = [f'execute as @a[tag=mg.play] at @s{p} if block ~ ~-1 ~ minecraft:{FRESH} run setblock ~ ~-1 ~ minecraft:{MARK}'
      for p in ('', ' positioned ~0.3 ~ ~0.3', ' positioned ~-0.3 ~ ~0.3', ' positioned ~0.3 ~ ~-0.3', ' positioned ~-0.3 ~ ~-0.3')]
w('tntice/tick', ['# ✷ TNT Run glace — tick (même règles que tntrun/tick)'] + MK +
  ['scoreboard players remove $dk mg.st 1', 'execute if score $dk mg.st matches ..0 run function mg:tntice/decay',
   'execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]',
   'execute as @a[tag=mg.play,scores={mg.t=..58}] run function mg:core/eliminate',
   'execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:core/eliminate',
   'execute store result score $alive mg.st if entity @a[tag=mg.play]',
   'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] run function mg:core/win_player',
   'execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw'])
D = ['# Glace bleue → verre bleu → vide (un bloc piétiné disparaît entre 9 et 18 ticks plus tard)', 'scoreboard players set $dk mg.st 9']
D += [f'fill {-HMAX} {y} {Z - HMAX} {HMAX} {y} {Z + HMAX} minecraft:air replace minecraft:{WARN}' for y in YS]
D += [f'fill {-HMAX} {y} {Z - HMAX} {HMAX} {y} {Z + HMAX} minecraft:{WARN} replace minecraft:{MARK}' for y in YS]
w('tntice/decay', D)
w('tntice/cleanup', [f'kill @e[type=minecraft:item,x={-HMAX - 1},y=50,z={Z - HMAX - 1},dx={2 * HMAX + 2},dy=50,dz={2 * HMAX + 2}]'])

C.register([GS, GB], 'tntice', [C.announce(GS, '', '✷ TNT RUN — GLACIER', 'aqua', 'la glace glisse et s\'efface sous tes pas !'),
                                 C.announce(GB, '', '✷ TNT RUN — GRAND GLACIER', 'aqua', 'la glace glisse et s\'efface sous tes pas !')])
C.forceload([f'# TNT Run glace (z {Z})', f'forceload add {-HMAX - 1} {Z - HMAX - 1} {HMAX + 1} {Z + HMAX + 1}'])

# menu ✷ TNT Run (dialogue sub_tntrun) : les deux cartes à côté de la tour de laine (gardées par gen_variants)
import json
import os
p = os.path.join(C.D, 'dialog', 'sub_tntrun.json')
d = json.load(open(p, encoding='utf-8'))
cmds = [a.get('action', {}).get('command') for a in d['actions']]
add = [(GS, 'Glacier', 'Même taille que la tour de laine, en glace qui glisse'), (GB, 'Grand glacier', 'Un peu plus grand, en glace qui glisse')]
i = cmds.index('trigger mg.go set 2') + 1
for g, nm, tip in add:
    if f'trigger mg.go set {g}' not in cmds:
        d['actions'].insert(i, {'label': [{'text': f'{nm} ', 'color': 'aqua'}, {'text': '★★★', 'color': 'gold'}, {'text': '☆', 'color': 'dark_gray'}],
                                'tooltip': [{'text': tip, 'color': 'gray'}],
                                'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.go set {g}'}})
        i += 1
with open(p, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
    f.write('\n')
print('TNT Run glace OK')
