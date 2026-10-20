"""Élytra : objets, chargement, construction asynchrone, plateformes et préparation / départ de la partie.
game(W, steps_b, steps_w, sec_keys) écrit les fonctions correspondantes via W (modes de jeu : sky_modes).
"""
import math

from sky_track import N, NS, PAD1, PAD3, PADR, PERCH1, PERCH3, RINGS
from sky_vox import Vox, to_cmds


# =====================================================================================
# Fonctions de jeu
# =====================================================================================
ELY = 'minecraft:elytra[minecraft:custom_data={mg_sky:1b},minecraft:unbreakable={},minecraft:enchantments={"minecraft:binding_curse":1},minecraft:custom_name={"text":"Élytres du ciel","color":"aqua","italic":false}]'
ROCK = 'minecraft:firework_rocket[minecraft:custom_data={mg_sky:1b},minecraft:fireworks={flight_duration:1},minecraft:custom_name={"text":"Fusée du ciel","color":"gold","italic":false}]'
BOW = 'minecraft:bow[minecraft:custom_data={mg_sky:1b},minecraft:unbreakable={},minecraft:enchantments={"minecraft:infinity":1},minecraft:custom_name={"text":"Arc du ciel","color":"red","italic":false}]'
ARROW = 'minecraft:arrow[minecraft:custom_data={mg_sky:1b}]'
WIND = 'minecraft:wind_charge[minecraft:custom_data={mg_sky:1b},minecraft:custom_name={"text":"Charge de vent","color":"aqua","italic":false}]'
SKYITEM = '*[minecraft:custom_data~{mg_sky:1b}]'
ADM = '[{"text":"[Mini-Jeux] ","color":"gold"},{"text":"%s","color":"%s"}]'


# ---- plateformes de départ
def disc(cx, cy, cz, r, blk_fn):
    V = Vox()
    for dx in range(-r - 2, r + 3):
        for dz in range(-r - 2, r + 3):
            d = math.hypot(dx, dz)
            b = blk_fn(d, dx, dz)
            if b:
                V.put(cx + dx, cy, cz + dz, b)
    return V


def pad_lines(c, floor_fn, title):
    cx, cy, cz = c
    V = disc(cx, cy, cz, PADR, floor_fn)
    for y in range(cy + 1, cy + 4):
        for dx in range(-PADR - 2, PADR + 3):
            for dz in range(-PADR - 2, PADR + 3):
                if PADR + 0.5 < math.hypot(dx, dz) <= PADR + 1.5:
                    V.put(cx + dx, y, cz + dz, 'barrier')
    return [f'# {title} (généré)', f'fill {cx-PADR-2} {cy} {cz-PADR-2} {cx+PADR+2} {cy+5} {cz+PADR+2} minecraft:air'] + [c for _, _, c in to_cmds(V.v)]


def pad1_floor(d, dx, dz):
    if d > PADR + 0.5:
        return None
    if d <= 1.2:
        return 'sea_lantern'
    if 3.5 < d <= 4.5:
        return 'light_blue_concrete'
    if d > PADR - 0.5:
        return 'quartz_bricks'
    return 'smooth_quartz'


def pad3_floor(d, dx, dz):
    if d > PADR + 0.5:
        return None
    if d <= 1.2:
        return 'sea_lantern'
    if 3.5 < d <= 4.5:
        return 'cyan_stained_glass'
    if d > PADR - 0.5:
        return 'waxed_oxidized_cut_copper'
    return 'light_blue_stained_glass'


FL1 = f'{PAD1[0]-16} {PAD1[2]-16} {PAD1[0]+16} {PAD1[2]+16}'
FL3 = f'{PAD3[0]-16} {PAD3[2]-16} {PAD3[0]+16} {PAD3[2]+16}'

DISPT = 'transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[%sf,%sf,%sf]}'

RULES = {
    1: f'[{{"text":"🪽 COURSE D\'ANNEAUX : ","color":"aqua","bold":true}},{{"text":"saute, ouvre tes élytres (Espace en l\'air) et traverse les {N} anneaux DANS L\'ORDRE — la traînée lumineuse montre le suivant. Anneaux dorés = +1 fusée. Le premier arrivé gagne (4 min max).","color":"gray","bold":false}}]',
    2: f'[{{"text":"🏹 COURSE + COMBAT : ","color":"red","bold":true}},{{"text":"même course de {N} anneaux, mais arc et charges de vent (rechargées toutes les 15 s) ! Un rival touché est sonné : ses élytres disparaissent 1,5 s. Personne ne meurt. Le premier arrivé gagne.","color":"gray","bold":false}}]',
    3: '[{"text":"🌪 SURVIE EN VOL : ","color":"light_purple","bold":true},{"text":"reste en l\'air ! Te poser, tomber sous l\'arène ou rester 3 s hors de la zone (cercle rouge qui rétrécit) = éliminé. Une fusée toutes les 8 s, colonnes de vent = élan vers le haut. La plateforme s\'effondre au bout de 10 s. Dernier en vol gagne.","color":"gray","bold":false}]',
}


def game(W, steps_b, steps_w, sec_keys):
    W('load', ['# Élytra : objectifs (à appeler depuis core/load)',
               'scoreboard objectives add mg.skr dummy [{"text":"🪽 Anneaux","color":"aqua","bold":true}]',
               'scoreboard objectives add mg.sks dummy [{"text":"🪽 Survivants","color":"aqua","bold":true}]',
               'scoreboard objectives add mg.skg dummy',
               'scoreboard objectives add mg.skst dummy',
               'scoreboard objectives add mg.skl dummy',
               'scoreboard objectives add mg.sko dummy'])
    W('remove', ['# Élytra : désinstallation (à appeler depuis mg:desinstaller)',
                 'scoreboard objectives remove mg.skr',
                 'scoreboard objectives remove mg.sks',
                 'scoreboard objectives remove mg.skg',
                 'scoreboard objectives remove mg.skst',
                 'scoreboard objectives remove mg.skl',
                 'scoreboard objectives remove mg.sko',
                 f'schedule clear {NS}/b_next',
                 f'schedule clear {NS}/pad_wait',
                 f'function {NS}/fl_secs_off',
                 f'function {NS}/pad_fl_off',
                 'data remove storage mg:sky built',
                 'data remove storage mg:sky z',
                 'advancement revoke @a only mg:sky/hurt'])

    # ---- construction asynchrone
    W('build', ['# (OP) Construit le parcours Élytra (modes 1-2) et l\'arène de survie (mode 3), section par section (asynchrone)',
                f'execute if score $skbm mg.st matches 1.. run return run tellraw @a[tag=mg.admin] {ADM % ("Élytra : construction déjà en cours.", "yellow")}',
                'scoreboard players set $skbm mg.st 1',
                'scoreboard players set $skbs mg.st 0',
                'scoreboard players set $skw mg.st 0',
                f'scoreboard players set $skbn mg.st {len(steps_b)}',
                f'tellraw @a[tag=mg.admin] {ADM % ("Élytra : construction du décor (" + str(len(sec_keys)) + " sections)...", "gray")}',
                f'schedule function {NS}/b_next 1t'])
    W('wipe', ['# (OP) Efface tout le décor Élytra (pour reconstruire après une modification du générateur)',
               f'execute if score $skbm mg.st matches 1.. run return run tellraw @a[tag=mg.admin] {ADM % ("Élytra : construction en cours, réessaie plus tard.", "yellow")}',
               'data remove storage mg:sky built',
               'scoreboard players set $skbm mg.st 2',
               'scoreboard players set $skbs mg.st 0',
               'scoreboard players set $skw mg.st 0',
               f'scoreboard players set $skbn mg.st {len(steps_w)}',
               f'schedule function {NS}/b_next 1t'])
    W('b_next', ['# Construction / effacement : une étape par tick (attente du chargement des tronçons)',
                 'scoreboard players set $skok mg.st 0',
                 f'execute if score $skbm mg.st matches 1 store result score $skok mg.st run function {NS}/b_step',
                 f'execute if score $skbm mg.st matches 2 store result score $skok mg.st run function {NS}/w_step',
                 'execute if score $skok mg.st matches 1 run scoreboard players set $skw mg.st 0',
                 'execute if score $skok mg.st matches 1 run scoreboard players add $skbs mg.st 1',
                 'execute if score $skok mg.st matches 0 run scoreboard players add $skw mg.st 1',
                 f'execute if score $skw mg.st matches 400.. run return run function {NS}/b_fail',
                 f'execute if score $skbs mg.st >= $skbn mg.st run return run function {NS}/b_done',
                 f'schedule function {NS}/b_next 1t'])
    W('b_done', ['# Fin de la construction (ou de l\'effacement)',
                 f'function {NS}/fl_secs_off',
                 'execute if score $skbm mg.st matches 1 run data modify storage mg:sky built set value 1b',
                 f'execute if score $skbm mg.st matches 1 run tellraw @a[tag=mg.admin] {ADM % ("Élytra : parcours d\'anneaux et arène de survie construits.", "green")}',
                 f'execute if score $skbm mg.st matches 2 run tellraw @a[tag=mg.admin] {ADM % ("Élytra : décor effacé.", "gray")}',
                 'scoreboard players set $skbm mg.st 0'])
    W('b_fail', ['# Zone jamais chargée : abandon propre',
                 f'function {NS}/fl_secs_off',
                 'scoreboard players set $skbm mg.st 0',
                 f'tellraw @a[tag=mg.admin] {ADM % ("Élytra : zone pas chargée, construction interrompue (relance mg:sky/build).", "red")}'])

    W('pad1', pad_lines(PAD1, pad1_floor, 'Plateforme de départ de la course (sol + barrière)'))
    W('pad3', pad_lines(PAD3, pad3_floor, 'Plateforme de décollage de l\'arène (sol + barrière)'))
    for nm, (cx, cy, cz) in (('pad1', PAD1), ('pad3', PAD3)):
        W(f'{nm}_open', [f'# Barrière retirée (GO)', f'fill {cx-PADR-2} {cy+1} {cz-PADR-2} {cx+PADR+2} {cy+3} {cz+PADR+2} minecraft:air replace minecraft:barrier'])
        W(f'{nm}_ld', ['# 1 si la plateforme est chargée'] +
          [f'execute unless loaded {cx+a} {cy} {cz+b} run return fail' for a in (-8, 8) for b in (-8, 8)] + ['return 1'])
    cx, cy, cz = PAD3
    W('pad3_off', ['# Mode 3 : la plateforme de décollage s\'effondre',
                   f'fill {cx-PADR-2} {cy} {cz-PADR-2} {cx+PADR+2} {cy+3} {cz+PADR+2} minecraft:air',
                   f'particle minecraft:cloud {cx} {cy} {cz} 4 0.5 4 0.05 120 force @a',
                   f'execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.glass.break master @s ~ ~ ~ 1 0.7',
                   'scoreboard players set $skpo mg.st 0',
                   'title @a[tag=mg.play] actionbar [{"text":"La plateforme s\'est effondrée : reste en l\'air !","color":"red"}]'])
    W('pad_fl_off', ['# Chargements temporaires des plateformes retirés', f'forceload remove {FL1}', f'forceload remove {FL3}'])

    r1 = RINGS[0]
    W('pad_wait', ['# Attend le chargement de la plateforme du mode puis y place les joueurs',
                   'execute unless score $game mg.st matches 74 run return 0',
                   'execute unless score $state mg.st matches 1..2 run return 0',
                   f'execute if score $elm mg.st matches 1..2 if function {NS}/pad1_ld run return run function {NS}/pad_place',
                   f'execute if score $elm mg.st matches 3 if function {NS}/pad3_ld run return run function {NS}/pad_place',
                   'scoreboard players add $skpw mg.st 1',
                   f'execute if score $skpw mg.st matches 60.. run return run function {NS}/pad_place',
                   f'schedule function {NS}/pad_wait 2t'])

    W('pad_place', ['# Plateforme posée, joueurs répartis dessus (gelés par le compte à rebours)',
                    'scoreboard players set $skpd mg.st 1',
                    'kill @e[tag=mg.sky]',
                    f'execute if score $elm mg.st matches 1..2 run function {NS}/pad1',
                    f'execute if score $elm mg.st matches 3 run function {NS}/pad3',
                    'scoreboard players set $skok mg.st 0',
                    f'execute if score $elm mg.st matches 1..2 store success score $skok mg.st run spreadplayers {PAD1[0]} {PAD1[2]} 1 4 under {PAD1[1]+2} false @a[tag=mg.play]',
                    f'execute if score $elm mg.st matches 3 store success score $skok mg.st run spreadplayers {PAD3[0]} {PAD3[2]} 1 4 under {PAD3[1]+2} false @a[tag=mg.play]',
                    f'execute if score $skok mg.st matches 0 if score $elm mg.st matches 1..2 run tp @a[tag=mg.play] {PAD1[0]+.5} {PAD1[1]+1} {PAD1[2]+.5}',
                    f'execute if score $skok mg.st matches 0 if score $elm mg.st matches 3 run tp @a[tag=mg.play] {PAD3[0]+.5} {PAD3[1]+1} {PAD3[2]+.5}',
                    f'execute if score $elm mg.st matches 1..2 as @a[tag=mg.play] at @s run tp @s ~ ~ ~ facing {r1[0]+.5} {r1[1]+.5} {r1[2]+.5}',
                    f'execute if score $elm mg.st matches 3 as @a[tag=mg.play] at @s run tp @s ~ ~ ~ facing {PAD3[0]+.5} {PAD3[1]-10} {PAD3[2]+60}',
                    f'execute if score $elm mg.st matches 1..2 run spawnpoint @a[tag=mg.play] {PAD1[0]} {PAD1[1]+1} {PAD1[2]}',
                    f'execute if score $elm mg.st matches 3 run spawnpoint @a[tag=mg.play] {PAD3[0]} {PAD3[1]+1} {PAD3[2]}',
                    f'execute if score $elm mg.st matches 1 run summon minecraft:text_display {PAD1[0]+.5} {PAD1[1]+5} {PAD1[2]+.5} {{Tags:["mg.fx","mg.sky"],billboard:"center",background:0,text:[{{"text":"🪽 COURSE D\'ANNEAUX","color":"aqua","bold":true}},{{"text":"\\n{N} anneaux dans l\'ordre — suis la traînée lumineuse","color":"gray","bold":false}}],{DISPT % (1.3, 1.3, 1.3)}}}',
                    f'execute if score $elm mg.st matches 2 run summon minecraft:text_display {PAD1[0]+.5} {PAD1[1]+5} {PAD1[2]+.5} {{Tags:["mg.fx","mg.sky"],billboard:"center",background:0,text:[{{"text":"🏹 COURSE + COMBAT","color":"red","bold":true}},{{"text":"\\n{N} anneaux — abats tes rivaux à l\'arc et à la charge de vent","color":"gray","bold":false}}],{DISPT % (1.3, 1.3, 1.3)}}}',
                    f'execute if score $elm mg.st matches 3 run summon minecraft:text_display {PAD3[0]+.5} {PAD3[1]+5} {PAD3[2]+.5} {{Tags:["mg.fx","mg.sky"],billboard:"center",background:0,text:[{{"text":"🌪 SURVIE EN VOL","color":"light_purple","bold":true}},{{"text":"\\nNe te pose jamais — reste dans la zone","color":"gray","bold":false}}],{DISPT % (1.3, 1.3, 1.3)}}}'])

    # ---- préparation / départ
    W('prepare', ['# Élytra — préparation ($elm : 1 course d\'anneaux, 2 course + combat, 3 survie en vol)',
                  'execute unless score $elm mg.st matches 1..3 run scoreboard players set $elm mg.st 1',
                  f'execute unless data storage mg:sky {{built:1b}} run tellraw @a [{{"text":"🪽 Le décor Élytra n\'est pas encore construit : il apparaît pendant la partie (les anneaux comptent déjà).","color":"yellow"}}]',
                  f'execute unless data storage mg:sky {{built:1b}} run function {NS}/build',
                  'scoreboard players set #-1 mg.st -1',
                  'scoreboard players set #2 mg.st 2',
                  'scoreboard players set #5 mg.st 5',
                  'scoreboard players set #10 mg.st 10',
                  'scoreboard players set #11 mg.st 11',
                  'scoreboard players set #20 mg.st 20',
                  'scoreboard players set #72 mg.st 72',
                  'scoreboard players set #160 mg.st 160',
                  'scoreboard players reset * mg.skr',
                  'scoreboard players reset * mg.sks',
                  'scoreboard players reset * mg.skst',
                  'scoreboard players reset * mg.skl',
                  'scoreboard players reset * mg.sko',
                  'tag @a remove mg.skf',
                  'tag @a remove mg.skstun',
                  'tag @a remove mg.skak',
                  'tag @a remove mg.skv',
                  'tag @a remove mg.skw',
                  'execute if score $elm mg.st matches 1..2 run scoreboard players set @a[tag=mg.play] mg.skr 0',
                  'execute if score $elm mg.st matches 3 run scoreboard players set @a[tag=mg.play] mg.sks 0',
                  'scoreboard players set @a[tag=mg.play] mg.skg -40',
                  'scoreboard players set @a[tag=mg.play] mg.skst 0',
                  'scoreboard players set @a[tag=mg.play] mg.skl 0',
                  'scoreboard players set @a[tag=mg.play] mg.sko 0',
                  'scoreboard players set $skt mg.st 0',
                  'scoreboard players set $skpd mg.st 0',
                  'scoreboard players set $skpw mg.st 0',
                  'scoreboard players set $skpo mg.st 1',
                  'advancement revoke @a only mg:sky/hurt',
                  f'execute if score $elm mg.st matches 1..2 run scoreboard players set $px mg.st {PERCH1[0]}',
                  f'execute if score $elm mg.st matches 1..2 run scoreboard players set $py mg.st {PERCH1[1]}',
                  f'execute if score $elm mg.st matches 1..2 run scoreboard players set $pz mg.st {PERCH1[2]}',
                  f'execute if score $elm mg.st matches 3 run scoreboard players set $px mg.st {PERCH3[0]}',
                  f'execute if score $elm mg.st matches 3 run scoreboard players set $py mg.st {PERCH3[1]}',
                  f'execute if score $elm mg.st matches 3 run scoreboard players set $pz mg.st {PERCH3[2]}',
                  'gamemode adventure @a[tag=mg.play]',
                  'clear @a[tag=mg.play]',
                  'effect clear @a[tag=mg.play] minecraft:levitation',
                  f'item replace entity @a[tag=mg.play] armor.chest with {ELY}',
                  f'execute if score $elm mg.st matches 1..2 run forceload add {FL1}',
                  f'execute if score $elm mg.st matches 3 run forceload add {FL3}',
                  f'schedule function {NS}/pad_wait 2t'])

    W('go', ['# Élytra — départ',
             f'execute if score $skpd mg.st matches 0 run function {NS}/pad_place',
             'scoreboard players set $skt mg.st 0',
             'effect give @a[tag=mg.play] minecraft:resistance infinite 4 true',
             'effect give @a[tag=mg.play] minecraft:saturation infinite 0 true',
             'scoreboard players set @a[tag=mg.play] mg.skg -40',
             f'execute if score $elm mg.st matches 1..2 run function {NS}/go_race',
             f'execute if score $elm mg.st matches 3 run function {NS}/go_surv',
             'execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.ender_dragon.flap master @s ~ ~ ~ 1 1.2'])
    W('go_race', ['# Modes 1-2 : barrière ouverte, fusées (+ arc et charges de vent en mode 2)',
                  f'function {NS}/pad1_open',
                  f'give @a[tag=mg.play] {ROCK} 3',
                  f'execute if score $elm mg.st matches 2 run give @a[tag=mg.play] {BOW}',
                  f'execute if score $elm mg.st matches 2 run give @a[tag=mg.play] {ARROW}',
                  f'execute if score $elm mg.st matches 2 run give @a[tag=mg.play] {WIND} 3',
                  'scoreboard players set $skwt mg.st 0',
                  'scoreboard objectives setdisplay sidebar mg.skr',
                  f'execute if score $elm mg.st matches 1 run tellraw @a[tag=mg.play] {RULES[1]}',
                  f'execute if score $elm mg.st matches 2 run tellraw @a[tag=mg.play] {RULES[2]}'])
    W('go_surv', ['# Mode 3 : barrière ouverte, fusées, zone de 70 blocs',
                  f'function {NS}/pad3_open',
                  f'give @a[tag=mg.play] {ROCK} 2',
                  'scoreboard players set $skz mg.st 700',
                  'data modify storage mg:sky z.r set value 70.0d',
                  'scoreboard players set $skpo mg.st 1',
                  'scoreboard objectives setdisplay sidebar mg.sks',
                  f'tellraw @a[tag=mg.play] {RULES[3]}'])

    W('tick', ['# Élytra — tick de partie (état 2)',
               'scoreboard players add $skt mg.st 1',
               'scoreboard players operation $skp mg.st = $skt mg.st',
               'scoreboard players operation $skp mg.st %= #2 mg.st',
               f'execute if score $elm mg.st matches 1..2 run function {NS}/t_race',
               f'execute if score $elm mg.st matches 3 run function {NS}/t_surv'])
