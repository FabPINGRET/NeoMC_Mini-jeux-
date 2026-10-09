# @s : boule, un sous-pas
scoreboard players operation #ln mg.st = @s mg.bln
execute if score $bsub mg.st matches 0 if score @s mg.bz matches 8000.. unless entity @s[tag=mg.bgut] run scoreboard players operation @s mg.bvx += @s mg.bsp
scoreboard players operation @s mg.bx += @s mg.bvx
scoreboard players operation @s mg.bz += @s mg.bvz
execute unless entity @s[tag=mg.bgut] unless score @s mg.bx matches -1500..1500 run function mg:bowl/gutter
execute unless entity @s[tag=mg.bgut] if score @s mg.bz matches 14000..20000 run function mg:bowl/ball_pins
execute if score @s mg.bz matches 20600.. run function mg:bowl/ball_pit
