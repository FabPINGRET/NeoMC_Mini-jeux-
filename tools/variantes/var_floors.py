"""Variantes de sols (Spleef, TNT Run, Splegg) : construction, rétrécissement, étage du haut, décroissance.

Jamais lancé seul : gen_variants.py appelle run() après var_common.init().
"""
from var_common import w
from var_data import FLOOR_MODES, FX, FZ, LAYOUTS


# ============================================================ sols : construction, rétrécissement, étage du haut, décroissance
def box(l):
    H = max(f[1] for f in l['floors']) + 1
    ys = [f[0] for f in l['floors']]
    return H, min(ys), max(ys)


def floor_prepare(mode, tag, extra):
    L = [f'# {mode["name"]} sur un autre sol ($ar) — appelé par {mode["key"]}/prepare. Généré.']
    for l in LAYOUTS:
        L.append(f'execute if score $ar mg.st matches {l["k"]} run function mg:var/floor/l{l["k"]}/build_{tag}')
    L += [f'kill @e[type=minecraft:item,x={FX - 40},y=40,z={FZ - 40},dx=80,dy=70,dz=80]']
    L += extra
    for l in LAYOUTS:
        L.append(f'execute if score $ar mg.st matches {l["k"]} run function mg:var/floor/l{l["k"]}/place')
    return L


def run():
    GH = max(box(l)[0] for l in LAYOUTS)
    GY1 = min(box(l)[1] for l in LAYOUTS) - 6
    GY2 = max(box(l)[2] for l in LAYOUTS) + 7
    for l in LAYOUTS:
        k = l['k']
        H, ymin, ymax = box(l)
        for mat in ('snow_block', 'white_wool'):
            tag = 'snow' if mat == 'snow_block' else 'wool'
            L = [f'# Sol {k} « {l["name"]} » en {mat} (centre {FX} ~ {FZ}). Généré.',
                 '# Nettoyage couche par couche (limite de volume de /fill)']
            for y in range(GY1, GY2 + 1):   # boîte commune à tous les sols (efface le sol précédent, quel qu'il soit)
                L.append(f'fill {FX - GH - 1} {y} {FZ - GH - 1} {FX + GH + 1} {y} {FZ + GH + 1} minecraft:air')
            for (y, h, hole) in l['floors']:
                L.append(f'fill {FX - h} {y} {FZ - h} {FX + h} {y} {FZ + h} minecraft:{mat}')
                if hole:
                    L.append(f'fill {FX - hole} {y} {FZ - hole} {FX + hole} {y} {FZ + hole} minecraft:air')
            y1, y2 = ymin - 6, ymax + 7
            L += [f'fill {FX - H - 1} {y1} {FZ - H - 1} {FX + H + 1} {y2} {FZ - H - 1} minecraft:barrier',
                  f'fill {FX - H - 1} {y1} {FZ + H + 1} {FX + H + 1} {y2} {FZ + H + 1} minecraft:barrier',
                  f'fill {FX - H - 1} {y1} {FZ - H} {FX - H - 1} {y2} {FZ + H} minecraft:barrier',
                  f'fill {FX + H + 1} {y1} {FZ - H} {FX + H + 1} {y2} {FZ + H} minecraft:barrier']
            w(f'var/floor/l{k}/build_{tag}', L)

        # placement : sur l'étage du haut
        top_y, top_h, top_hole = l['floors'][0]
        sp = [f'# Sol {k} : perchoir, élimination, placement sur l’étage du haut. Généré.',
              'scoreboard players set $px mg.st 0', f'scoreboard players set $py mg.st {ymax + 10}', f'scoreboard players set $pz mg.st {FZ}',
              f'scoreboard players set $yd mg.st {ymin - 4}', f'scoreboard players set $ky mg.st {ymin - 4}',
              f'scoreboard players set $nf mg.st {len(l["floors"])}',
              'gamemode adventure @a[tag=mg.play]',
              f'execute as @a[tag=mg.play] run spawnpoint @s {FX} {top_y + 8} {FZ}']
        if top_hole:
            # anneau : 12 points fixes sur l'anneau (pas de départ au-dessus du trou)
            r = (top_h + top_hole) // 2 + 1
            pts = []
            for (px, pz) in [(-r, -r), (0, -r), (r, -r), (r, 0), (r, r), (0, r), (-r, r), (-r, 0),
                             (-r + 3, -r), (r, -r + 3), (r - 3, r), (-r, r - 3)]:
                pts.append((FX + px + 0.5, top_y + 1, FZ + pz + 0.5))
            sp.append('tag @a remove mg.tts')
            for _ in range(2):
                for (px, py, pz) in pts:
                    sp.append(f'execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {{x:{px},y:{py},z:{pz},fx:{FX + 0.5},fz:{FZ + 0.5}}}')
            sp += [f'tp @a[tag=mg.play,tag=!mg.tts] {pts[0][0]} {pts[0][1]} {pts[0][2]}', 'tag @a remove mg.tts']
        else:
            sp.append(f'spreadplayers {FX} {FZ} 3 {max(2, top_h - 2)} under {top_y + 2} false @a[tag=mg.play]')
        w(f'var/floor/l{k}/place', sp)

        # rétrécissement (Spleef) : étape s retire l'anneau extérieur de chaque étage, taille mini 9×9 (ou trou + 2)
        for s in range(1, 11):
            L = [f'# Sol {k}, rétrécissement étape {s} (neige). Généré.']
            for (y, h, hole) in l['floors']:
                rr = h - s + 1
                if rr - 1 < max(4, hole + 2):
                    continue
                L += [f'fill {FX - rr} {y} {FZ - rr} {FX + rr} {y} {FZ - rr} minecraft:air replace minecraft:snow_block',
                      f'fill {FX - rr} {y} {FZ + rr} {FX + rr} {y} {FZ + rr} minecraft:air replace minecraft:snow_block',
                      f'fill {FX - rr} {y} {FZ - rr + 1} {FX - rr} {y} {FZ + rr - 1} minecraft:air replace minecraft:snow_block',
                      f'fill {FX + rr} {y} {FZ - rr + 1} {FX + rr} {y} {FZ + rr - 1} minecraft:air replace minecraft:snow_block']
            w(f'var/floor/l{k}/shrink_{s}', L)

        # décroissance TNT Run
        L = [f'# Sol {k}, TNT Run : laine orange → vide, rouge → orange. Généré.', 'scoreboard players operation $dk mg.st = $vdk mg.st']
        for (y, h, hole) in l['floors']:
            L.append(f'fill {FX - h} {y} {FZ - h} {FX + h} {y} {FZ + h} minecraft:air replace minecraft:orange_wool')
        for (y, h, hole) in l['floors']:
            L.append(f'fill {FX - h} {y} {FZ - h} {FX + h} {y} {FZ + h} minecraft:orange_wool replace minecraft:red_wool')
        w(f'var/floor/l{k}/decay', L)

        # étage du haut (Spleef / Splegg) : même logique que spleef/top_check, sur les 3 étages du haut
        fl = l['floors'][:3]
        L = [f'# Sol {k} : un seul joueur reste sur l’étage occupé le plus haut → il disparaît après 15 s. Généré.',
             'scoreboard players set $tfn mg.st 0', 'scoreboard players set #tf20 mg.st 20']
        for i, (y, h, hole) in enumerate(fl, 1):
            L.append(f'execute store result score $tf{i} mg.st if entity @a[tag=mg.play,scores={{mg.t={y + 1}..}}]')
        L.append('execute if score $tf1 mg.st matches 1 if score $alive mg.st matches 2.. run scoreboard players set $tfn mg.st 1')
        if len(fl) > 1:
            L.append('execute if score $tf1 mg.st matches 0 if score $tf2 mg.st matches 1 if score $alive mg.st matches 2.. run scoreboard players set $tfn mg.st 2')
        if len(fl) > 2:
            L.append('execute if score $tf1 mg.st matches 0 if score $tf2 mg.st matches 0 if score $tf3 mg.st matches 1 if score $alive mg.st matches 2.. run scoreboard players set $tfn mg.st 3')
        L += ['execute if score $tfn mg.st matches 0 run return run scoreboard players set $tff mg.st 0',
              'execute unless score $tfn mg.st = $tff mg.st run tellraw @a[tag=!mg.surv] [{"text":"⚠ ","color":"gold"},{"text":"Un joueur est seul en haut : l\'étage disparaît dans 15 secondes !","color":"gold"}]',
              'execute unless score $tfn mg.st = $tff mg.st run scoreboard players set $tfc mg.st 300',
              'scoreboard players operation $tff mg.st = $tfn mg.st',
              'scoreboard players remove $tfc mg.st 1',
              'scoreboard players operation $tfs mg.st = $tfc mg.st',
              'scoreboard players add $tfs mg.st 19',
              'scoreboard players operation $tfs mg.st /= #tf20 mg.st',
              'title @a[tag=!mg.surv,tag=!mg.lk] actionbar [{"text":"⚠ L\'étage du haut disparaît dans ","color":"gold"},{"score":{"name":"$tfs","objective":"mg.st"},"color":"red","bold":true},{"text":" s","color":"gold"}]',
              'execute if score $tfc mg.st matches 1.. run return 0']
        for i, (y, h, hole) in enumerate(fl, 1):
            L.append(f'execute if score $tff mg.st matches {i} run fill {FX - h} {y} {FZ - h} {FX + h} {y} {FZ + h} minecraft:air replace minecraft:snow_block')
        L += ['tellraw @a[tag=!mg.surv] [{"text":"💥 L\'étage du haut a disparu !","color":"red","bold":true}]',
              'execute as @a[tag=mg.play] at @s run playsound minecraft:block.snow.break master @s ~ ~ ~ 1 0.5',
              'scoreboard players set $tff mg.st 0']
        w(f'var/floor/l{k}/top_check', L)

    disp = lambda name: [f'execute if score $ar mg.st matches {l["k"]} run function mg:var/floor/l{l["k"]}/{name}' for l in LAYOUTS]
    w('var/floor/top_check', ['# Étage du haut (Spleef / Splegg en variante). Généré.'] + disp('top_check'))
    w('var/floor/decay', ['# TNT Run en variante : décroissance sur le sol $ar. Généré.'] + disp('decay'))
    L = ['# Spleef en variante : rétrécissement (étape $ss, intervalle $vsk2). Généré.',
         'scoreboard players add $ss mg.st 1', 'scoreboard players operation $sk mg.st = $vsk2 mg.st']
    for l in LAYOUTS:
        for s in range(1, 11):
            L.append(f'execute if score $ar mg.st matches {l["k"]} if score $ss mg.st matches {s} run function mg:var/floor/l{l["k"]}/shrink_{s}')
    L.append('execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.snow.break master @s ~ ~ ~ 1 0.6')
    w('var/floor/shrink', L)

    w('var/mode/spleef_prepare', floor_prepare(FLOOR_MODES[0], 'snow', [
        'scoreboard players set $vsk1 mg.st 800', 'scoreboard players set $vsk2 mg.st 240',
        'execute if score $dif mg.st matches 1 run scoreboard players set $vsk1 mg.st 1000',
        'execute if score $dif mg.st matches 1 run scoreboard players set $vsk2 mg.st 300',
        'execute if score $dif mg.st matches 3 run scoreboard players set $vsk1 mg.st 600',
        'execute if score $dif mg.st matches 3 run scoreboard players set $vsk2 mg.st 180',
        'execute if score $dif mg.st matches 4 run scoreboard players set $vsk1 mg.st 400',
        'execute if score $dif mg.st matches 4 run scoreboard players set $vsk2 mg.st 120']))
    w('var/mode/spleef_go', ['# Spleef, variante : premier rétrécissement selon la difficulté (après spleef/go). Généré.',
                             'scoreboard players operation $sk mg.st = $vsk1 mg.st'])
    w('var/mode/tntrun_prepare', floor_prepare(FLOOR_MODES[1], 'wool', [
        'scoreboard players set $vdk mg.st 9',
        'execute if score $dif mg.st matches 1 run scoreboard players set $vdk mg.st 12',
        'execute if score $dif mg.st matches 3 run scoreboard players set $vdk mg.st 7',
        'execute if score $dif mg.st matches 4 run scoreboard players set $vdk mg.st 5',
        'scoreboard players operation $dk mg.st = $vdk mg.st']))
    w('var/mode/splegg_prepare', floor_prepare(FLOOR_MODES[2], 'snow', [
        'kill @e[distance=0..,type=minecraft:egg]',
        f'kill @e[type=minecraft:chicken,x={FX - 40},y=40,z={FZ - 40},dx=80,dy=70,dz=80]',
        'scoreboard players set $vrs mg.st 160', 'scoreboard players set $vcr mg.st 0',
        'execute if score $dif mg.st matches 1 run scoreboard players set $vrs mg.st 60',
        'execute if score $dif mg.st matches 3.. run scoreboard players set $vcr mg.st 1',
        'execute if score $dif mg.st matches 4 run scoreboard players set $vrs mg.st 240']))

    w('var/fl', ['# Zones chargées des variantes (sols, centre 0 ~ 24300). Généré.',
                 f'forceload add {FX - 48} {FZ - 48} {FX + 48} {FZ + 48}'])
