# @s recharge
scoreboard players remove @s mg.grl 1
execute if score @s mg.grl matches 1.. run return 0
execute if score @s mg.grt matches 1 run scoreboard players set @s mg.g1 8
execute if entity @s[tag=mg.gtw] if score @s mg.grt matches 1 run scoreboard players set @s mg.g1 16
execute if score @s mg.grt matches 1 if items entity @s container.* *[custom_data~{gun:1,pap:1b}] run scoreboard players set @s mg.g1 16
execute if score @s mg.grt matches 2 run scoreboard players set @s mg.g2 30
execute if entity @s[tag=mg.gtw] if score @s mg.grt matches 2 run scoreboard players set @s mg.g2 60
execute if score @s mg.grt matches 2 if items entity @s container.* *[custom_data~{gun:2,pap:1b}] run scoreboard players set @s mg.g2 60
execute if score @s mg.grt matches 3 run scoreboard players set @s mg.g3 4
execute if entity @s[tag=mg.gtw] if score @s mg.grt matches 3 run scoreboard players set @s mg.g3 8
execute if score @s mg.grt matches 3 if items entity @s container.* *[custom_data~{gun:3,pap:1b}] run scoreboard players set @s mg.g3 8
execute if score @s mg.grt matches 4 run scoreboard players set @s mg.g4 10
execute if entity @s[tag=mg.gtw] if score @s mg.grt matches 4 run scoreboard players set @s mg.g4 20
execute if score @s mg.grt matches 4 if items entity @s container.* *[custom_data~{gun:4,pap:1b}] run scoreboard players set @s mg.g4 20
execute if score @s mg.grt matches 5 run scoreboard players set @s mg.g5 5
execute if entity @s[tag=mg.gtw] if score @s mg.grt matches 5 run scoreboard players set @s mg.g5 10
execute if score @s mg.grt matches 5 if items entity @s container.* *[custom_data~{gun:5,pap:1b}] run scoreboard players set @s mg.g5 10
execute if score @s mg.grt matches 6 run scoreboard players set @s mg.g6 20
execute if entity @s[tag=mg.gtw] if score @s mg.grt matches 6 run scoreboard players set @s mg.g6 40
execute if score @s mg.grt matches 6 if items entity @s container.* *[custom_data~{gun:6,pap:1b}] run scoreboard players set @s mg.g6 40
execute if score @s mg.grt matches 7 run scoreboard players set @s mg.g7 60
execute if entity @s[tag=mg.gtw] if score @s mg.grt matches 7 run scoreboard players set @s mg.g7 120
execute if score @s mg.grt matches 7 if items entity @s container.* *[custom_data~{gun:7,pap:1b}] run scoreboard players set @s mg.g7 120
execute if score @s mg.grt matches 8 run scoreboard players set @s mg.g8 6
execute if entity @s[tag=mg.gtw] if score @s mg.grt matches 8 run scoreboard players set @s mg.g8 12
execute if score @s mg.grt matches 8 if items entity @s container.* *[custom_data~{gun:8,pap:1b}] run scoreboard players set @s mg.g8 12
playsound minecraft:item.crossbow.loading_end player @s ~ ~ ~ 0.8 1.4
