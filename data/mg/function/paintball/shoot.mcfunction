# Tir de peinture (@s = joueur qui maintient le clic droit)
scoreboard players reset @s mg.qs
execute if score @s mg.cd matches 1.. run return 0
execute if score @s mg.pi matches ..5 run scoreboard players set @s mg.cd 10
execute if score @s mg.pi matches ..5 run return run title @s actionbar [{"text":"✖ Plus d'encre ! Reste sur ta couleur pour recharger","color":"red"}]
scoreboard players remove @s mg.pi 6
scoreboard players set @s mg.cd 3
execute if entity @s[team=mg_red] run scoreboard players set $st mg.st 1
execute if entity @s[team=mg_blue] run scoreboard players set $st mg.st 2
tag @s add mg.qsh
scoreboard players set $rs mg.st 80
execute at @s anchored eyes positioned ^ ^ ^0.5 run function mg:paintball/ray
tag @s remove mg.qsh
execute at @s run playsound minecraft:entity.snowball.throw master @a ~ ~ ~ 0.6 1.6
