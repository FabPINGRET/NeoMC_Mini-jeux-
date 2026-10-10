"""🚗 Autos tamponneuses sur glace — ids 221 (5 coups), 222 (3 coups), 223 (8 coups). Piste ronde de glace en z 37400.

    python tools/arcade/gen_autotamp.py .

Chacun conduit un bateau (invulnérable) sur une piste de glace fermée. Les bateaux se tamponnent avec la physique vanilla.
Un choc = deux bateaux à moins de 2 blocs dont l'un roule vite (≥ 3 blocs/s) : le plus lent est « tamponné » et perd un coup,
le plus rapide marque un point (mg.atp). Un bateau ne peut être touché qu'une fois par seconde.
Plus de coups → éliminé. Le dernier en piste gagne ; au bout de 3 min, le plus de coups restants (puis de points) gagne.
Descendre du bateau (accroupi) : on remonte aussitôt dans un bateau neuf. Seul : entraînement (fin au temps, match nul).
"""
import json
import os
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
GID = 221
Z = C.param('Z', 37400)
RIN = 18                 # rayon de la piste
LIMIT = 3600             # 3 min
WOODS = ['oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'mangrove', 'cherry', 'pale_oak']
BOATS = '@e[type=#mg:at_boats,tag=mg.atb]'

os.makedirs(os.path.join(C.D, 'tags/entity_type'), exist_ok=True)
with open(os.path.join(C.D, 'tags/entity_type/at_boats.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump({'values': [f'minecraft:{x}_boat' for x in WOODS]}, f, indent=2)
    f.write('\n')

# ------------------------------------------------------------------ piste
B = [f'# 🚗 Autos tamponneuses — piste ronde (rayon {RIN}) centrée en 0 64 {Z}']
B += [f'fill -{RIN + 6} {y} {Z - RIN - 6} {RIN + 6} {y} {Z + RIN + 6} minecraft:air' for y in range(62, 76)]
B += [f'fill -{RIN + 5} 63 {Z - RIN - 5} {RIN + 5} 63 {Z + RIN + 5} minecraft:smooth_stone']
for x in range(-RIN - 2, RIN + 3):
    for z in range(-RIN - 2, RIN + 3):
        d = (x * x + z * z) ** 0.5
        if d <= RIN + 0.5:
            blk = 'blue_ice' if (int(d) % 6 == 5) else 'packed_ice'
            if d <= 2.5:
                continue
            B.append(f'setblock {x} 64 {Z + z} minecraft:{blk}')
        elif d <= RIN + 1.6:
            # bordure « pare-chocs » jaune et noire, 2 blocs, barrière invisible au-dessus
            col = 'yellow_concrete' if ((x + z) // 2) % 2 == 0 else 'black_concrete'
            B += [f'setblock {x} 64 {Z + z} minecraft:{col}', f'setblock {x} 65 {Z + z} minecraft:{col}',
                  f'fill {x} 66 {Z + z} {x} 70 {Z + z} minecraft:barrier']
# plot central (petit rond-point qui fait rebondir), lanternes
B += [f'fill -2 64 {Z - 2} 2 65 {Z + 2} minecraft:red_concrete', f'fill -1 66 {Z - 1} 1 66 {Z + 1} minecraft:white_concrete',
      f'setblock 0 67 {Z} minecraft:sea_lantern', f'fill -2 66 {Z - 2} 2 70 {Z + 2} minecraft:barrier replace minecraft:air']
for (xx, zz) in ((RIN + 3, 0), (-RIN - 3, 0), (0, RIN + 3), (0, -RIN - 3), (15, 15), (-15, 15), (15, -15), (-15, -15)):
    B += [f'fill {xx} 64 {Z + zz} {xx} 67 {Z + zz} minecraft:polished_blackstone_wall', f'setblock {xx} 68 {Z + zz} minecraft:lantern']
w('autotamp/build', B)

# ------------------------------------------------------------------ partie
PL = '@a[tag=mg.play]'
SP = []
import math
for k in range(12):
    a = 2 * math.pi * k / 12
    SP.append((round(14 * math.cos(a), 1), round(14 * math.sin(a), 1)))
w('autotamp/prepare', ['# 🚗 Autos tamponneuses — préparation ($atx = coups au départ)', 'function mg:autotamp/build',
                       f'kill {BOATS}', 'kill @e[tag=mg.ats]'] +
  [f'summon minecraft:marker {x} 65 {Z + z} {{Tags:["mg.ats","mg.fx"]}}' for x, z in SP] +
  [f'execute as @e[type=minecraft:marker,tag=mg.ats] at @s run tp @s ~ ~ ~ facing 0 65 {Z}',
   'scoreboard players set $px mg.st 0', 'scoreboard players set $py mg.st 82', f'scoreboard players set $pz mg.st {Z}',
   f'clear {PL}', f'effect clear {PL}', f'gamemode adventure {PL}', f'team join mg_at {PL}', 'tag @e remove mg.atu',
   f'execute as {PL} run function mg:autotamp/place',
   f'scoreboard players operation @a[tag=mg.play] mg.atl = $atx mg.st', 'scoreboard players set @a mg.atp 0',
   'scoreboard players set $att mg.st 0'])
w('autotamp/place', ['# @s : une place libre sur le cercle de départ',
                     'execute unless entity @e[type=minecraft:marker,tag=mg.ats,tag=!mg.atu] run tag @e[tag=mg.ats] remove mg.atu',
                     'tag @e[type=minecraft:marker,tag=mg.ats,tag=!mg.atu,sort=random,limit=1] add mg.atq',
                     'tp @s @e[type=minecraft:marker,tag=mg.atq,limit=1]', 'execute at @s run spawnpoint @s ~ ~ ~',
                     'tag @e[tag=mg.atq] add mg.atu', 'tag @e[tag=mg.atq] remove mg.atq'])
w('autotamp/go', ['# Départ : chacun monte dans son bateau',
                  'scoreboard objectives setdisplay sidebar mg.atl',
                  f'execute as {PL} at @s run function mg:autotamp/boat',
                  f'effect give {PL} minecraft:resistance infinite 4 true', f'effect give {PL} minecraft:saturation infinite 0 true',
                  f'bossbar add mg:autotamp {js({"text": "🚗 Autos tamponneuses", "color": "aqua"})}', 'bossbar set mg:autotamp color blue',
                  f'bossbar set mg:autotamp max {LIMIT}', f'bossbar set mg:autotamp players {PL}',
                  f'tellraw {PL} ' + js([{'text': '🚗 AUTOS TAMPONNEUSES : ', 'color': 'aqua', 'bold': True}, {'text': 'fonce dans les autres ! Chaque fois qu\'on te tamponne (tu roulais moins vite), tu perds un coup ; à 0, éliminé. '
                               'Dernier en piste = victoire. Accroupi = sortir (tu remontes aussitôt).', 'color': 'gray'}])])
w('autotamp/boat', ['# @s : un bateau neuf (bois au hasard) à sa position, lié par mg.atid',
                    'execute unless score @s mg.atid matches 1.. run scoreboard players add $atn mg.st 1',
                    'execute unless score @s mg.atid matches 1.. run scoreboard players operation @s mg.atid = $atn mg.st',
                    'scoreboard players operation $p mg.st = @s mg.atid',
                    f'execute as {BOATS} if score @s mg.atid = $p mg.st run kill @s',
                    'execute store result score $r mg.st run random value 0..8'] +
  [f'execute if score $r mg.st matches {i} run summon minecraft:{wd}_boat ~ ~0.2 ~ {{Tags:["mg.atb","mg.atn"],Invulnerable:1b}}'
   for i, wd in enumerate(WOODS)] +
  ['execute as @e[tag=mg.atn] at @s run rotate @s facing 0 65 ' + str(Z),
   'scoreboard players operation @e[tag=mg.atn] mg.atid = $p mg.st',
   'ride @s mount @e[tag=mg.atn,limit=1]', 'tag @e[tag=mg.atn] remove mg.atn'])
w('autotamp/speed', ['# @s = bateau : vitesse (|dx| + |dz|, centièmes de bloc par tick) depuis le tick précédent',
                     'execute store result score $x mg.st run data get entity @s Pos[0] 100',
                     'execute store result score $z mg.st run data get entity @s Pos[2] 100',
                     'scoreboard players operation $dx mg.st = $x mg.st', 'scoreboard players operation $dx mg.st -= @s mg.atx',
                     'scoreboard players operation $dz mg.st = $z mg.st', 'scoreboard players operation $dz mg.st -= @s mg.atz',
                     'execute if score $dx mg.st matches ..-1 run scoreboard players operation $dx mg.st *= #m1 mg.st',
                     'execute if score $dz mg.st matches ..-1 run scoreboard players operation $dz mg.st *= #m1 mg.st',
                     'scoreboard players operation @s mg.atv = $dx mg.st', 'scoreboard players operation @s mg.atv += $dz mg.st',
                     'execute unless score @s mg.atx matches -2147483648.. run scoreboard players set @s mg.atv 0',
                     'scoreboard players operation @s mg.atx = $x mg.st', 'scoreboard players operation @s mg.atz = $z mg.st',
                     'execute if score @s mg.atc matches 1.. run scoreboard players remove @s mg.atc 1'])
w('autotamp/bump', ['# @s = bateau sans délai : un autre bateau tout près ET plus rapide (≥ 15) → @s est tamponné',
                    'scoreboard players set $ms mg.st 0',
                    f'execute as @e[type=#mg:at_boats,tag=mg.atb,distance=0.01..2] run scoreboard players operation $ms mg.st > @s mg.atv',
                    'execute if score $ms mg.st matches ..14 run return 0',
                    'execute unless score @s mg.atv < $ms mg.st run return 0',
                    'scoreboard players set @s mg.atc 20',
                    # le(s) tamponneur(s) : le plus rapide à côté
                    f'execute as @e[type=#mg:at_boats,tag=mg.atb,distance=0.01..2] if score @s mg.atv = $ms mg.st run function mg:autotamp/pusher',
                    'execute on passengers if entity @s[type=minecraft:player,tag=mg.play] run function mg:autotamp/hit',
                    'execute at @s run particle minecraft:crit ~ ~0.8 ~ 0.6 0.4 0.6 0.4 25 force',
                    'execute at @s run playsound minecraft:entity.zombie.attack_wooden_door master @a ~ ~ ~ 0.9 1.4'])
w('autotamp/pusher', ['# @s = bateau tamponneur', 'scoreboard players set @s mg.atc 20',
                      'execute on passengers if entity @s[type=minecraft:player,tag=mg.play] run scoreboard players add @s mg.atp 1',
                      'execute on passengers if entity @s[type=minecraft:player,tag=mg.play] run title @s actionbar {"text":"💥 Tamponné ! +1","color":"green","bold":true}'])
w('autotamp/hit', ['# @s (joueur) vient d\'être tamponné', 'scoreboard players remove @s mg.atl 1',
                   'title @s actionbar [{"text":"💢 On t\'a tamponné ! Coups restants : ","color":"red"},{"score":{"name":"@s","objective":"mg.atl"},"color":"yellow","bold":true}]',
                   'execute if score @s mg.atl matches ..0 run function mg:autotamp/out'])
w('autotamp/out', ['# @s n\'a plus de coups', 'scoreboard players operation $p mg.st = @s mg.atid',
                   'ride @s dismount', f'execute as {BOATS} if score @s mg.atid = $p mg.st run kill @s',
                   'execute if score $n0 mg.st matches 2.. run return run function mg:core/eliminate',
                   # seul : on recommence
                   'scoreboard players operation @s mg.atl = $atx mg.st', 'function mg:autotamp/place', 'execute at @s run function mg:autotamp/boat'])
w('autotamp/remount', ['# @s (joueur en piste) n\'est plus dans un bateau : nouveau bateau à sa place (dans la piste)',
                       f'execute unless entity @s[x=-{RIN},y=60,z={Z - RIN},dx={2 * RIN},dy=12,dz={2 * RIN}] run function mg:autotamp/place',
                       'execute at @s run function mg:autotamp/boat'])
w('autotamp/tick', ['# 🚗 Autos tamponneuses — tick', 'scoreboard players add $att mg.st 1', 'scoreboard players set #m1 mg.st -1',
                    f'execute store result bossbar mg:autotamp value run scoreboard players get $att mg.st',
                    f'execute as {BOATS} run function mg:autotamp/speed',
                    f'execute as {BOATS} unless score @s mg.atc matches 1.. at @s run function mg:autotamp/bump',
                    f'execute as {PL} unless predicate mg:coaster_riding run function mg:autotamp/remount',
                    # bateaux sans conducteur (joueur déconnecté, éliminé…)
                    f'execute as {BOATS} unless predicate mg:coaster_has_rider run kill @s',
                    'execute store result score $a mg.st if entity ' + PL,
                    'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $a mg.st matches ..1 run return run function mg:autotamp/end',
                    f'execute if score $state mg.st matches 2 if score $att mg.st matches {LIMIT}.. run function mg:autotamp/end'])
w('autotamp/end', ['# Fin : dernier en piste, sinon le plus de coups restants (puis de points)',
                   'execute unless score $state mg.st matches 2 run return 0',
                   'execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] {"text":"🚗 Fin de l\'entraînement.","color":"yellow"}',
                   'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                   'scoreboard players set $bl mg.st -1', 'scoreboard players operation $bl mg.st > @a[tag=mg.play] mg.atl',
                   'tag @a remove mg.atw',
                   'execute as @a[tag=mg.play] if score @s mg.atl = $bl mg.st run tag @s add mg.atw',
                   'scoreboard players set $bp mg.st -1', 'scoreboard players operation $bp mg.st > @a[tag=mg.atw] mg.atp',
                   'execute as @a[tag=mg.atw] unless score @s mg.atp = $bp mg.st run tag @s remove mg.atw',
                   'execute store result score $c mg.st if entity @a[tag=mg.atw]',
                   'execute if score $c mg.st matches 1 as @a[tag=mg.atw,limit=1] run return run function mg:core/win_player',
                   'function mg:core/draw'])
w('autotamp/cleanup', [f'kill {BOATS}', 'kill @e[tag=mg.ats]', 'bossbar remove mg:autotamp', 'team leave @a[team=mg_at]',
                       'tag @a remove mg.atw', 'scoreboard players reset * mg.atl', 'scoreboard players reset * mg.atid',
                       'effect clear @a[tag=mg.play] minecraft:resistance', 'effect clear @a[tag=mg.play] minecraft:saturation'])

C.register([221, 222, 223], 'autotamp', [
    C.announce(221, '', '🚗 AUTOS TAMPONNEUSES', 'aqua', 'sur la glace, 5 coups encaissés et c\'est perdu !'),
    C.announce(222, '', '🚗 AUTOS TAMPONNEUSES', 'aqua', 'sur la glace, 3 coups encaissés et c\'est perdu !'),
    C.announce(223, '', '🚗 AUTOS TAMPONNEUSES', 'aqua', 'sur la glace, 8 coups encaissés et c\'est perdu !')])
C.objectives([('mg.atl', 'dummy {"text":"🚗 Coups restants","color":"aqua","bold":true}'), ('mg.atp', 'dummy'), ('mg.atid', 'dummy'),
              ('mg.atx', 'dummy'), ('mg.atz', 'dummy'), ('mg.atv', 'dummy'), ('mg.atc', 'dummy')])
C.patch('core/load', 'scoreboard objectives add mg.bw trigger',
        ['team add mg_at', 'team modify mg_at friendlyFire false', 'team modify mg_at nametagVisibility always'])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['bossbar remove mg:autotamp', 'team remove mg_at'])
# 221 = 5 coups, 222 = 3 coups, 223 = 8 coups : même jeu, $atx = nombre de coups (fixé avant l'annonce et prepare)
C.patch('core/request', 'execute if score $game mg.st matches 91..92 run scoreboard players set $game mg.st 28', [
    '# Autos tamponneuses : 221 = 5 coups, 222 = 3 coups, 223 = 8 coups → $atx',
    'execute if score $game mg.st matches 221 run scoreboard players set $atx mg.st 5',
    'execute if score $game mg.st matches 222 run scoreboard players set $atx mg.st 3',
    'execute if score $game mg.st matches 223 run scoreboard players set $atx mg.st 8'])
C.forceload([f'# Autos tamponneuses (z {Z})', f'forceload add -{RIN + 6} {Z - RIN - 6} {RIN + 6} {Z + RIN + 6}'])
print('Autos tamponneuses OK')
