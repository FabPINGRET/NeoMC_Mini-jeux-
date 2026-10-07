# Marque le kart de @s (mg.kk) et sa caméra (mg.kcamc)
scoreboard players operation $me mg.st = @s mg.ri
tag @e[tag=mg.kk] remove mg.kk
tag @e[tag=mg.kcamc] remove mg.kcamc
execute as @e[type=minecraft:block_display,tag=mg.kart] if score @s mg.ri = $me mg.st run tag @s add mg.kk
execute as @e[type=minecraft:item_display,tag=mg.kcam] if score @s mg.ri = $me mg.st run tag @s add mg.kcamc
