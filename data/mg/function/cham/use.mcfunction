# @s a fait un clic droit avec un outil
scoreboard players set @s mg.cmq 0
execute if items entity @s weapon.mainhand *[custom_data~{chm:1}] run return run function mg:cham/tool_1
execute if items entity @s weapon.mainhand *[custom_data~{chm:2}] run return run function mg:cham/tool_2
execute if items entity @s weapon.mainhand *[custom_data~{chm:3}] run return run function mg:cham/tool_3
execute if items entity @s weapon.mainhand *[custom_data~{chm:4}] run return run function mg:cham/tool_4
execute if items entity @s weapon.mainhand *[custom_data~{chm:5}] run return run function mg:cham/tool_5
execute if items entity @s weapon.mainhand *[custom_data~{chm:10}] run return run function mg:cham/tool_10
