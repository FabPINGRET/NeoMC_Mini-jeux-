# @s : fin d'immobilisation (filet, piège)
data merge entity @s {NoAI:0b}
tag @s remove mg.tvnetted
scoreboard players operation $tvi mg.st = @s mg.tvid
execute as @e[type=minecraft:block_display,tag=mg.tvnetd] if score @s mg.tvid = $tvi mg.st run kill @s
