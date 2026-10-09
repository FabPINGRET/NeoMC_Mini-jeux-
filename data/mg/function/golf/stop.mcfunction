# @s = balle arrêtée
tag @s remove mg.gfmv
scoreboard players set @s mg.gfu 0
scoreboard players set @s mg.gfv 0
scoreboard players set @s mg.gfw 0
execute at @s if block ~ ~-0.05 ~ #minecraft:leaves run return run function mg:golf/penalty_tree
execute at @s if block ~ ~-0.05 ~ #minecraft:logs run return run function mg:golf/penalty_tree
execute at @s if block ~ ~-0.2 ~ minecraft:cauldron run return run function mg:golf/holed
scoreboard players operation $cur mg.st = @s mg.gfi
execute as @a[tag=mg.play] if score @s mg.gfi = $cur mg.st run function mg:golf/next
