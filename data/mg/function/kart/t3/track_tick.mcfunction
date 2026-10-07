# Forteresse Bob-omb : Chomps (chaque tick de bataille)
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 0
scoreboard players operation $hp mg.st %= #h90 mg.st
execute if score $hp mg.st matches 15 run tp @e[tag=mg.kh1] 0.5 66.8 21945.0
execute if score $hp mg.st matches 18 run tp @e[tag=mg.kh1] 0.5 66.2 21945.0
execute if score $hp mg.st matches 30 run tp @e[tag=mg.kh1] 0.5 66.8 21945.0
execute if score $hp mg.st matches 33 run tp @e[tag=mg.kh1] 0.5 66.2 21945.0
execute if score $hp mg.st matches 52 run execute positioned 0.5 66.2 21945.0 run playsound minecraft:entity.wolf.growl master @a[tag=mg.play,distance=..30] ~ ~ ~ 1 0.5
execute if score $hp mg.st matches 60 run data merge entity @e[tag=mg.kh1,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[tag=mg.kh1] 0.5 66.2 21955.5
execute if score $hp mg.st matches 60 run data merge entity @e[tag=mg.kh1l1,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[tag=mg.kh1l1] 0.5 66.2 21944.67
execute if score $hp mg.st matches 72 run data merge entity @e[tag=mg.kh1l1,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[tag=mg.kh1l1] 0.5 66.2 21942.92
execute if score $hp mg.st matches 60 run data merge entity @e[tag=mg.kh1l2,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[tag=mg.kh1l2] 0.5 66.2 21946.83
execute if score $hp mg.st matches 72 run data merge entity @e[tag=mg.kh1l2,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[tag=mg.kh1l2] 0.5 66.2 21943.33
execute if score $hp mg.st matches 60 run data merge entity @e[tag=mg.kh1l3,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[tag=mg.kh1l3] 0.5 66.2 21949.0
execute if score $hp mg.st matches 72 run data merge entity @e[tag=mg.kh1l3,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[tag=mg.kh1l3] 0.5 66.2 21943.75
execute if score $hp mg.st matches 60 run data merge entity @e[tag=mg.kh1l4,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[tag=mg.kh1l4] 0.5 66.2 21951.17
execute if score $hp mg.st matches 72 run data merge entity @e[tag=mg.kh1l4,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[tag=mg.kh1l4] 0.5 66.2 21944.17
execute if score $hp mg.st matches 60 run data merge entity @e[tag=mg.kh1l5,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[tag=mg.kh1l5] 0.5 66.2 21953.33
execute if score $hp mg.st matches 72 run data merge entity @e[tag=mg.kh1l5,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[tag=mg.kh1l5] 0.5 66.2 21944.58
execute if score $hp mg.st matches 61..70 positioned 0.5 65.0 21945.0 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.9] run function mg:kart/t3/hz_big
execute if score $hp mg.st matches 61..70 positioned 0.5 65.0 21947.1 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.9] run function mg:kart/t3/hz_big
execute if score $hp mg.st matches 61..70 positioned 0.5 65.0 21949.2 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.9] run function mg:kart/t3/hz_big
execute if score $hp mg.st matches 61..70 positioned 0.5 65.0 21951.3 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.9] run function mg:kart/t3/hz_big
execute if score $hp mg.st matches 61..70 positioned 0.5 65.0 21953.4 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.9] run function mg:kart/t3/hz_big
execute if score $hp mg.st matches 61..70 positioned 0.5 65.0 21955.5 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.9] run function mg:kart/t3/hz_big
execute if score $hp mg.st matches 72 run data merge entity @e[tag=mg.kh1,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[tag=mg.kh1] 0.5 66.2 21945.0
scoreboard players operation $hp mg.st = $ktime mg.st
scoreboard players add $hp mg.st 45
scoreboard players operation $hp mg.st %= #h90 mg.st
execute if score $hp mg.st matches 15 run tp @e[tag=mg.kh2] 0.5 66.8 22056.0
execute if score $hp mg.st matches 18 run tp @e[tag=mg.kh2] 0.5 66.2 22056.0
execute if score $hp mg.st matches 30 run tp @e[tag=mg.kh2] 0.5 66.8 22056.0
execute if score $hp mg.st matches 33 run tp @e[tag=mg.kh2] 0.5 66.2 22056.0
execute if score $hp mg.st matches 52 run execute positioned 0.5 66.2 22056.0 run playsound minecraft:entity.wolf.growl master @a[tag=mg.play,distance=..30] ~ ~ ~ 1 0.5
execute if score $hp mg.st matches 60 run data merge entity @e[tag=mg.kh2,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[tag=mg.kh2] 0.5 66.2 22045.5
execute if score $hp mg.st matches 60 run data merge entity @e[tag=mg.kh2l1,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[tag=mg.kh2l1] 0.5 66.2 22056.33
execute if score $hp mg.st matches 72 run data merge entity @e[tag=mg.kh2l1,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[tag=mg.kh2l1] 0.5 66.2 22058.08
execute if score $hp mg.st matches 60 run data merge entity @e[tag=mg.kh2l2,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[tag=mg.kh2l2] 0.5 66.2 22054.17
execute if score $hp mg.st matches 72 run data merge entity @e[tag=mg.kh2l2,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[tag=mg.kh2l2] 0.5 66.2 22057.67
execute if score $hp mg.st matches 60 run data merge entity @e[tag=mg.kh2l3,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[tag=mg.kh2l3] 0.5 66.2 22052.0
execute if score $hp mg.st matches 72 run data merge entity @e[tag=mg.kh2l3,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[tag=mg.kh2l3] 0.5 66.2 22057.25
execute if score $hp mg.st matches 60 run data merge entity @e[tag=mg.kh2l4,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[tag=mg.kh2l4] 0.5 66.2 22049.83
execute if score $hp mg.st matches 72 run data merge entity @e[tag=mg.kh2l4,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[tag=mg.kh2l4] 0.5 66.2 22056.83
execute if score $hp mg.st matches 60 run data merge entity @e[tag=mg.kh2l5,limit=1] {teleport_duration:4}
execute if score $hp mg.st matches 60 run tp @e[tag=mg.kh2l5] 0.5 66.2 22047.67
execute if score $hp mg.st matches 72 run data merge entity @e[tag=mg.kh2l5,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[tag=mg.kh2l5] 0.5 66.2 22056.42
execute if score $hp mg.st matches 61..70 positioned 0.5 65.0 22056.0 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.9] run function mg:kart/t3/hz_big
execute if score $hp mg.st matches 61..70 positioned 0.5 65.0 22053.9 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.9] run function mg:kart/t3/hz_big
execute if score $hp mg.st matches 61..70 positioned 0.5 65.0 22051.8 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.9] run function mg:kart/t3/hz_big
execute if score $hp mg.st matches 61..70 positioned 0.5 65.0 22049.7 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.9] run function mg:kart/t3/hz_big
execute if score $hp mg.st matches 61..70 positioned 0.5 65.0 22047.6 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.9] run function mg:kart/t3/hz_big
execute if score $hp mg.st matches 61..70 positioned 0.5 65.0 22045.5 as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.9] run function mg:kart/t3/hz_big
execute if score $hp mg.st matches 72 run data merge entity @e[tag=mg.kh2,limit=1] {teleport_duration:15}
execute if score $hp mg.st matches 72 run tp @e[tag=mg.kh2] 0.5 66.2 22056.0
function mg:kart/bat_tick
