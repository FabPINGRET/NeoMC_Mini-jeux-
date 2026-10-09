# @s : marqueur — libellés du score (data.a / data.b, jeux data.ga / data.gb) et tableau du court
data modify entity @s data.a set value "0"
execute if score @s mg.tnp1 matches 1 run data modify entity @s data.a set value "15"
execute if score @s mg.tnp1 matches 2 run data modify entity @s data.a set value "30"
execute if score @s mg.tnp1 matches 3.. run data modify entity @s data.a set value "40"
data modify entity @s data.b set value "0"
execute if score @s mg.tnp2 matches 1 run data modify entity @s data.b set value "15"
execute if score @s mg.tnp2 matches 2 run data modify entity @s data.b set value "30"
execute if score @s mg.tnp2 matches 3.. run data modify entity @s data.b set value "40"
execute if score @s mg.tnp1 matches 3.. if score @s mg.tnp2 matches 3.. if score @s mg.tnp1 > @s mg.tnp2 run data modify entity @s data.a set value "AV"
execute if score @s mg.tnp1 matches 3.. if score @s mg.tnp2 matches 3.. if score @s mg.tnp2 > @s mg.tnp1 run data modify entity @s data.b set value "AV"
execute store result entity @s data.ga int 1 run scoreboard players get @s mg.tng1
execute store result entity @s data.gb int 1 run scoreboard players get @s mg.tng2
execute as @e[type=minecraft:text_display,tag=mg.tntd,tag=mg.tnk] run function mg:tennis/board_set with entity @e[type=minecraft:marker,tag=mg.tncm,tag=mg.tnk,limit=1] data
