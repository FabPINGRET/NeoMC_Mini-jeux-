# @s éliminé : ses marqueurs et sa moto disparaissent, ses murs restent
tag @s remove mg.tme
scoreboard players operation $tid mg.st = @s mg.trc
ride @s dismount
execute as @e[tag=mg.trm] if score @s mg.trc = $tid mg.st run kill @s
execute as @e[tag=mg.trp] if score @s mg.trc = $tid mg.st run kill @s
execute as @e[tag=mg.trh] if score @s mg.trc = $tid mg.st run tp @s ~ -100 ~
execute at @s run particle minecraft:explosion ~ ~1 ~ 0.3 0.3 0.3 0 3
execute at @s run playsound minecraft:entity.generic.explode master @a ~ ~ ~ 0.6 1.6
attribute @s minecraft:jump_strength base reset
function mg:core/eliminate
