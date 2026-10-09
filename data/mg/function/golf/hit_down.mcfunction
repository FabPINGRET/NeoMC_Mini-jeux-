# Touche le sol en descendant : dans la cuve = rentrée ; sinon posée sur le bloc, rebond si l'impact est fort
execute if score @s mg.gfv matches ..-150 at @s if block ~ ~ ~ minecraft:cauldron run return run function mg:golf/holed
execute if score $gfsp0 mg.st matches ..420 at @s if block ~ ~ ~ minecraft:cauldron run return run function mg:golf/holed
scoreboard players operation @s mg.gfy /= #gf1000 mg.st
scoreboard players add @s mg.gfy 1
scoreboard players operation @s mg.gfy *= #gf1000 mg.st
execute store result entity @s Pos[1] double 0.001 run scoreboard players get @s mg.gfy
execute if score @s mg.gfv matches ..-150 at @s run return run function mg:golf/bounce
scoreboard players set @s mg.gfv 0
