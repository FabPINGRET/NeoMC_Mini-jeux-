scoreboard players operation $oli mg.st = @s mg.olid
tag @s add mg.olorph
execute as @e[tag=mg.olbd] if score @s mg.olid = $oli mg.st run tag @e[tag=mg.olorph] remove mg.olorph
execute if entity @s[tag=mg.olorph] run kill @s
