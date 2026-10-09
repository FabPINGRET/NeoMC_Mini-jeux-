# Recharge Sniper
execute if score @s mg.g5 matches 5.. run return 0
execute if score @s mg.grl matches 1.. run return 0
scoreboard players set @s mg.grl 60
execute if entity @s[tag=mg.zsc] run scoreboard players set @s mg.grl 30
scoreboard players set @s mg.grt 5
playsound minecraft:item.crossbow.loading_middle player @s ~ ~ ~ 0.8 1.2
