"""Élytra : les trois modes (course d'anneaux, combat, survie en vol) et le nettoyage de fin de partie.
modes(W, OUT) écrit les fonctions correspondantes via W ; OUT est le dossier de sortie (sous-dossier rk/).
"""
import os

from sky_game import ELY, ROCK, SKYITEM, WIND
from sky_shapes import COL_R, COL_Y0, COL_Y1, COLS
from sky_track import ARENA, AXES, FLOOR3, N, NS, PAD1, PAD3, PATH, RINGS, ZONE


SPLIT = ['scoreboard players operation $es mg.st = $skt mg.st', 'scoreboard players operation $es mg.st /= #20 mg.st',
         'scoreboard players operation $ecs mg.st = $skt mg.st', 'scoreboard players operation $ecs mg.st %= #20 mg.st',
         'scoreboard players operation $ecs mg.st *= #5 mg.st']


def tparts(col):
    T = '{"score":{"name":"$es","objective":"mg.st"},"color":"%s"},{"text":",","color":"%s"}' % (col, col)
    return (f'{T},{{"text":"0","color":"{col}"}},{{"score":{{"name":"$ecs","objective":"mg.st"}},"color":"{col}"}}',
            f'{T},{{"score":{{"name":"$ecs","objective":"mg.st"}},"color":"{col}"}}')


def modes(W, OUT):
    # ---- course (modes 1-2)
    W('t_race', ['# Modes 1-2 : chrono, joueurs, combat, limite de 4 minutes'] + SPLIT + [
        f'execute as @a[tag=mg.play] at @s run function {NS}/r_player',
        f'execute if score $elm mg.st matches 2 run function {NS}/t_combat',
        'execute if score $skt mg.st matches 3600 run tellraw @a[tag=mg.play] [{"text":"🪽 Plus qu\'une minute !","color":"gold"}]',
        f'execute if score $state mg.st matches 2 if score $skt mg.st matches 4800.. run function {NS}/r_timeout',
        'execute if score $state mg.st matches 2 unless entity @a[tag=mg.play] run function mg:core/draw'])

    zx, zy, zz, zdx, zdy, zdz = ZONE
    W('r_player', ['# Course, chaque tick (@s = participant, positionné)',
                   'execute if entity @s[tag=mg.skf] run return 0',
                   '# Compteur « pas en vol plané » (négatif = délai de grâce)',
                   'scoreboard players add @s mg.skg 1',
                   'execute if score @s mg.skg matches 1.. if predicate mg:gliding run scoreboard players set @s mg.skg 0',
                   f'execute if entity @s[x={PAD1[0]-8},y={PAD1[1]},z={PAD1[2]-8},dx=16,dy=6,dz=16] run scoreboard players set @s mg.skg -40',
                   'execute if entity @s[tag=mg.skstun] run scoreboard players set @s mg.skg -30',
                   f'execute if score @s mg.skg matches 20.. run return run function {NS}/rescue',
                   f'execute unless entity @s[x={zx},y={zy},z={zz},dx={zdx},dy={zdy},dz={zdz}] run return run function {NS}/rescue',
                   f'function {NS}/r_hud']
      + [f'execute if score @s mg.skr matches {k} run return run function {NS}/rk/r{k}' for k in range(N)])

    a, b2 = tparts('white')
    W('r_hud', ['# Chrono et progression (@s)',
                f'execute if score $ecs mg.st matches ..9 if score $elm mg.st matches 1 run title @s actionbar [{{"text":"⏱ ","color":"aqua"}},{a},{{"text":" s   ◎ ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.skr"}},"color":"aqua"}},{{"text":"/{N}","color":"gray"}}]',
                f'execute if score $ecs mg.st matches 10.. if score $elm mg.st matches 1 run title @s actionbar [{{"text":"⏱ ","color":"aqua"}},{b2},{{"text":" s   ◎ ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.skr"}},"color":"aqua"}},{{"text":"/{N}","color":"gray"}}]',
                f'execute if score $ecs mg.st matches ..9 if score $elm mg.st matches 2 unless entity @s[tag=mg.skstun] run title @s actionbar [{{"text":"⏱ ","color":"aqua"}},{a},{{"text":" s   ◎ ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.skr"}},"color":"aqua"}},{{"text":"/{N}   💨 recharge dans ","color":"gray"}},{{"score":{{"name":"$skws","objective":"mg.st"}},"color":"aqua"}},{{"text":" s","color":"gray"}}]',
                f'execute if score $ecs mg.st matches 10.. if score $elm mg.st matches 2 unless entity @s[tag=mg.skstun] run title @s actionbar [{{"text":"⏱ ","color":"aqua"}},{b2},{{"text":" s   ◎ ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.skr"}},"color":"aqua"}},{{"text":"/{N}   💨 recharge dans ","color":"gray"}},{{"score":{{"name":"$skws","objective":"mg.st"}},"color":"aqua"}},{{"text":" s","color":"gray"}}]',
                'execute if entity @s[tag=mg.skstun] run title @s actionbar [{"text":"💫 Sonné ! Élytres de retour dans un instant...","color":"red"}]'])

    os.makedirs(os.path.join(OUT, 'rk'), exist_ok=True)
    for k in range(N):
        x, y, z, size, kind = RINGS[k]
        h = size // 2 - 1
        if AXES[k] == 'x':
            box = f'x={x-2},y={y-h},z={z-h},dx=4,dy={2*h},dz={2*h}'
        else:
            box = f'x={x-h},y={y-h},z={z-2},dx={2*h},dy={2*h},dz=4'
        prev = PATH[k]
        floor = max(ZONE[1], min(prev[1], y) - 32)
        col = 'wax_on' if kind == 'b' else 'end_rod'
        W(f'rk/r{k}', [f'# Vers l\'anneau {k+1}/{N} (@s, {RINGS[k][4]}) : passage, plancher, traînée (généré)',
                       f'execute if entity @s[{box}] run return run function {NS}/pass',
                       f'execute unless entity @s[y={floor},dy=400] run return run function {NS}/rescue',
                       f'execute if score $skp mg.st matches 0 anchored eyes facing {x+.5} {y+.5} {z+.5} run function {NS}/trail',
                       f'execute if score $skp mg.st matches 0 run particle minecraft:{col} {x+.5} {y+.5} {z+.5} {h*.5:.1f} {h*.5:.1f} {h*.5:.1f} 0.01 4 force @s'])
    W('trail', ['# Traînée lumineuse vers l\'anneau suivant (@s, orienté vers l\'anneau, vue par @s seul)']
      + [f'particle minecraft:end_rod ^ ^-0.4 ^{d} 0 0 0 0 1 force @s' for d in range(3, 17, 2)])

    boosts = [i + 1 for i, r in enumerate(RINGS) if r[4] == 'b']
    W('pass', ['# Anneau franchi (@s)',
               'scoreboard players add @s mg.skr 1',
               'playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.5',
               'particle minecraft:totem_of_undying ~ ~ ~ 0.6 0.6 0.6 0.3 15 force @s']
      + [f'execute if score @s mg.skr matches {b} run function {NS}/boost' for b in boosts]
      + [f'execute if score @s mg.skr matches {N}.. run return run function {NS}/finish'])
    W('boost', ['# Anneau doré (@s) : une fusée de plus',
                f'give @s {ROCK} 1',
                'playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.8 1.6',
                'title @s subtitle [{"text":"🚀 +1 fusée !","color":"gold","bold":true}]',
                'title @s title [{"text":" "}]'])

    resc = ['# Remise en selle (@s) : au-dessus du dernier anneau franchi, orienté vers le suivant (généré)',
            f'execute if score @s mg.skr matches 0 run tp @s {PAD1[0]+.5} {PAD1[1]+1} {PAD1[2]+.5} facing {RINGS[0][0]+.5} {RINGS[0][1]+.5} {RINGS[0][2]+.5}']
    for k in range(1, N):
        x, y, z, size, _ = RINGS[k - 1]
        nx, ny, nz = RINGS[k][:3]
        resc.append(f'execute if score @s mg.skr matches {k} run tp @s {x+.5} {y + size // 2 + 3} {z+.5} facing {nx+.5} {ny+.5} {nz+.5}')
    resc += [f'execute if entity @s[tag=mg.skstun] run function {NS}/unstun',
             'effect give @s minecraft:slow_falling 2 0 true',
             'scoreboard players set @s mg.skg -40',
             'title @s subtitle [{"text":"Appuie sur Espace pour replaner !","color":"yellow"}]',
             'title @s title [{"text":"↺","color":"aqua","bold":true}]',
             'playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 0.7 1.3']
    W('rescue', resc)

    a, b2 = tparts('gold')
    W('finish', ['# Arrivée (@s) : temps, record du serveur (mode 1), victoire'] + SPLIT + [
        'tag @s add mg.skf',
        'effect give @s minecraft:slow_falling 30 0 true',
        'title @s title [{"text":"🏁 Arrivée !","color":"gold","bold":true}]',
        f'execute if score $ecs mg.st matches ..9 run tellraw @a[tag=!mg.surv] [{{"text":"🏁 ","color":"gold"}},{{"selector":"@s","color":"yellow"}},{{"text":" boucle la course en ","color":"gray"}},{a},{{"text":" s","color":"gold"}}]',
        f'execute if score $ecs mg.st matches 10.. run tellraw @a[tag=!mg.surv] [{{"text":"🏁 ","color":"gold"}},{{"selector":"@s","color":"yellow"}},{{"text":" boucle la course en ","color":"gray"}},{b2},{{"text":" s","color":"gold"}}]',
        'execute unless score $skrec mg.st matches 1.. run scoreboard players set $skrec mg.st 999999',
        f'execute if score $elm mg.st matches 1 if score $skt mg.st < $skrec mg.st run function {NS}/record',
        'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. run effect give @a[tag=mg.play] minecraft:slow_falling 15 0 true',
        'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. run return run function mg:core/win_player',
        'tellraw @s [{"text":"(Mode test solo : menu → Arrêter pour finir)","color":"dark_gray","italic":true}]'])
    W('record', ['# Nouveau record du serveur, course d\'anneaux (@s ; $es / $ecs déjà calculés)',
                 'scoreboard players operation $skrec mg.st = $skt mg.st',
                 f'execute if score $ecs mg.st matches ..9 run tellraw @a [{{"text":"🏆 ","color":"gold"}},{{"selector":"@s","color":"yellow","bold":true}},{{"text":" bat le record de la course Élytra : ","color":"gray"}},{a},{{"text":" s !","color":"gold"}}]',
                 f'execute if score $ecs mg.st matches 10.. run tellraw @a [{{"text":"🏆 ","color":"gold"}},{{"selector":"@s","color":"yellow","bold":true}},{{"text":" bat le record de la course Élytra : ","color":"gray"}},{b2},{{"text":" s !","color":"gold"}}]',
                 'function mg:hall/ely {key:"elyg",lbl:"🪽 Record Élytra : course"}'])
    W('r_timeout', ['# 4 minutes écoulées : le plus avancé gagne',
                    'tellraw @a[tag=mg.play] [{"text":"🪽 Temps écoulé : le plus avancé l\'emporte !","color":"gold"}]',
                    'effect give @a[tag=mg.play] minecraft:slow_falling 15 0 true',
                    'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                    'scoreboard players set $skmx mg.st -1',
                    'execute as @a[tag=mg.play] run scoreboard players operation $skmx mg.st > @s mg.skr',
                    'execute if score $skmx mg.st matches ..0 run return run function mg:core/draw',
                    'tag @a remove mg.skw',
                    'execute as @a[tag=mg.play] if score @s mg.skr = $skmx mg.st run tag @s add mg.skw',
                    'execute as @a[tag=mg.skw,sort=random,limit=1] run function mg:core/win_player',
                    'tag @a remove mg.skw'])

    # ---- combat (mode 2)
    W('t_combat', ['# Mode 2 : sonnés, recharge des charges de vent, détonation de proximité des charges',
                   'scoreboard players remove @a[scores={mg.skst=1..}] mg.skst 1',
                   f'execute as @a[tag=mg.skstun,scores={{mg.skst=..0}}] run function {NS}/unstun',
                   'scoreboard players add $skwt mg.st 1',
                   f'execute if score $skwt mg.st matches 300.. run function {NS}/wc_refill',
                   'scoreboard players set $skws mg.st 300',
                   'scoreboard players operation $skws mg.st -= $skwt mg.st',
                   'scoreboard players operation $skws mg.st /= #20 mg.st',
                   f'execute as @e[type=minecraft:wind_charge,x={zx-20},y=60,z={zz-20},dx={zdx+40},dy=240,dz={zdz+40}] at @s run function {NS}/wc_check'])
    W('wc_refill', ['# Toutes les 15 s : 3 charges de vent',
                    'scoreboard players set $skwt mg.st 0',
                    f'clear @a[tag=mg.play] minecraft:wind_charge[minecraft:custom_data~{{mg_sky:1b}}]',
                    f'give @a[tag=mg.play] {WIND} 3',
                    'execute as @a[tag=mg.play] at @s run playsound minecraft:item.armor.equip_elytra master @s ~ ~ ~ 0.6 1.6'])
    W('wc_check', ['# Charge de vent (@s) : explose au contact d\'un rival (à 3,5 blocs)',
                   'execute unless entity @a[tag=mg.play,distance=..3.5] run return 0',
                   'tag @a remove mg.skak',
                   'execute on origin run tag @s add mg.skak',
                   'execute as @a[tag=mg.play,tag=!mg.skak,tag=!mg.skstun,distance=..3.5,sort=nearest,limit=1] run tag @s add mg.skv',
                   'execute unless entity @a[tag=mg.skv] run return run tag @a remove mg.skak',
                   'particle minecraft:gust_emitter_small ~ ~ ~ 0 0 0 0 1 force @a',
                   'playsound minecraft:entity.wind_charge.wind_burst master @a ~ ~ ~ 1.5 1',
                   f'execute as @a[tag=mg.skv] run function {NS}/stun',
                   'tag @a remove mg.skv',
                   'tag @a remove mg.skak',
                   'kill @s'])
    W('hurt_adv', ['# Touché par une flèche ou une charge de vent d\'un joueur (@s = victime) — avancement mg:sky/hurt',
                   'advancement revoke @s only mg:sky/hurt',
                   'execute unless score $game mg.st matches 74 run return 0',
                   'execute unless score $state mg.st matches 2 run return 0',
                   'execute unless score $elm mg.st matches 2 run return 0',
                   'execute unless entity @s[tag=mg.play] run return 0',
                   'tag @a remove mg.skak',
                   'execute on attacker run tag @s[tag=mg.play] add mg.skak',
                   'execute if entity @s[tag=mg.skak] run return run tag @a remove mg.skak',
                   f'function {NS}/stun',
                   'tag @a remove mg.skak'])
    W('stun', ['# Rival touché (@s = victime ; tireur tagué mg.skak s\'il est connu) : élytres retirées 1,5 s',
               'execute if entity @s[tag=mg.skstun] run return 0',
               'execute if entity @s[tag=mg.skf] run return 0',
               'tag @s add mg.skstun',
               'scoreboard players set @s mg.skst 30',
               'item replace entity @s armor.chest with minecraft:air',
               'execute if entity @a[tag=mg.skak] run tellraw @a[tag=!mg.surv] [{"text":"🏹 ","color":"red"},{"selector":"@a[tag=mg.skak,limit=1]","color":"yellow"},{"text":" a abattu ","color":"gray"},{"selector":"@s","color":"yellow"},{"text":" !","color":"gray"}]',
               'execute unless entity @a[tag=mg.skak] run tellraw @a[tag=!mg.surv] [{"text":"🏹 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" est abattu !","color":"gray"}]',
               'title @s subtitle [{"text":"Tes élytres reviennent dans 1,5 s","color":"gray"}]',
               'title @s title [{"text":"💫 Sonné !","color":"red","bold":true}]',
               'playsound minecraft:entity.player.hurt master @s ~ ~ ~ 1 0.8',
               'execute at @s run particle minecraft:crit ~ ~1 ~ 0.4 0.6 0.4 0.3 25 force @a',
               'execute as @a[tag=mg.skak] at @s run playsound minecraft:entity.arrow.hit_player master @s ~ ~ ~ 1 1'])
    W('unstun', ['# Fin de l\'étourdissement (@s) : élytres rendues',
                 'tag @s remove mg.skstun',
                 'scoreboard players set @s mg.skst 0',
                 'execute unless entity @s[tag=mg.play] run return 0',
                 f'item replace entity @s armor.chest with {ELY}',
                 'scoreboard players set @s mg.skg -30',
                 'title @s subtitle [{"text":"Élytres rendues : appuie sur Espace !","color":"yellow","bold":true}]',
                 'title @s title [{"text":" "}]',
                 'playsound minecraft:item.armor.equip_elytra master @s ~ ~ ~ 1 1.2'])

    # ---- survie en vol (mode 3)
    ax0, az0 = ARENA
    W('t_surv', ['# Mode 3 : plateforme, zone, joueurs, colonnes de vent, fusées, fin',
                 'execute if score $skt mg.st matches 140 run title @a[tag=mg.play] actionbar [{"text":"⚠ La plateforme s\'effondre dans 3 s !","color":"red","bold":true}]',
                 f'execute if score $skt mg.st matches 200 run function {NS}/pad3_off',
                 '# Rayon de la zone (dixièmes de bloc) : 700 → 150 en 3 minutes',
                 f'execute if score $skt mg.st matches ..3600 run function {NS}/s_zone',
                 'scoreboard players operation $skp5 mg.st = $skt mg.st',
                 'scoreboard players operation $skp5 mg.st %= #5 mg.st',
                 'scoreboard players operation $skfw mg.st = $skt mg.st',
                 'scoreboard players operation $skfw mg.st %= #160 mg.st',
                 'scoreboard players set $skfs mg.st 160',
                 'scoreboard players operation $skfs mg.st -= $skfw mg.st',
                 'scoreboard players operation $skfs mg.st /= #20 mg.st',
                 'scoreboard players operation $skzr mg.st = $skz mg.st',
                 'scoreboard players operation $skzr mg.st /= #10 mg.st',
                 'execute store result score $skn mg.st if entity @a[tag=mg.play]',
                 '# Colonnes de vent (actives pendant les 3 premières minutes)',
                 'scoreboard players remove @a[scores={mg.skl=1..}] mg.skl 1',
                 f'execute as @a[scores={{mg.skl=100}}] run function {NS}/lift_end',
                 f'execute if score $skt mg.st matches ..3599 run function {NS}/s_cols',
                 f'execute as @a[tag=mg.play] at @s run function {NS}/s_player',
                 f'execute if score $skp5 mg.st matches 0 as @a[tag=mg.play] at @s positioned {ax0+.5} ~ {az0+.5} run function {NS}/zone_chk with storage mg:sky z',
                 f'execute if score $skp5 mg.st matches 0 as @a[tag=mg.play] at @s positioned {ax0+.5} ~ {az0+.5} run function {NS}/zone_draw with storage mg:sky z',
                 f'execute if score $skp5 mg.st matches 0 as @a[tag=mg.out] at @s positioned {ax0+.5} ~ {az0+.5} run function {NS}/zone_draw with storage mg:sky z',
                 '# Une fusée toutes les 8 s (jusqu\'à la mort subite)',
                 f'execute if score $skt mg.st matches ..3599 if score $skfw mg.st matches 0 run function {NS}/s_rocket',
                 'execute if score $skt mg.st matches 3600 run tellraw @a[tag=!mg.surv] [{"text":"🌪 MORT SUBITE : ","color":"red","bold":true},{"text":"zone au minimum, plus de fusées ni de colonnes de vent !","color":"gray","bold":false}]',
                 'execute if score $skt mg.st matches 3600 as @a[tag=!mg.surv] at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.5 1.5',
                 '# Survivants : une seconde de plus',
                 'scoreboard players operation $skq mg.st = $skt mg.st',
                 'scoreboard players operation $skq mg.st %= #20 mg.st',
                 'execute if score $skq mg.st matches 0 run scoreboard players add @a[tag=mg.play] mg.sks 1',
                 '# Fin',
                 'execute store result score $skn mg.st if entity @a[tag=mg.play]',
                 f'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $skn mg.st matches 1 as @a[tag=mg.play,limit=1] run function {NS}/s_win',
                 f'execute if score $state mg.st matches 2 if score $skt mg.st matches 6000.. run function {NS}/s_timeout',
                 'execute if score $state mg.st matches 2 unless entity @a[tag=mg.play] run function mg:core/draw'])
    W('s_zone', ['# $skz = 700 - t × 11 / 72  (t ≤ 3600) → mg:sky z.r',
                 'scoreboard players operation $skz mg.st = $skt mg.st',
                 'scoreboard players operation $skz mg.st *= #11 mg.st',
                 'scoreboard players operation $skz mg.st /= #72 mg.st',
                 'scoreboard players operation $skz mg.st *= #-1 mg.st',
                 'scoreboard players add $skz mg.st 700',
                 'execute if score $skz mg.st matches ..150 run scoreboard players set $skz mg.st 150',
                 'execute store result storage mg:sky z.r double 0.1 run scoreboard players get $skz mg.st'])
    W('s_player', ['# Survie en vol, chaque tick (@s = participant, positionné)',
                   'scoreboard players add @s mg.skg 1',
                   'execute if score @s mg.skg matches 1.. if predicate mg:gliding run scoreboard players set @s mg.skg 0',
                   f'execute if score $skpo mg.st matches 1 if entity @s[x={PAD3[0]-8},y={PAD3[1]},z={PAD3[2]-8},dx=16,dy=6,dz=16] run scoreboard players set @s mg.skg -40',
                   'execute if score @s mg.skl matches 101.. run scoreboard players set @s mg.skg -20',
                   f'execute unless entity @s[y={FLOOR3},dy=400] run return run function {NS}/s_elim {{why:"est tombé dans le vide"}}',
                   f'execute if score @s mg.skg matches 20.. run return run function {NS}/s_elim {{why:"s\'est posé"}}',
                   f'execute if score @s mg.sko matches 60.. run return run function {NS}/s_elim {{why:"est resté hors de la zone"}}',
                   'execute if score @s mg.sko matches 1.. run return run title @s actionbar [{"text":"⚠ HORS DE LA ZONE — reviens vers le centre ! ","color":"red","bold":true},{"score":{"name":"@s","objective":"mg.sko"},"color":"yellow"},{"text":"/60","color":"gray"}]',
                   'execute if score @s mg.skl matches 101.. run return run title @s actionbar [{"text":"💨 Colonne de vent !","color":"aqua","bold":true}]',
                   'execute if score $skt mg.st matches ..3599 run title @s actionbar [{"text":"🪽 En vol : ","color":"aqua"},{"score":{"name":"$skn","objective":"mg.st"},"color":"white"},{"text":"   ◯ zone ","color":"gray"},{"score":{"name":"$skzr","objective":"mg.st"},"color":"red"},{"text":" blocs   🚀 dans ","color":"gray"},{"score":{"name":"$skfs","objective":"mg.st"},"color":"gold"},{"text":" s","color":"gray"}]',
                   'execute if score $skt mg.st matches 3600.. run title @s actionbar [{"text":"🌪 MORT SUBITE","color":"red","bold":true},{"text":"   🪽 En vol : ","color":"aqua","bold":false},{"score":{"name":"$skn","objective":"mg.st"},"color":"white","bold":false}]'])
    W('s_elim', ['# Éliminé (@s) — macro {why}',
                 '$tellraw @a[tag=!mg.surv] [{"text":"🪽 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" $(why).","color":"gray"}]',
                 'scoreboard players reset @s mg.sks',
                 'scoreboard players set @s mg.skl 0',
                 'scoreboard players set @s mg.sko 0',
                 'effect clear @s minecraft:levitation',
                 f'clear @s {SKYITEM}',
                 'function mg:core/eliminate'])
    W('zone_chk', ['# Dans la zone ? (@s, positionné au centre à sa hauteur) — macro {r}',
                   '$execute if entity @s[distance=..$(r)] run return run scoreboard players set @s mg.sko 0',
                   'execute if score @s mg.sko matches 0 run title @s subtitle [{"text":"Hors de la zone : 3 s pour revenir !","color":"red"}]',
                   'execute if score @s mg.sko matches 0 run title @s title [{"text":"⚠","color":"red","bold":true}]',
                   'execute if score @s mg.sko matches 0 run playsound minecraft:block.note_block.bass master @s ~ ~ ~ 1 0.6',
                   'scoreboard players add @s mg.sko 5'])
    W('zone_draw', ['# Cercle de la zone à la hauteur du joueur, vu par lui seul (@s, positionné au centre) — macro {r} (généré)']
      + [f'$execute rotated {a} 0 run particle minecraft:dust{{color:[1.0,0.2,0.15],scale:3.0}} ^ ^ ^$(r) 0.1 2.5 0.1 0 3 force @s' for a in range(0, 360, 8)])
    W('s_cols', ['# Colonnes de vent : élan vers le haut (généré)']
      + [f'execute as @a[tag=mg.play,x={cx-COL_R},y={COL_Y0},z={cz-COL_R},dx={2*COL_R},dy={COL_Y1-COL_Y0},dz={2*COL_R},scores={{mg.skl=..0}}] run function {NS}/lift' for cx, cz in COLS]
      + ['execute if score $skp5 mg.st matches 0 run function mg:sky/s_colfx'])
    W('s_colfx', ['# Colonnes de vent : particules ascendantes (généré)']
      + [l for cx, cz in COLS for l in (
          f'particle minecraft:cloud {cx+.5} {(COL_Y0+COL_Y1)//2} {cz+.5} 1.3 26 1.3 0.02 30 force @a',
          f'particle minecraft:small_gust {cx+.5} {(COL_Y0+COL_Y1)//2} {cz+.5} 1.5 26 1.5 0 12 force @a',
          f'particle minecraft:end_rod {cx+.5} {COL_Y0+3} {cz+.5} 1.5 1 1.5 0.15 6 force @a')])
    W('lift', ['# Entrée dans une colonne de vent (@s) : 1,5 s de lévitation, puis 5 s avant la suivante',
               'scoreboard players set @s mg.skl 130',
               'effect give @s minecraft:levitation infinite 9 true',
               'playsound minecraft:entity.breeze.wind_burst master @s ~ ~ ~ 1 1'])
    W('lift_end', ['# Fin de l\'élan (@s)',
                   'effect clear @s minecraft:levitation',
                   'execute if entity @s[tag=mg.play] run title @s subtitle [{"text":"Appuie sur Espace pour replaner !","color":"yellow","bold":true}]',
                   'execute if entity @s[tag=mg.play] run title @s title [{"text":" "}]'])
    W('s_rocket', ['# Une fusée pour chaque survivant',
                   f'give @a[tag=mg.play] {ROCK} 1',
                   'execute as @a[tag=mg.play] at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 0.8 1.4'])
    W('s_win', ['# Dernier en vol (@s)',
                'effect give @s minecraft:slow_falling 15 0 true',
                'function mg:core/win_player'])
    W('s_timeout', ['# 5 minutes : le plus haut gagne',
                    'tellraw @a[tag=mg.play] [{"text":"🌪 Temps écoulé : le plus haut l\'emporte !","color":"gold"}]',
                    'effect give @a[tag=mg.play] minecraft:slow_falling 15 0 true',
                    'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                    'execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]',
                    'scoreboard players set $skmx mg.st -9999',
                    'execute as @a[tag=mg.play] run scoreboard players operation $skmx mg.st > @s mg.t',
                    'tag @a remove mg.skw',
                    'execute as @a[tag=mg.play] if score @s mg.t = $skmx mg.st run tag @s add mg.skw',
                    'execute as @a[tag=mg.skw,sort=random,limit=1] run function mg:core/win_player',
                    'tag @a remove mg.skw'])

    W('cleanup', ['# Élytra — nettoyage (appelé par core/return_lobby)',
                  f'clear @a {SKYITEM}',
                  'effect clear @a[scores={mg.skl=1..}] minecraft:levitation',
                  'kill @e[tag=mg.sky]',
                  f'kill @e[type=minecraft:wind_charge,x={zx-20},y=0,z={zz-20},dx={zdx+40},dy=320,dz=1600]',
                  'tag @a remove mg.skf',
                  'tag @a remove mg.skstun',
                  'tag @a remove mg.skak',
                  'tag @a remove mg.skv',
                  'tag @a remove mg.skw',
                  'scoreboard players reset * mg.skr',
                  'scoreboard players reset * mg.sks',
                  'scoreboard players reset * mg.skg',
                  'scoreboard players reset * mg.skst',
                  'scoreboard players reset * mg.skl',
                  'scoreboard players reset * mg.sko',
                  'advancement revoke @a only mg:sky/hurt',
                  f'schedule clear {NS}/pad_wait',
                  f'function {NS}/pad_fl_off'])
