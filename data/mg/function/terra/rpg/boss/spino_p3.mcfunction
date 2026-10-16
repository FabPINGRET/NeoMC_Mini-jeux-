# Reine enragée (25 %)
tag @s add mg.trp3
effect give @s minecraft:speed infinite 0 true
effect give @s minecraft:strength infinite 0 true
scoreboard players set @s mg.tvat 16
tag @s add mg.tvroar
playsound minecraft:entity.ender_dragon.growl hostile @a ~ ~ ~ 2 0.8
tellraw @a[tag=mg.tvw,distance=..60] {"text":"🦖 La reine du marais est enragée !","color":"red","bold":true}
