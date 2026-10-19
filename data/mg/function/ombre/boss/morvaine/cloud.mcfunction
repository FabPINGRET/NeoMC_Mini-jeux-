# Morvaine, la mère-sorcière : cloud
execute as @a[tag=mg.olw,gamemode=adventure,distance=..20,sort=random,limit=1] at @s run summon minecraft:area_effect_cloud ~ ~ ~ {Tags:["mg.ol"],Radius:3f,Duration:120,potion_contents:{potion:"minecraft:strong_poison"},custom_particle:{type:"minecraft:entity_effect",color:[0.3,0.8,0.2,1.0]}}
