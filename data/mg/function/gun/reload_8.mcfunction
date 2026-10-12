# Recharge Revolver Python
execute if score @s mg.g8 matches 12.. run return 0
execute if score @s mg.g8 matches 6.. unless items entity @s container.* *[custom_data~{gun:8,pap:1b}] unless entity @s[tag=mg.gtw] run return 0
execute if score @s mg.grl matches 1.. run return 0
scoreboard players set @s mg.grl 40
execute if entity @s[tag=mg.zsc] run scoreboard players set @s mg.grl 20
scoreboard players set @s mg.grt 8
playsound minecraft:item.crossbow.loading_middle player @s ~ ~ ~ 0.8 1.2
