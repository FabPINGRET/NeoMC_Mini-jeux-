# Apparition de @s (participant, $tma = arène, #tms = départ) : PV neufs, 3 s de protection (mg.tmp), tir impossible
scoreboard players set @s mg.tmhp 2
function mg:tdm/unscope
tag @s add mg.tmp
scoreboard players set @s mg.tmx 60
scoreboard players set @s mg.tmcd 0
scoreboard players set @s mg.tmkc 0
title @s actionbar {"text":"3","color":"yellow","bold":true}
execute if score $tma mg.st matches 1 positioned 0.5 89 40000.5 run function mg:tdm/spawn_slot
execute if score $tma mg.st matches 2 positioned 0.5 81 40400.5 run function mg:tdm/spawn_slot
execute if score $tma mg.st matches 3 positioned 0.5 81 40800.5 run function mg:tdm/spawn_slot
