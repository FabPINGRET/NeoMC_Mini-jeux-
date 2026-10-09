# Collision en x : marche d'un bloc franchie en roulant, sinon retour et rebond (−40 %)
execute if entity @s[tag=mg.gfg] if score $gfsp0 mg.st matches 60.. at @s if block ~ ~1.05 ~ #mg:golf_pass run return run function mg:golf/step_up
scoreboard players operation @s mg.gfx -= $gfd mg.st
execute store result entity @s Pos[0] double 0.001 run scoreboard players get @s mg.gfx
scoreboard players operation @s mg.gfu *= #gfm1 mg.st
scoreboard players set $gfk mg.st 4
scoreboard players operation @s mg.gfu *= $gfk mg.st
scoreboard players operation @s mg.gfu /= #gf10 mg.st
execute if score $gfsp0 mg.st matches 200.. at @s run playsound minecraft:block.wood.hit master @a ~ ~ ~ 0.6 1.6
