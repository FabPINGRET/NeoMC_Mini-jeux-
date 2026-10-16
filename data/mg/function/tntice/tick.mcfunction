# ✷ TNT Run glace — tick (même règles que tntrun/tick)
execute as @a[tag=mg.play] at @s if block ~ ~-1 ~ minecraft:packed_ice run setblock ~ ~-1 ~ minecraft:blue_ice
execute as @a[tag=mg.play] at @s positioned ~0.3 ~ ~0.3 if block ~ ~-1 ~ minecraft:packed_ice run setblock ~ ~-1 ~ minecraft:blue_ice
execute as @a[tag=mg.play] at @s positioned ~-0.3 ~ ~0.3 if block ~ ~-1 ~ minecraft:packed_ice run setblock ~ ~-1 ~ minecraft:blue_ice
execute as @a[tag=mg.play] at @s positioned ~0.3 ~ ~-0.3 if block ~ ~-1 ~ minecraft:packed_ice run setblock ~ ~-1 ~ minecraft:blue_ice
execute as @a[tag=mg.play] at @s positioned ~-0.3 ~ ~-0.3 if block ~ ~-1 ~ minecraft:packed_ice run setblock ~ ~-1 ~ minecraft:blue_ice
scoreboard players remove $dk mg.st 1
execute if score $dk mg.st matches ..0 run function mg:tntice/decay
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.t=..58}] run function mg:core/eliminate
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:core/eliminate
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] run function mg:core/win_player
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw
