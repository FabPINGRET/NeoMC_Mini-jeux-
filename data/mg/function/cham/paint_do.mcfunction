# @s : peint la partie $cmpp (1 tout, 2 tête, 3 corps, 4 bras, 5 jambes) avec la matière $cmm
scoreboard players operation $cmid mg.st = @s mg.cmid
execute store result storage mg:cham p.m int 1 run scoreboard players get $cmm mg.st
execute if score $cmpp mg.st matches 1 run data modify storage mg:cham p.k1 set value 1b
execute if score $cmpp mg.st matches 1 run data modify storage mg:cham p.k2 set value 1b
execute if score $cmpp mg.st matches 1 run data modify storage mg:cham p.k3 set value 1b
execute if score $cmpp mg.st matches 1 run data modify storage mg:cham p.k4 set value 1b
execute if score $cmpp mg.st matches 1 run data modify storage mg:cham p.k5 set value 1b
execute if score $cmpp mg.st matches 1 run data modify storage mg:cham p.k6 set value 1b
execute if score $cmpp mg.st matches 2 run data modify storage mg:cham p.k1 set value 1b
execute if score $cmpp mg.st matches 3 run data modify storage mg:cham p.k2 set value 1b
execute if score $cmpp mg.st matches 4 run data modify storage mg:cham p.k3 set value 1b
execute if score $cmpp mg.st matches 4 run data modify storage mg:cham p.k4 set value 1b
execute if score $cmpp mg.st matches 5 run data modify storage mg:cham p.k5 set value 1b
execute if score $cmpp mg.st matches 5 run data modify storage mg:cham p.k6 set value 1b
function mg:cham/paint_apply with storage mg:cham p
data remove storage mg:cham p
execute at @s run playsound minecraft:block.honey_block.place player @s ~ ~ ~ 0.8 1.3
function mg:cham/hud
