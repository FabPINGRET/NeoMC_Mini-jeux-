# Nyxar, dragon de la Lune Noire : dive
effect give @s minecraft:levitation 2 4 true
tag @s add mg.olroar
scoreboard players set @s mg.olat 20
playsound minecraft:entity.ender_dragon.growl hostile @a ~ ~ ~ 3 0.5
execute as @a[tag=mg.olw,gamemode=adventure,distance=..24,sort=random,limit=1] at @s run summon minecraft:marker ~ ~ ~ {Tags:["mg.ol","mg.oldive"]}
scoreboard players set @e[tag=mg.oldive] mg.olst 3
