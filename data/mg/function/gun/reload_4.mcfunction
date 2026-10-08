# Recharge Fusil M14
execute if score @s mg.g4 matches 10.. run return 0
execute if score @s mg.grl matches 1.. run return 0
scoreboard players set @s mg.grl 40
execute if entity @s[tag=mg.zsc] run scoreboard players set @s mg.grl 20
scoreboard players set @s mg.grt 4
playsound minecraft:item.crossbow.loading_middle player @s ~ ~ ~ 0.8 1.2
