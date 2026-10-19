# Nyxar, dragon de la Lune Noire : roar
scoreboard players set @s mg.olat 20
tag @s add mg.olroar
playsound minecraft:entity.ender_dragon.growl hostile @a ~ ~ ~ 3 0.4
effect give @a[tag=mg.olw,gamemode=adventure,distance=..18] minecraft:darkness 4 0 true
effect give @a[tag=mg.olw,gamemode=adventure,distance=..18] minecraft:slowness 3 1
