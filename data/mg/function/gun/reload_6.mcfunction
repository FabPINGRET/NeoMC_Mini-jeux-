# Recharge Ray Gun
execute if score @s mg.g6 matches 40.. run return 0
execute if score @s mg.g6 matches 20.. unless items entity @s container.* *[custom_data~{gun:6,pap:1b}] unless entity @s[tag=mg.gtw] run return 0
execute if score @s mg.grl matches 1.. run return 0
scoreboard players set @s mg.grl 50
execute if entity @s[tag=mg.zsc] run scoreboard players set @s mg.grl 25
scoreboard players set @s mg.grt 6
playsound minecraft:item.crossbow.loading_middle player @s ~ ~ ~ 0.8 1.2
