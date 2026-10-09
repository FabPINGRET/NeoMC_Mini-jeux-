# Recharge Fusil à pompe
execute if score @s mg.g3 matches 4.. run return 0
execute if score @s mg.grl matches 1.. run return 0
scoreboard players set @s mg.grl 50
execute if entity @s[tag=mg.zsc] run scoreboard players set @s mg.grl 25
scoreboard players set @s mg.grt 3
playsound minecraft:item.crossbow.loading_middle player @s ~ ~ ~ 0.8 1.2
