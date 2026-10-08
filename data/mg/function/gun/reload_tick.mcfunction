# @s recharge
scoreboard players remove @s mg.grl 1
execute if score @s mg.grl matches 1.. run return 0
execute if score @s mg.grt matches 1 run scoreboard players set @s mg.g1 8
execute if score @s mg.grt matches 2 run scoreboard players set @s mg.g2 30
execute if score @s mg.grt matches 3 run scoreboard players set @s mg.g3 4
execute if score @s mg.grt matches 4 run scoreboard players set @s mg.g4 10
execute if score @s mg.grt matches 5 run scoreboard players set @s mg.g5 5
execute if score @s mg.grt matches 6 run scoreboard players set @s mg.g6 20
playsound minecraft:item.crossbow.loading_end player @s ~ ~ ~ 0.8 1.4
