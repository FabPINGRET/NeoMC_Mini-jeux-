# @s : le frame en cours attend #pn lancers de bonus (valeur 10)
execute if score @s mg.bp1f matches 1.. run return run function mg:bowl/push2
scoreboard players operation @s mg.bp1f = @s mg.bfr
scoreboard players set @s mg.bp1s 10
scoreboard players operation @s mg.bp1n = #pn mg.st
