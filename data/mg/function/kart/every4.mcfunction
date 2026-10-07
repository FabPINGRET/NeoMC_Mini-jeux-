scoreboard players set $kph mg.st 0
scoreboard players add $kbr mg.st 1
execute if score $kbr mg.st matches 4.. run scoreboard players set $kbr mg.st 0
execute if score $kbr mg.st matches 0 as @e[type=minecraft:item_display,tag=mg.kbox] run data merge entity @s {start_interpolation:0,interpolation_duration:4,transformation:{left_rotation:{angle:0f,axis:[0f,1f,0f]}}}
execute if score $kbr mg.st matches 1 as @e[type=minecraft:item_display,tag=mg.kbox] run data merge entity @s {start_interpolation:0,interpolation_duration:4,transformation:{left_rotation:{angle:1.5708f,axis:[0f,1f,0f]}}}
execute if score $kbr mg.st matches 2 as @e[type=minecraft:item_display,tag=mg.kbox] run data merge entity @s {start_interpolation:0,interpolation_duration:4,transformation:{left_rotation:{angle:3.1416f,axis:[0f,1f,0f]}}}
execute if score $kbr mg.st matches 3 as @e[type=minecraft:item_display,tag=mg.kbox] run data merge entity @s {start_interpolation:0,interpolation_duration:4,transformation:{left_rotation:{angle:4.7124f,axis:[0f,1f,0f]}}}
execute as @a[tag=mg.play] run function mg:kart/progress
execute as @a[tag=mg.play] run function mg:kart/rank_one
execute as @a[tag=mg.play] run function mg:kart/hud
