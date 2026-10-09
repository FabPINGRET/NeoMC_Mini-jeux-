# Sous-pas : x, z puis y (chacun annulé / rebondi si la balle entre dans un bloc plein)
scoreboard players operation $gfd mg.st = @s mg.gfu
scoreboard players operation $gfd mg.st /= #gf4 mg.st
scoreboard players operation @s mg.gfx += $gfd mg.st
execute store result entity @s Pos[0] double 0.001 run scoreboard players get @s mg.gfx
execute at @s unless block ~ ~0.05 ~ #mg:golf_pass run function mg:golf/hit_x
scoreboard players operation $gfd mg.st = @s mg.gfw
scoreboard players operation $gfd mg.st /= #gf4 mg.st
scoreboard players operation @s mg.gfz += $gfd mg.st
execute store result entity @s Pos[2] double 0.001 run scoreboard players get @s mg.gfz
execute at @s unless block ~ ~0.05 ~ #mg:golf_pass run function mg:golf/hit_z
scoreboard players operation $gfd mg.st = @s mg.gfv
scoreboard players operation $gfd mg.st /= #gf4 mg.st
scoreboard players operation @s mg.gfy += $gfd mg.st
execute store result entity @s Pos[1] double 0.001 run scoreboard players get @s mg.gfy
execute if score $gfd mg.st matches ..-1 at @s unless block ~ ~ ~ #mg:golf_pass run function mg:golf/hit_down
execute if score $gfd mg.st matches 1.. at @s unless block ~ ~ ~ #mg:golf_pass run function mg:golf/hit_up
execute unless entity @s[tag=mg.gfmv] run return 0
execute at @s if block ~ ~ ~ minecraft:water run return run function mg:golf/penalty_water
execute if score $gfsp0 mg.st matches ..420 at @s if block ~ ~-0.2 ~ minecraft:cauldron run function mg:golf/holed
