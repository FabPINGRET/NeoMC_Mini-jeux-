execute as @e[tag=blue_light,distance=0..] at @s run particle minecraft:soul_fire_flame ~ ~ ~ 0.2 0.2 0.2 0 1 force
execute as @e[tag=blue_light,distance=0..] at @s if entity @a[gamemode=!spectator,distance=..1,tag=mg.flw] run schedule function floaty:sched/game/blue_light_spawn 1s
execute as @e[tag=blue_light,distance=0..] at @s if score Inventory DungeonFlag matches 1 run tp @a[distance=..1,tag=mg.flw] -2 57 -26 180 0
execute as @e[tag=blue_light,distance=0..] at @s if score Inventory DungeonFlag matches 2 run tp @a[distance=..1,tag=mg.flw] -341 57 -246 0 0
execute as @e[tag=blue_light,distance=0..] at @s if score Inventory DungeonFlag matches 3 run tp @a[distance=..1,tag=mg.flw] 283 57 -166 180 0
execute as @e[tag=blue_light,distance=0..] at @s if score Inventory DungeonFlag matches 4 run tp @a[distance=..1,tag=mg.flw] 9900 57 -241 0 0
execute as @e[tag=blue_light,distance=0..] at @s if score Inventory DungeonFlag matches 5 run tp @a[distance=..1,tag=mg.flw] 10468 52 110 0 -30
execute as @e[tag=blue_light,distance=0..] at @s if score Inventory DungeonFlag matches 6 run tp @a[distance=..1,tag=mg.flw] 10440 58 -379 0 0
execute as @e[tag=blue_light,distance=0..] at @s if score Inventory DungeonFlag matches 7 run tp @a[distance=..1,tag=mg.flw] 10085 187 1280 180 0
execute as @e[tag=blue_light,distance=0..] at @s if score Inventory DungeonFlag matches 8 run tp @a[distance=..1,tag=mg.flw] 9799 57 77 -90 0
execute as @e[tag=blue_light,distance=0..] at @s if score Inventory DungeonFlag matches 9 run tp @a[distance=..1,tag=mg.flw] -9832 249 566 0 0
execute as @e[tag=blue_light,distance=0..] at @s if score Inventory DungeonFlag matches 10 run tp @a[distance=..1,tag=mg.flw] 9997 59 242 180 0
execute as @e[tag=blue_light,distance=0..] at @s if score Inventory DungeonFlag matches 11 run tp @a[distance=..1,tag=mg.flw] 94 47 53 90 0
