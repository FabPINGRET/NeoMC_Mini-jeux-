# Recharge Mitraillette MP5
execute if score @s mg.g2 matches 60.. run return 0
execute if score @s mg.g2 matches 30.. unless items entity @s container.* *[custom_data~{gun:2,pap:1b}] unless entity @s[tag=mg.gtw] run return 0
execute if score @s mg.grl matches 1.. run return 0
scoreboard players set @s mg.grl 40
execute if entity @s[tag=mg.zsc] run scoreboard players set @s mg.grl 20
scoreboard players set @s mg.grt 2
playsound minecraft:item.crossbow.loading_middle player @s ~ ~ ~ 0.8 1.2
