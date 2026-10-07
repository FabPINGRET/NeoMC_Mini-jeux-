# Royaume Koopa : dangers (chaque tick de course)
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 0
scoreboard players operation $hp mg.st %= #h100 mg.st
execute if score $hp mg.st matches 48 run tp @e[type=minecraft:item_display,tag=mg.kh1] -183.64 84.6 19112.93
execute if score $hp mg.st matches 52 run execute positioned -183.64 79.6 19112.93 run playsound minecraft:block.stone.hit master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 0.5
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh1,limit=1] {teleport_duration:2}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh1] -183.64 79.6 19112.93
execute if score $hp mg.st matches 62 run execute positioned -183.64 78.0 19112.93 run particle minecraft:explosion ~ ~0.3 ~ 1.2 0.2 1.2 0 4
execute if score $hp mg.st matches 62 run execute positioned -183.64 78.0 19112.93 run playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..28] ~ ~ ~ 0.8 0.6
execute if score $hp mg.st matches 61..84 positioned -183.64 78.0 19112.93 as @e[type=minecraft:block_display,tag=mg.kart,distance=..2.3] run function mg:kart/t2/hz_big
execute if score $hp mg.st matches 85 run data merge entity @e[type=minecraft:item_display,tag=mg.kh1,limit=1] {teleport_duration:20}
execute if score $hp mg.st matches 85 run tp @e[type=minecraft:item_display,tag=mg.kh1] -183.64 84.1 19112.93
execute if score $hp mg.st matches 99 run data merge entity @e[type=minecraft:item_display,tag=mg.kh1,limit=1] {teleport_duration:3}
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 50
scoreboard players operation $hp mg.st %= #h100 mg.st
execute if score $hp mg.st matches 48 run tp @e[type=minecraft:item_display,tag=mg.kh2] -185.49 84.6 19117.15
execute if score $hp mg.st matches 52 run execute positioned -185.49 79.6 19117.15 run playsound minecraft:block.stone.hit master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 0.5
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh2,limit=1] {teleport_duration:2}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh2] -185.49 79.6 19117.15
execute if score $hp mg.st matches 62 run execute positioned -185.49 78.0 19117.15 run particle minecraft:explosion ~ ~0.3 ~ 1.2 0.2 1.2 0 4
execute if score $hp mg.st matches 62 run execute positioned -185.49 78.0 19117.15 run playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..28] ~ ~ ~ 0.8 0.6
execute if score $hp mg.st matches 61..84 positioned -185.49 78.0 19117.15 as @e[type=minecraft:block_display,tag=mg.kart,distance=..2.3] run function mg:kart/t2/hz_big
execute if score $hp mg.st matches 85 run data merge entity @e[type=minecraft:item_display,tag=mg.kh2,limit=1] {teleport_duration:20}
execute if score $hp mg.st matches 85 run tp @e[type=minecraft:item_display,tag=mg.kh2] -185.49 84.1 19117.15
execute if score $hp mg.st matches 99 run data merge entity @e[type=minecraft:item_display,tag=mg.kh2,limit=1] {teleport_duration:3}
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 0
scoreboard players operation $hp mg.st %= #h100 mg.st
execute if score $hp mg.st matches 48 run tp @e[type=minecraft:item_display,tag=mg.kh3] -158.54 85.6 19121.42
execute if score $hp mg.st matches 52 run execute positioned -158.54 80.6 19121.42 run playsound minecraft:block.stone.hit master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 0.5
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh3,limit=1] {teleport_duration:2}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh3] -158.54 80.6 19121.42
execute if score $hp mg.st matches 62 run execute positioned -158.54 79.0 19121.42 run particle minecraft:explosion ~ ~0.3 ~ 1.2 0.2 1.2 0 4
execute if score $hp mg.st matches 62 run execute positioned -158.54 79.0 19121.42 run playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..28] ~ ~ ~ 0.8 0.6
execute if score $hp mg.st matches 61..84 positioned -158.54 79.0 19121.42 as @e[type=minecraft:block_display,tag=mg.kart,distance=..2.3] run function mg:kart/t2/hz_big
execute if score $hp mg.st matches 85 run data merge entity @e[type=minecraft:item_display,tag=mg.kh3,limit=1] {teleport_duration:20}
execute if score $hp mg.st matches 85 run tp @e[type=minecraft:item_display,tag=mg.kh3] -158.54 85.1 19121.42
execute if score $hp mg.st matches 99 run data merge entity @e[type=minecraft:item_display,tag=mg.kh3,limit=1] {teleport_duration:3}
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 50
scoreboard players operation $hp mg.st %= #h100 mg.st
execute if score $hp mg.st matches 48 run tp @e[type=minecraft:item_display,tag=mg.kh4] -159.52 85.6 19125.92
execute if score $hp mg.st matches 52 run execute positioned -159.52 80.6 19125.92 run playsound minecraft:block.stone.hit master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 0.5
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh4,limit=1] {teleport_duration:2}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh4] -159.52 80.6 19125.92
execute if score $hp mg.st matches 62 run execute positioned -159.52 79.0 19125.92 run particle minecraft:explosion ~ ~0.3 ~ 1.2 0.2 1.2 0 4
execute if score $hp mg.st matches 62 run execute positioned -159.52 79.0 19125.92 run playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..28] ~ ~ ~ 0.8 0.6
execute if score $hp mg.st matches 61..84 positioned -159.52 79.0 19125.92 as @e[type=minecraft:block_display,tag=mg.kart,distance=..2.3] run function mg:kart/t2/hz_big
execute if score $hp mg.st matches 85 run data merge entity @e[type=minecraft:item_display,tag=mg.kh4,limit=1] {teleport_duration:20}
execute if score $hp mg.st matches 85 run tp @e[type=minecraft:item_display,tag=mg.kh4] -159.52 85.1 19125.92
execute if score $hp mg.st matches 99 run data merge entity @e[type=minecraft:item_display,tag=mg.kh4,limit=1] {teleport_duration:3}
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 0
scoreboard players operation $hp mg.st %= #h100 mg.st
execute if score $hp mg.st matches 48 run tp @e[type=minecraft:item_display,tag=mg.kh5] -133.78 85.6 19118.65
execute if score $hp mg.st matches 52 run execute positioned -133.78 80.6 19118.65 run playsound minecraft:block.stone.hit master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 0.5
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh5,limit=1] {teleport_duration:2}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh5] -133.78 80.6 19118.65
execute if score $hp mg.st matches 62 run execute positioned -133.78 79.0 19118.65 run particle minecraft:explosion ~ ~0.3 ~ 1.2 0.2 1.2 0 4
execute if score $hp mg.st matches 62 run execute positioned -133.78 79.0 19118.65 run playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..28] ~ ~ ~ 0.8 0.6
execute if score $hp mg.st matches 61..84 positioned -133.78 79.0 19118.65 as @e[type=minecraft:block_display,tag=mg.kart,distance=..2.3] run function mg:kart/t2/hz_big
execute if score $hp mg.st matches 85 run data merge entity @e[type=minecraft:item_display,tag=mg.kh5,limit=1] {teleport_duration:20}
execute if score $hp mg.st matches 85 run tp @e[type=minecraft:item_display,tag=mg.kh5] -133.78 85.1 19118.65
execute if score $hp mg.st matches 99 run data merge entity @e[type=minecraft:item_display,tag=mg.kh5,limit=1] {teleport_duration:3}
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 50
scoreboard players operation $hp mg.st %= #h100 mg.st
execute if score $hp mg.st matches 48 run tp @e[type=minecraft:item_display,tag=mg.kh6] -131.89 85.6 19122.84
execute if score $hp mg.st matches 52 run execute positioned -131.89 80.6 19122.84 run playsound minecraft:block.stone.hit master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 0.5
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh6,limit=1] {teleport_duration:2}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh6] -131.89 80.6 19122.84
execute if score $hp mg.st matches 62 run execute positioned -131.89 79.0 19122.84 run particle minecraft:explosion ~ ~0.3 ~ 1.2 0.2 1.2 0 4
execute if score $hp mg.st matches 62 run execute positioned -131.89 79.0 19122.84 run playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..28] ~ ~ ~ 0.8 0.6
execute if score $hp mg.st matches 61..84 positioned -131.89 79.0 19122.84 as @e[type=minecraft:block_display,tag=mg.kart,distance=..2.3] run function mg:kart/t2/hz_big
execute if score $hp mg.st matches 85 run data merge entity @e[type=minecraft:item_display,tag=mg.kh6,limit=1] {teleport_duration:20}
execute if score $hp mg.st matches 85 run tp @e[type=minecraft:item_display,tag=mg.kh6] -131.89 85.1 19122.84
execute if score $hp mg.st matches 99 run data merge entity @e[type=minecraft:item_display,tag=mg.kh6,limit=1] {teleport_duration:3}
execute as @e[type=minecraft:item_display,tag=mg.kh7] at @s run rotate @s ~7 0
execute as @e[type=minecraft:item_display,tag=mg.kh7] at @s positioned ^ ^ ^0.85 run tp @e[type=minecraft:item_display,tag=mg.kh7b1] ~ ~ ~
execute as @e[type=minecraft:item_display,tag=mg.kh7] at @s positioned ^ ^ ^1.7 run tp @e[type=minecraft:item_display,tag=mg.kh7b2] ~ ~ ~
execute as @e[type=minecraft:item_display,tag=mg.kh7] at @s positioned ^ ^ ^2.55 run tp @e[type=minecraft:item_display,tag=mg.kh7b3] ~ ~ ~
execute as @e[type=minecraft:item_display,tag=mg.kh7] at @s positioned ^ ^ ^3.4 run tp @e[type=minecraft:item_display,tag=mg.kh7b4] ~ ~ ~
execute as @e[type=minecraft:item_display,tag=mg.kh7] at @s positioned ^ ^ ^4.25 run tp @e[type=minecraft:item_display,tag=mg.kh7b5] ~ ~ ~
execute as @e[type=minecraft:item_display,tag=mg.kh8] at @s run rotate @s ~-6 0
execute as @e[type=minecraft:item_display,tag=mg.kh8] at @s positioned ^ ^ ^0.85 run tp @e[type=minecraft:item_display,tag=mg.kh8b1] ~ ~ ~
execute as @e[type=minecraft:item_display,tag=mg.kh8] at @s positioned ^ ^ ^1.7 run tp @e[type=minecraft:item_display,tag=mg.kh8b2] ~ ~ ~
execute as @e[type=minecraft:item_display,tag=mg.kh8] at @s positioned ^ ^ ^2.55 run tp @e[type=minecraft:item_display,tag=mg.kh8b3] ~ ~ ~
execute as @e[type=minecraft:item_display,tag=mg.kh8] at @s positioned ^ ^ ^3.4 run tp @e[type=minecraft:item_display,tag=mg.kh8b4] ~ ~ ~
execute as @e[type=minecraft:item_display,tag=mg.kh8] at @s positioned ^ ^ ^4.25 run tp @e[type=minecraft:item_display,tag=mg.kh8b5] ~ ~ ~
execute as @e[type=minecraft:item_display,tag=mg.kfb] at @s positioned ~ ~-0.7 ~ as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.05] run function mg:kart/t2/hz_hit
execute if score $kph mg.st matches 0 as @e[type=minecraft:item_display,tag=mg.kfb] at @s run particle minecraft:flame ~ ~ ~ 0.1 0.1 0.1 0.01 1
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 0
scoreboard players operation $hp mg.st %= #h100 mg.st
execute if score $hp mg.st matches 1 run data merge entity @e[type=minecraft:item_display,tag=mg.kh9,limit=1] {teleport_duration:6}
execute if score $hp mg.st matches 1 run tp @e[type=minecraft:item_display,tag=mg.kh9] 198.88 65.4 19032.74
execute if score $hp mg.st matches 1 run execute positioned 191.93 63.4 19033.6 run particle minecraft:splash ~ ~0.5 ~ 0.4 0.2 0.4 0 12
execute if score $hp mg.st matches 1 run execute positioned 191.93 63.4 19033.6 run playsound minecraft:entity.salmon.flop master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 1
execute if score $hp mg.st matches 7 run data merge entity @e[type=minecraft:item_display,tag=mg.kh9,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 7 run tp @e[type=minecraft:item_display,tag=mg.kh9] 203.84 66.0 19032.12
execute if score $hp mg.st matches 11 run tp @e[type=minecraft:item_display,tag=mg.kh9] 208.8 65.4 19031.51
execute if score $hp mg.st matches 15 run data merge entity @e[type=minecraft:item_display,tag=mg.kh9,limit=1] {teleport_duration:6}
execute if score $hp mg.st matches 15 run tp @e[type=minecraft:item_display,tag=mg.kh9] 215.75 63.4 19030.64
execute if score $hp mg.st matches 21 run execute positioned 215.75 63.4 19030.64 run particle minecraft:splash ~ ~0.5 ~ 0.4 0.2 0.4 0 12
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh9,limit=1] {teleport_duration:0}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh9] 191.93 63.4 19033.6
execute if score $hp mg.st matches 7 positioned 198.88 64.8 19032.74 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 8 positioned 200.12 64.95 19032.58 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 9 positioned 201.36 65.1 19032.43 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 10 positioned 202.6 65.25 19032.28 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 11 positioned 203.84 65.4 19032.12 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 12 positioned 205.08 65.25 19031.97 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 13 positioned 206.32 65.1 19031.81 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 14 positioned 207.56 64.95 19031.66 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 15 positioned 208.8 64.8 19031.51 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 37
scoreboard players operation $hp mg.st %= #h100 mg.st
execute if score $hp mg.st matches 1 run data merge entity @e[type=minecraft:item_display,tag=mg.kh10,limit=1] {teleport_duration:6}
execute if score $hp mg.st matches 1 run tp @e[type=minecraft:item_display,tag=mg.kh10] 197.84 65.4 19026.17
execute if score $hp mg.st matches 1 run execute positioned 190.97 63.4 19027.51 run particle minecraft:splash ~ ~0.5 ~ 0.4 0.2 0.4 0 12
execute if score $hp mg.st matches 1 run execute positioned 190.97 63.4 19027.51 run playsound minecraft:entity.salmon.flop master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 1
execute if score $hp mg.st matches 7 run data merge entity @e[type=minecraft:item_display,tag=mg.kh10,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 7 run tp @e[type=minecraft:item_display,tag=mg.kh10] 202.75 66.0 19025.21
execute if score $hp mg.st matches 11 run tp @e[type=minecraft:item_display,tag=mg.kh10] 207.65 65.4 19024.25
execute if score $hp mg.st matches 15 run data merge entity @e[type=minecraft:item_display,tag=mg.kh10,limit=1] {teleport_duration:6}
execute if score $hp mg.st matches 15 run tp @e[type=minecraft:item_display,tag=mg.kh10] 214.52 63.4 19022.91
execute if score $hp mg.st matches 21 run execute positioned 214.52 63.4 19022.91 run particle minecraft:splash ~ ~0.5 ~ 0.4 0.2 0.4 0 12
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh10,limit=1] {teleport_duration:0}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh10] 190.97 63.4 19027.51
execute if score $hp mg.st matches 7 positioned 197.84 64.8 19026.17 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 8 positioned 199.07 64.95 19025.93 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 9 positioned 200.29 65.1 19025.69 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 10 positioned 201.52 65.25 19025.45 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 11 positioned 202.75 65.4 19025.21 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 12 positioned 203.97 65.25 19024.97 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 13 positioned 205.2 65.1 19024.73 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 14 positioned 206.43 64.95 19024.49 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 15 positioned 207.65 64.8 19024.25 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 71
scoreboard players operation $hp mg.st %= #h100 mg.st
execute if score $hp mg.st matches 1 run data merge entity @e[type=minecraft:item_display,tag=mg.kh11,limit=1] {teleport_duration:6}
execute if score $hp mg.st matches 1 run tp @e[type=minecraft:item_display,tag=mg.kh11] 196.31 65.4 19019.81
execute if score $hp mg.st matches 1 run execute positioned 189.59 63.4 19021.78 run particle minecraft:splash ~ ~0.5 ~ 0.4 0.2 0.4 0 12
execute if score $hp mg.st matches 1 run execute positioned 189.59 63.4 19021.78 run playsound minecraft:entity.salmon.flop master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 1
execute if score $hp mg.st matches 7 run data merge entity @e[type=minecraft:item_display,tag=mg.kh11,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 7 run tp @e[type=minecraft:item_display,tag=mg.kh11] 201.1 66.0 19018.41
execute if score $hp mg.st matches 11 run tp @e[type=minecraft:item_display,tag=mg.kh11] 205.9 65.4 19017.0
execute if score $hp mg.st matches 15 run data merge entity @e[type=minecraft:item_display,tag=mg.kh11,limit=1] {teleport_duration:6}
execute if score $hp mg.st matches 15 run tp @e[type=minecraft:item_display,tag=mg.kh11] 212.62 63.4 19015.03
execute if score $hp mg.st matches 21 run execute positioned 212.62 63.4 19015.03 run particle minecraft:splash ~ ~0.5 ~ 0.4 0.2 0.4 0 12
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh11,limit=1] {teleport_duration:0}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh11] 189.59 63.4 19021.78
execute if score $hp mg.st matches 7 positioned 196.31 64.8 19019.81 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 8 positioned 197.51 64.95 19019.46 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 9 positioned 198.7 65.1 19019.11 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 10 positioned 199.9 65.25 19018.76 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 11 positioned 201.1 65.4 19018.41 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 12 positioned 202.3 65.25 19018.06 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 13 positioned 203.5 65.1 19017.7 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 14 positioned 204.7 64.95 19017.35 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 15 positioned 205.9 64.8 19017.0 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 10
scoreboard players operation $hp mg.st %= #h90 mg.st
execute if score $hp mg.st matches 1 run data merge entity @e[type=minecraft:item_display,tag=mg.kh12,limit=1] {teleport_duration:6}
execute if score $hp mg.st matches 1 run tp @e[type=minecraft:item_display,tag=mg.kh12] -175.83 78.4 19113.24
execute if score $hp mg.st matches 1 run execute positioned -174.57 75.8 19109.98 run particle minecraft:lava ~ ~0.5 ~ 0.4 0.2 0.4 0 12
execute if score $hp mg.st matches 1 run execute positioned -174.57 75.8 19109.98 run playsound minecraft:block.lava.pop master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 1
execute if score $hp mg.st matches 7 run data merge entity @e[type=minecraft:item_display,tag=mg.kh12,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 7 run tp @e[type=minecraft:item_display,tag=mg.kh12] -177.64 79.0 19117.9
execute if score $hp mg.st matches 11 run tp @e[type=minecraft:item_display,tag=mg.kh12] -179.45 78.4 19122.57
execute if score $hp mg.st matches 15 run data merge entity @e[type=minecraft:item_display,tag=mg.kh12,limit=1] {teleport_duration:6}
execute if score $hp mg.st matches 15 run tp @e[type=minecraft:item_display,tag=mg.kh12] -180.71 75.8 19125.83
execute if score $hp mg.st matches 21 run execute positioned -180.71 75.8 19125.83 run particle minecraft:lava ~ ~0.5 ~ 0.4 0.2 0.4 0 12
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh12,limit=1] {teleport_duration:0}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh12] -174.57 75.8 19109.98
execute if score $hp mg.st matches 7 positioned -175.83 77.8 19113.24 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 8 positioned -176.28 77.95 19114.41 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 9 positioned -176.73 78.1 19115.57 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 10 positioned -177.19 78.25 19116.74 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 11 positioned -177.64 78.4 19117.9 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 12 positioned -178.09 78.25 19119.07 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 13 positioned -178.54 78.1 19120.24 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 14 positioned -178.99 77.95 19121.4 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 15 positioned -179.45 77.8 19122.57 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 55
scoreboard players operation $hp mg.st %= #h90 mg.st
execute if score $hp mg.st matches 1 run data merge entity @e[type=minecraft:item_display,tag=mg.kh13,limit=1] {teleport_duration:6}
execute if score $hp mg.st matches 1 run tp @e[type=minecraft:item_display,tag=mg.kh13] -150.26 79.4 19119.97
execute if score $hp mg.st matches 1 run execute positioned -150.0 76.8 19116.48 run particle minecraft:lava ~ ~0.5 ~ 0.4 0.2 0.4 0 12
execute if score $hp mg.st matches 1 run execute positioned -150.0 76.8 19116.48 run playsound minecraft:block.lava.pop master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 1
execute if score $hp mg.st matches 7 run data merge entity @e[type=minecraft:item_display,tag=mg.kh13,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 7 run tp @e[type=minecraft:item_display,tag=mg.kh13] -150.63 80.0 19124.96
execute if score $hp mg.st matches 11 run tp @e[type=minecraft:item_display,tag=mg.kh13] -151.01 79.4 19129.94
execute if score $hp mg.st matches 15 run data merge entity @e[type=minecraft:item_display,tag=mg.kh13,limit=1] {teleport_duration:6}
execute if score $hp mg.st matches 15 run tp @e[type=minecraft:item_display,tag=mg.kh13] -151.27 76.8 19133.43
execute if score $hp mg.st matches 21 run execute positioned -151.27 76.8 19133.43 run particle minecraft:lava ~ ~0.5 ~ 0.4 0.2 0.4 0 12
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh13,limit=1] {teleport_duration:0}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh13] -150.0 76.8 19116.48
execute if score $hp mg.st matches 7 positioned -150.26 78.8 19119.97 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 8 positioned -150.35 78.95 19121.22 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 9 positioned -150.45 79.1 19122.46 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 10 positioned -150.54 79.25 19123.71 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 11 positioned -150.63 79.4 19124.96 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 12 positioned -150.73 79.25 19126.2 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 13 positioned -150.82 79.1 19127.45 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 14 positioned -150.92 78.95 19128.69 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 15 positioned -151.01 78.8 19129.94 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 80
scoreboard players operation $hp mg.st %= #h90 mg.st
execute if score $hp mg.st matches 1 run data merge entity @e[type=minecraft:item_display,tag=mg.kh14,limit=1] {teleport_duration:6}
execute if score $hp mg.st matches 1 run tp @e[type=minecraft:item_display,tag=mg.kh14] -142.17 79.4 19119.0
execute if score $hp mg.st matches 1 run execute positioned -143.16 76.8 19115.64 run particle minecraft:lava ~ ~0.5 ~ 0.4 0.2 0.4 0 12
execute if score $hp mg.st matches 1 run execute positioned -143.16 76.8 19115.64 run playsound minecraft:block.lava.pop master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 1
execute if score $hp mg.st matches 7 run data merge entity @e[type=minecraft:item_display,tag=mg.kh14,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 7 run tp @e[type=minecraft:item_display,tag=mg.kh14] -140.76 80.0 19123.8
execute if score $hp mg.st matches 11 run tp @e[type=minecraft:item_display,tag=mg.kh14] -139.35 79.4 19128.59
execute if score $hp mg.st matches 15 run data merge entity @e[type=minecraft:item_display,tag=mg.kh14,limit=1] {teleport_duration:6}
execute if score $hp mg.st matches 15 run tp @e[type=minecraft:item_display,tag=mg.kh14] -138.37 76.8 19131.95
execute if score $hp mg.st matches 21 run execute positioned -138.37 76.8 19131.95 run particle minecraft:lava ~ ~0.5 ~ 0.4 0.2 0.4 0 12
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh14,limit=1] {teleport_duration:0}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh14] -143.16 76.8 19115.64
execute if score $hp mg.st matches 7 positioned -142.17 78.8 19119.0 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 8 positioned -141.82 78.95 19120.2 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 9 positioned -141.47 79.1 19121.4 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 10 positioned -141.11 79.25 19122.6 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 11 positioned -140.76 79.4 19123.8 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 12 positioned -140.41 79.25 19124.99 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 13 positioned -140.06 79.1 19126.19 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 14 positioned -139.71 78.95 19127.39 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 15 positioned -139.35 78.8 19128.59 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.5] run function mg:kart/t2/hz_hit
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 0
scoreboard players operation $hp mg.st %= #h70 mg.st
execute if score $hp mg.st matches 10 run tp @e[type=minecraft:item_display,tag=mg.kh15] 158.5 70.6 18864.5
execute if score $hp mg.st matches 25 run tp @e[type=minecraft:item_display,tag=mg.kh15] 158.5 70.2 18864.5
execute if score $hp mg.st matches 40 run execute positioned 158.5 70.2 18864.5 run playsound minecraft:entity.ravager.roar master @a[tag=mg.play,distance=..18] ~ ~ ~ 0.4 1.8
execute if score $hp mg.st matches 48 run data merge entity @e[type=minecraft:item_display,tag=mg.kh15,limit=1] {teleport_duration:3}
execute if score $hp mg.st matches 48 run tp @e[type=minecraft:item_display,tag=mg.kh15] 161.3 65.9 18858.65
execute if score $hp mg.st matches 50 run execute positioned 161.3 65.9 18858.65 run playsound minecraft:entity.evoker_fangs.attack master @a[tag=mg.play,distance=..18] ~ ~ ~ 1 1.2
execute if score $hp mg.st matches 50..55 positioned 161.3 65.0 18858.65 as @e[type=minecraft:block_display,tag=mg.kart,distance=..2.0] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 56 run data merge entity @e[type=minecraft:item_display,tag=mg.kh15,limit=1] {teleport_duration:10}
execute if score $hp mg.st matches 56 run tp @e[type=minecraft:item_display,tag=mg.kh15] 158.5 70.2 18864.5
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 23
scoreboard players operation $hp mg.st %= #h70 mg.st
execute if score $hp mg.st matches 10 run tp @e[type=minecraft:item_display,tag=mg.kh16] 145.5 70.6 18834.5
execute if score $hp mg.st matches 25 run tp @e[type=minecraft:item_display,tag=mg.kh16] 145.5 70.2 18834.5
execute if score $hp mg.st matches 40 run execute positioned 145.5 70.2 18834.5 run playsound minecraft:entity.ravager.roar master @a[tag=mg.play,distance=..18] ~ ~ ~ 0.4 1.8
execute if score $hp mg.st matches 48 run data merge entity @e[type=minecraft:item_display,tag=mg.kh16,limit=1] {teleport_duration:3}
execute if score $hp mg.st matches 48 run tp @e[type=minecraft:item_display,tag=mg.kh16] 142.99 65.9 18840.45
execute if score $hp mg.st matches 50 run execute positioned 142.99 65.9 18840.45 run playsound minecraft:entity.evoker_fangs.attack master @a[tag=mg.play,distance=..18] ~ ~ ~ 1 1.2
execute if score $hp mg.st matches 50..55 positioned 142.99 65.0 18840.45 as @e[type=minecraft:block_display,tag=mg.kart,distance=..2.0] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 56 run data merge entity @e[type=minecraft:item_display,tag=mg.kh16,limit=1] {teleport_duration:10}
execute if score $hp mg.st matches 56 run tp @e[type=minecraft:item_display,tag=mg.kh16] 145.5 70.2 18834.5
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 46
scoreboard players operation $hp mg.st %= #h70 mg.st
execute if score $hp mg.st matches 10 run tp @e[type=minecraft:item_display,tag=mg.kh17] 121.5 70.6 18853.5
execute if score $hp mg.st matches 25 run tp @e[type=minecraft:item_display,tag=mg.kh17] 121.5 70.2 18853.5
execute if score $hp mg.st matches 40 run execute positioned 121.5 70.2 18853.5 run playsound minecraft:entity.ravager.roar master @a[tag=mg.play,distance=..18] ~ ~ ~ 0.4 1.8
execute if score $hp mg.st matches 48 run data merge entity @e[type=minecraft:item_display,tag=mg.kh17,limit=1] {teleport_duration:3}
execute if score $hp mg.st matches 48 run tp @e[type=minecraft:item_display,tag=mg.kh17] 119.13 65.9 18847.17
execute if score $hp mg.st matches 50 run execute positioned 119.13 65.9 18847.17 run playsound minecraft:entity.evoker_fangs.attack master @a[tag=mg.play,distance=..18] ~ ~ ~ 1 1.2
execute if score $hp mg.st matches 50..55 positioned 119.13 65.0 18847.17 as @e[type=minecraft:block_display,tag=mg.kart,distance=..2.0] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 56 run data merge entity @e[type=minecraft:item_display,tag=mg.kh17,limit=1] {teleport_duration:10}
execute if score $hp mg.st matches 56 run tp @e[type=minecraft:item_display,tag=mg.kh17] 121.5 70.2 18853.5
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 69
scoreboard players operation $hp mg.st %= #h70 mg.st
execute if score $hp mg.st matches 10 run tp @e[type=minecraft:item_display,tag=mg.kh18] 93.5 70.6 18839.5
execute if score $hp mg.st matches 25 run tp @e[type=minecraft:item_display,tag=mg.kh18] 93.5 70.2 18839.5
execute if score $hp mg.st matches 40 run execute positioned 93.5 70.2 18839.5 run playsound minecraft:entity.ravager.roar master @a[tag=mg.play,distance=..18] ~ ~ ~ 0.4 1.8
execute if score $hp mg.st matches 48 run data merge entity @e[type=minecraft:item_display,tag=mg.kh18,limit=1] {teleport_duration:3}
execute if score $hp mg.st matches 48 run tp @e[type=minecraft:item_display,tag=mg.kh18] 93.99 65.9 18845.45
execute if score $hp mg.st matches 50 run execute positioned 93.99 65.9 18845.45 run playsound minecraft:entity.evoker_fangs.attack master @a[tag=mg.play,distance=..18] ~ ~ ~ 1 1.2
execute if score $hp mg.st matches 50..55 positioned 93.99 65.0 18845.45 as @e[type=minecraft:block_display,tag=mg.kart,distance=..2.0] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 56 run data merge entity @e[type=minecraft:item_display,tag=mg.kh18,limit=1] {teleport_duration:10}
execute if score $hp mg.st matches 56 run tp @e[type=minecraft:item_display,tag=mg.kh18] 93.5 70.2 18839.5
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 92
scoreboard players operation $hp mg.st %= #h70 mg.st
execute if score $hp mg.st matches 10 run tp @e[type=minecraft:item_display,tag=mg.kh19] 67.5 70.6 18853.5
execute if score $hp mg.st matches 25 run tp @e[type=minecraft:item_display,tag=mg.kh19] 67.5 70.2 18853.5
execute if score $hp mg.st matches 40 run execute positioned 67.5 70.2 18853.5 run playsound minecraft:entity.ravager.roar master @a[tag=mg.play,distance=..18] ~ ~ ~ 0.4 1.8
execute if score $hp mg.st matches 48 run data merge entity @e[type=minecraft:item_display,tag=mg.kh19,limit=1] {teleport_duration:3}
execute if score $hp mg.st matches 48 run tp @e[type=minecraft:item_display,tag=mg.kh19] 69.47 65.9 18847.56
execute if score $hp mg.st matches 50 run execute positioned 69.47 65.9 18847.56 run playsound minecraft:entity.evoker_fangs.attack master @a[tag=mg.play,distance=..18] ~ ~ ~ 1 1.2
execute if score $hp mg.st matches 50..55 positioned 69.47 65.0 18847.56 as @e[type=minecraft:block_display,tag=mg.kart,distance=..2.0] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 56 run data merge entity @e[type=minecraft:item_display,tag=mg.kh19,limit=1] {teleport_duration:10}
execute if score $hp mg.st matches 56 run tp @e[type=minecraft:item_display,tag=mg.kh19] 67.5 70.2 18853.5
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 115
scoreboard players operation $hp mg.st %= #h70 mg.st
execute if score $hp mg.st matches 10 run tp @e[type=minecraft:item_display,tag=mg.kh20] 43.5 70.6 18833.5
execute if score $hp mg.st matches 25 run tp @e[type=minecraft:item_display,tag=mg.kh20] 43.5 70.2 18833.5
execute if score $hp mg.st matches 40 run execute positioned 43.5 70.2 18833.5 run playsound minecraft:entity.ravager.roar master @a[tag=mg.play,distance=..18] ~ ~ ~ 0.4 1.8
execute if score $hp mg.st matches 48 run data merge entity @e[type=minecraft:item_display,tag=mg.kh20,limit=1] {teleport_duration:3}
execute if score $hp mg.st matches 48 run tp @e[type=minecraft:item_display,tag=mg.kh20] 46.05 65.9 18838.88
execute if score $hp mg.st matches 50 run execute positioned 46.05 65.9 18838.88 run playsound minecraft:entity.evoker_fangs.attack master @a[tag=mg.play,distance=..18] ~ ~ ~ 1 1.2
execute if score $hp mg.st matches 50..55 positioned 46.05 65.0 18838.88 as @e[type=minecraft:block_display,tag=mg.kart,distance=..2.0] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 56 run data merge entity @e[type=minecraft:item_display,tag=mg.kh20,limit=1] {teleport_duration:10}
execute if score $hp mg.st matches 56 run tp @e[type=minecraft:item_display,tag=mg.kh20] 43.5 70.2 18833.5
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 138
scoreboard players operation $hp mg.st %= #h70 mg.st
execute if score $hp mg.st matches 10 run tp @e[type=minecraft:item_display,tag=mg.kh21] 38.5 70.6 18865.5
execute if score $hp mg.st matches 25 run tp @e[type=minecraft:item_display,tag=mg.kh21] 38.5 70.2 18865.5
execute if score $hp mg.st matches 40 run execute positioned 38.5 70.2 18865.5 run playsound minecraft:entity.ravager.roar master @a[tag=mg.play,distance=..18] ~ ~ ~ 0.4 1.8
execute if score $hp mg.st matches 48 run data merge entity @e[type=minecraft:item_display,tag=mg.kh21,limit=1] {teleport_duration:3}
execute if score $hp mg.st matches 48 run tp @e[type=minecraft:item_display,tag=mg.kh21] 33.23 65.9 18860.88
execute if score $hp mg.st matches 50 run execute positioned 33.23 65.9 18860.88 run playsound minecraft:entity.evoker_fangs.attack master @a[tag=mg.play,distance=..18] ~ ~ ~ 1 1.2
execute if score $hp mg.st matches 50..55 positioned 33.23 65.0 18860.88 as @e[type=minecraft:block_display,tag=mg.kart,distance=..2.0] run function mg:kart/t2/hz_hit
execute if score $hp mg.st matches 56 run data merge entity @e[type=minecraft:item_display,tag=mg.kh21,limit=1] {teleport_duration:10}
execute if score $hp mg.st matches 56 run tp @e[type=minecraft:item_display,tag=mg.kh21] 38.5 70.2 18865.5
scoreboard players operation $hw mg.st = $ktime mg.st
scoreboard players operation $hw mg.st %= #h66 mg.st
execute as @e[type=minecraft:item_display,tag=mg.kwalk] at @s run tp @s ^ ^ ^0.12
execute if score $hw mg.st matches 0 as @e[type=minecraft:item_display,tag=mg.kwalk] at @s run tp @s ~ ~ ~ ~180 0
execute as @e[type=minecraft:item_display,tag=mg.kgoo,tag=!mg.kdead] at @s if entity @e[type=minecraft:block_display,tag=mg.kart,distance=..1.4] run function mg:kart/t2/goo_squash
execute as @e[type=minecraft:item_display,tag=mg.kpok] at @s positioned ~ ~-0.6 ~ as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.4] run function mg:kart/t2/hz_hit
execute as @e[tag=mg.kdead] run function mg:kart/t2/goo_wait
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 0
scoreboard players operation $hp mg.st %= #h90 mg.st
execute if score $hp mg.st matches 15 run tp @e[type=minecraft:item_display,tag=mg.kh32] -100.7 74.8 19149.05
execute if score $hp mg.st matches 18 run tp @e[type=minecraft:item_display,tag=mg.kh32] -100.7 74.2 19149.05
execute if score $hp mg.st matches 30 run tp @e[type=minecraft:item_display,tag=mg.kh32] -100.7 74.8 19149.05
execute if score $hp mg.st matches 33 run tp @e[type=minecraft:item_display,tag=mg.kh32] -100.7 74.2 19149.05
execute if score $hp mg.st matches 45 run tp @e[type=minecraft:item_display,tag=mg.kh32] -100.7 74.8 19149.05
execute if score $hp mg.st matches 48 run tp @e[type=minecraft:item_display,tag=mg.kh32] -100.7 74.2 19149.05
execute if score $hp mg.st matches 52 run execute positioned -100.7 74.2 19149.05 run playsound minecraft:entity.wolf.growl master @a[tag=mg.play,distance=..24] ~ ~ ~ 1 0.5
execute if score $hp mg.st matches 58 run execute positioned -100.7 74.2 19149.05 run playsound minecraft:entity.wolf.ambient master @a[tag=mg.play,distance=..30] ~ ~ ~ 1 0.5
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh32,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh32] -86.27 74.2 19144.26
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh32l1,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh32l1] -100.27 74.2 19148.91
execute if score $hp mg.st matches 72 run data merge entity @e[type=minecraft:item_display,tag=mg.kh32l1,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[type=minecraft:item_display,tag=mg.kh32l1] -102.67 74.2 19149.71
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh32l2,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh32l2] -97.47 74.2 19147.98
execute if score $hp mg.st matches 72 run data merge entity @e[type=minecraft:item_display,tag=mg.kh32l2,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[type=minecraft:item_display,tag=mg.kh32l2] -102.28 74.2 19149.58
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh32l3,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh32l3] -94.67 74.2 19147.05
execute if score $hp mg.st matches 72 run data merge entity @e[type=minecraft:item_display,tag=mg.kh32l3,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[type=minecraft:item_display,tag=mg.kh32l3] -101.88 74.2 19149.45
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh32l4,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh32l4] -91.87 74.2 19146.12
execute if score $hp mg.st matches 72 run data merge entity @e[type=minecraft:item_display,tag=mg.kh32l4,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[type=minecraft:item_display,tag=mg.kh32l4] -101.49 74.2 19149.32
execute if score $hp mg.st matches 60 run data merge entity @e[type=minecraft:item_display,tag=mg.kh32l5,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[type=minecraft:item_display,tag=mg.kh32l5] -89.07 74.2 19145.19
execute if score $hp mg.st matches 72 run data merge entity @e[type=minecraft:item_display,tag=mg.kh32l5,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[type=minecraft:item_display,tag=mg.kh32l5] -101.09 74.2 19149.18
execute if score $hp mg.st matches 61..70 positioned -96.71 73.0 19147.73 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.8] run function mg:kart/t2/hz_big
execute if score $hp mg.st matches 61..70 positioned -94.1 73.0 19146.86 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.8] run function mg:kart/t2/hz_big
execute if score $hp mg.st matches 61..70 positioned -91.49 73.0 19146.0 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.8] run function mg:kart/t2/hz_big
execute if score $hp mg.st matches 61..70 positioned -88.88 73.0 19145.13 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.8] run function mg:kart/t2/hz_big
execute if score $hp mg.st matches 61..70 positioned -86.27 73.0 19144.26 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.8] run function mg:kart/t2/hz_big
execute if score $hp mg.st matches 72 run data merge entity @e[type=minecraft:item_display,tag=mg.kh32,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[type=minecraft:item_display,tag=mg.kh32] -100.7 74.2 19149.05
execute if score $kph mg.st matches 2 positioned -222.88 67.2 18900.15 run particle minecraft:falling_dust{block_state:"minecraft:sand"} ~ ~ ~ 2 0.1 4 0 6
