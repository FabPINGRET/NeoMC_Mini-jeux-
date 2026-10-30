fill -10247 93 411 -10197 104 459 air replace minecraft:white_stained_glass
fill -10247 93 411 -10197 104 459 air replace minecraft:green_stained_glass
fill -10247 93 411 -10197 104 459 air replace minecraft:lime_stained_glass
fill -10247 93 411 -10197 104 459 air replace minecraft:red_stained_glass
fill -10247 93 411 -10197 104 459 air replace minecraft:verdant_froglight[axis=x]
fill -10247 93 411 -10197 104 459 air replace minecraft:verdant_froglight[axis=z]
fill -10247 93 411 -10197 104 459 air replace minecraft:smooth_quartz_stairs

execute as @e[tag=boss_skt_hole_10,distance=0..] at @s run clone -10181 73 405 -10168 77 413 ~-12 ~1 ~-4
execute as @e[tag=boss_skt_hole_10,distance=0..] at @s run clone -10199 73 425 -10197 73 427 ~-1 ~ ~-1

summon area_effect_cloud -10213 93 444 {ReapplicationDelay:20,Radius:6f,RadiusPerTick:0.15f,RadiusOnUse:-0.1f,Duration:120,potion_contents:{custom_effects:[{id:"minecraft:wither",amplifier:0,duration:200}]}}
summon area_effect_cloud -10213 94 444 {ReapplicationDelay:20,Radius:6f,RadiusPerTick:0.15f,RadiusOnUse:-0.1f,Duration:120,potion_contents:{custom_effects:[{id:"minecraft:wither",amplifier:0,duration:200}]}}

playsound minecraft:entity.phantom.bite hostile @a[tag=mg.flw] -10213 94 444 3 0.1
particle minecraft:crit -10213 94 444 1 1 1 0.1 25
