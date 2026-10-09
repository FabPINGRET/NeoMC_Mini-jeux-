# @s = marqueur 10 blocs devant la balle → $gfux / $gfuz (×1000)
execute store result score $gfux mg.st run data get entity @s Pos[0] 1000
execute store result score $gfuz mg.st run data get entity @s Pos[2] 1000
scoreboard players operation $gfux mg.st -= @e[tag=mg.gfmy,limit=1] mg.gfx
scoreboard players operation $gfuz mg.st -= @e[tag=mg.gfmy,limit=1] mg.gfz
scoreboard players operation $gfux mg.st /= #gf10 mg.st
scoreboard players operation $gfuz mg.st /= #gf10 mg.st
kill @s
