# Recharge Mitrailleuse RPK
execute if score @s mg.g7 matches 120.. run return 0
execute if score @s mg.g7 matches 60.. unless items entity @s container.* *[custom_data~{gun:7,pap:1b}] unless entity @s[tag=mg.gtw] run return 0
execute if score @s mg.grl matches 1.. run return 0
scoreboard players set @s mg.grl 80
execute if entity @s[tag=mg.zsc] run scoreboard players set @s mg.grl 40
scoreboard players set @s mg.grt 7
playsound minecraft:item.crossbow.loading_middle player @s ~ ~ ~ 0.8 1.2
