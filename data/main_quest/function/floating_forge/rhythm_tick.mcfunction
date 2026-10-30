execute as @e[tag=blade_metal_marker,tag=!sound,tag=hat,distance=0..] at @s if entity @n[tag=blade_metal,distance=..0.5] run playsound minecraft:block.note_block.hat master @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute as @e[tag=blade_metal_marker,tag=!sound,tag=rim,distance=0..] at @s if entity @n[tag=blade_metal,distance=..0.5] run playsound minecraft:block.note_block.snare master @a[tag=mg.flw] ~ ~ ~ 2 0.7
execute as @e[tag=blade_metal_marker,tag=!sound,distance=0..] at @s if entity @n[tag=blade_metal,distance=..0.5] run tag @s add sound
execute as @e[tag=blade_metal_marker,tag=!contact,distance=0..] at @s if entity @n[tag=blade_metal,distance=..1] run tag @s add contact

execute as @e[tag=blade_metal_marker,tag=contact,tag=!struck,tag=right,distance=0..] at @s if entity @n[tag=blade_metal,distance=1..] run function main_quest:floating_forge/fail
execute as @e[tag=blade_metal_marker,tag=contact,tag=!struck,tag=left,distance=0..] at @s if entity @n[tag=blade_metal,distance=1..] run function main_quest:floating_forge/fail

execute if score blade_metal_speed Value matches 21 as @e[tag=blade_metal_marker,tag=contact,tag=struck,tag=left,distance=0..] at @s if entity @n[tag=blade_metal,distance=1..] run function main_quest:floating_forge/win


execute as @e[tag=blade_metal_marker,tag=contact,distance=0..] at @s if entity @n[tag=blade_metal,distance=1..] run tag @s remove contact
execute as @e[tag=blade_metal_marker,tag=contact,distance=0..] at @s if entity @n[tag=blade_metal,distance=0.5..] run tag @s remove sound
execute as @e[tag=blade_metal_marker,distance=0..] at @s if entity @n[tag=blade_metal,distance=1..] run tag @s remove struck

execute as @e[tag=blade_metal_marker,tag=contact,tag=!left,tag=!right,distance=0..] at @s run data merge entity @s {glow_color_override:65280}
execute as @e[tag=blade_metal_marker,tag=!contact,distance=0..] at @s run data merge entity @s {glow_color_override:16777215}
execute as @e[tag=blade_metal_marker,tag=contact,tag=left,tag=!struck,distance=0..] at @s run data merge entity @s {glow_color_override:16711680}
execute as @e[tag=blade_metal_marker,tag=contact,tag=right,tag=!struck,distance=0..] at @s run data merge entity @s {glow_color_override:16711680}
execute as @e[tag=blade_metal_marker,tag=contact,tag=struck,distance=0..] at @s run data merge entity @s {glow_color_override:65280}

execute as @n[tag=blade_metal,distance=0..] at @n[tag=blade_metal_loc,distance=0..] run tp @s ~ ~ ~
execute as @n[tag=blade_metal,distance=0..] at @s if entity @n[tag=blade_metal_dest,distance=..0.25] if entity @e[tag=blade_metal_marker,tag=contact,tag=right,distance=0..] run function main_quest:floating_forge/dest_left
execute as @n[tag=blade_metal,distance=0..] at @s if entity @n[tag=blade_metal_dest,distance=..0.25] if entity @e[tag=blade_metal_marker,tag=contact,tag=left,distance=0..] run function main_quest:floating_forge/dest_right
