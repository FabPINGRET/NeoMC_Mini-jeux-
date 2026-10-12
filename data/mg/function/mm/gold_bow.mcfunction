# @s : 10 pièces → un arc, ou une flèche si on en a déjà un
clear @s minecraft:gold_ingot 10
scoreboard players remove @s mg.mmo 10
execute at @s run playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
execute unless items entity @s container.* minecraft:bow run return run function mg:mm/gold_newbow
give @s minecraft:arrow 1
title @s actionbar {"text":"🪙 10 pièces → +1 flèche","color":"gold"}
