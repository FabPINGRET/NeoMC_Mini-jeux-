# @s : flèche rechargée
give @s minecraft:arrow 1
scoreboard players set @s mg.mma 0
execute at @s run playsound minecraft:item.crossbow.loading_end player @s ~ ~ ~ 0.6 1.2
