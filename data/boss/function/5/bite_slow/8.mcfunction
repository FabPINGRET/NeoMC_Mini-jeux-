fill -10247 93 411 -10197 104 459 air replace minecraft:white_stained_glass
fill -10247 93 411 -10197 104 459 air replace minecraft:green_stained_glass
fill -10247 93 411 -10197 104 459 air replace minecraft:lime_stained_glass
fill -10247 93 411 -10197 104 459 air replace minecraft:red_stained_glass
fill -10247 93 411 -10197 104 459 air replace minecraft:verdant_froglight[axis=x]
fill -10247 93 411 -10197 104 459 air replace minecraft:verdant_froglight[axis=z]
fill -10247 93 411 -10197 104 459 air replace minecraft:smooth_quartz_stairs

execute as @e[tag=boss_skt_hole_8,distance=0..] at @s run clone -10175 73 415 -10167 77 428 ~-4 ~1 ~-12
execute as @e[tag=boss_skt_hole_8,distance=0..] at @s run clone -10199 73 421 -10197 73 423 ~-1 ~ ~-1

summon area_effect_cloud -10222 93 445 {ReapplicationDelay:20,Radius:6f,RadiusPerTick:0.15f,RadiusOnUse:-0.1f,Duration:120,potion_contents:{custom_effects:[{id:"minecraft:wither",amplifier:0,duration:200}]}}
summon area_effect_cloud -10222 94 445 {ReapplicationDelay:20,Radius:6f,RadiusPerTick:0.15f,RadiusOnUse:-0.1f,Duration:120,potion_contents:{custom_effects:[{id:"minecraft:wither",amplifier:0,duration:200}]}}

playsound minecraft:entity.phantom.bite hostile @a[tag=mg.flw] -10222 94 445 3 0.1
particle minecraft:crit -10222 94 445 1 1 1 0.1 25
