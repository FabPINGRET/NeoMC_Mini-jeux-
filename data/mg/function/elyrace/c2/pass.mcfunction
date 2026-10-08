# @s = joueur qui vient de franchir le trou du prochain anneau : un anneau de plus (les aiguillages ci-dessous lisent le nouveau total)
scoreboard players add @s mg.xa 1
execute at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.6
execute at @s run particle minecraft:happy_villager ~ ~1 ~ 0.5 0.5 0.5 0.1 12
execute if score @s mg.xa matches 4 run function mg:elyrace/cp_reached
execute if score @s mg.xa matches 8 run function mg:elyrace/cp_reached
execute if score @s mg.xa matches 13 run function mg:elyrace/cp_reached
execute if score @s mg.xa matches 17 run function mg:elyrace/cp_reached
execute if score @s mg.xa matches 20.. run function mg:elyrace/finish
function mg:elyrace/c2/hud
