# Recharge Pistolet M1911
execute if score @s mg.g1 matches 8.. run return 0
execute if score @s mg.grl matches 1.. run return 0
scoreboard players set @s mg.grl 30
execute if entity @s[tag=mg.zsc] run scoreboard players set @s mg.grl 15
scoreboard players set @s mg.grt 1
playsound minecraft:item.crossbow.loading_middle player @s ~ ~ ~ 0.8 1.2
