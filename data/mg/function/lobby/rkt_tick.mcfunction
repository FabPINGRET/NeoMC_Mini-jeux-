# @s : roquette du lobby en vol (3 pas de 0,7 bloc par tick, 3 s au plus)
scoreboard players add @s mg.gpc 1
execute if score @s mg.gpc matches 60.. run return run function mg:lobby/rkt_boom
function mg:lobby/rkt_step
execute if entity @s at @s run function mg:lobby/rkt_step
execute if entity @s at @s run function mg:lobby/rkt_step
execute if entity @s run particle minecraft:flame ~ ~ ~ 0.05 0.05 0.05 0.02 3
