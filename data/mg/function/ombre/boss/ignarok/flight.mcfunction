# Ignarok, dragon de feu : flight
effect give @s minecraft:levitation 3 3 true
playsound minecraft:entity.ender_dragon.growl hostile @a ~ ~ ~ 3 0.8
tag @s add mg.olroar
scoreboard players set @s mg.olat 30
execute as @a[tag=mg.olw,gamemode=adventure,distance=..26] at @s run summon minecraft:marker ~ ~ ~ {Tags:["mg.ol","mg.olfall"]}
scoreboard players set @e[tag=mg.olfall] mg.olst 3
