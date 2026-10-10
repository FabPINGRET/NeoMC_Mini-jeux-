# @s n'a plus de coups
scoreboard players operation $p mg.st = @s mg.atid
ride @s dismount
execute as @e[type=#mg:at_boats,tag=mg.atb] if score @s mg.atid = $p mg.st run kill @s
execute if score $n0 mg.st matches 2.. run return run function mg:core/eliminate
scoreboard players operation @s mg.atl = $atx mg.st
function mg:autotamp/place
execute at @s run function mg:autotamp/boat
