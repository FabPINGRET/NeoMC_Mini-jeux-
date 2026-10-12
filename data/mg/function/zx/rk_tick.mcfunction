# @s : roquette en vol, 3 pas de 0,7 bloc par tick
scoreboard players add @s mg.zmc 1
execute if score @s mg.zmc matches 40.. run return run function mg:zx/rk_boom
function mg:zx/rk_step
execute if entity @s at @s run function mg:zx/rk_step
execute if entity @s at @s run function mg:zx/rk_step
execute if entity @s run particle minecraft:flame ~ ~ ~ 0.05 0.05 0.05 0.02 3
