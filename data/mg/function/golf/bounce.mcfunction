# Rebond (impact) selon la surface
function mg:golf/surf
scoreboard players operation @s mg.gfv *= #gfm1 mg.st
scoreboard players operation @s mg.gfv *= $gfr mg.st
scoreboard players operation @s mg.gfv /= #gf1000 mg.st
scoreboard players operation @s mg.gfu *= $gfh mg.st
scoreboard players operation @s mg.gfu /= #gf1000 mg.st
scoreboard players operation @s mg.gfw *= $gfh mg.st
scoreboard players operation @s mg.gfw /= #gf1000 mg.st
execute if score @s mg.gfv matches ..80 run scoreboard players set @s mg.gfv 0
playsound minecraft:block.wood.hit master @a ~ ~ ~ 0.5 1.8
execute if block ~ ~-0.05 ~ minecraft:sand run particle minecraft:block{block_state:"minecraft:sand"} ~ ~0.1 ~ 0.2 0.1 0.2 0 12 force
execute if block ~ ~-0.05 ~ minecraft:sand run playsound minecraft:block.sand.fall master @a ~ ~ ~ 1 0.8
