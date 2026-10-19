# @s (créature, à sa position) : son modèle la suit (os posés sur leurs articulations, image mg.olak)
scoreboard players operation $oli mg.st = @s mg.olid
execute if entity @s[tag=mg.olrp] run function mg:ombre/an_state
scoreboard players operation $olak mg.st = @s mg.olak
execute as @e[tag=mg.olbp,distance=..24] if score @s mg.olid = $oli mg.st run tag @s add mg.olbc
execute unless entity @e[tag=mg.olbc,distance=..24,limit=1] as @e[tag=mg.olbp] if score @s mg.olid = $oli mg.st run tp @s ~ ~ ~
execute unless entity @e[tag=mg.olbc,distance=..24,limit=1] as @e[tag=mg.olbp,distance=..24] if score @s mg.olid = $oli mg.st run tag @s add mg.olbc
execute if entity @s[tag=mg.olrp] rotated ~ 0 run function mg:ombre/an_sp
execute as @e[tag=mg.olbc,distance=..24] unless score @s mg.olab matches 1.. run tp @s ~ ~ ~ ~ 0
tag @e[tag=mg.olbc,distance=..24] remove mg.olbc
