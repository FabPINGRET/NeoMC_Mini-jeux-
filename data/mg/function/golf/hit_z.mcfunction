# Collision en z : marche d'un bloc franchie en roulant, sinon retour et rebond (−40 %)
execute if entity @s[tag=mg.gfg] if score $gfsp0 mg.st matches 60.. at @s if block ~ ~1.05 ~ #mg:golf_pass run return run function mg:golf/step_up
scoreboard players operation @s mg.gfz -= $gfd mg.st
execute store result entity @s Pos[2] double 0.001 run scoreboard players get @s mg.gfz
scoreboard players operation @s mg.gfw *= #gfm1 mg.st
scoreboard players set $gfk mg.st 4
scoreboard players operation @s mg.gfw *= $gfk mg.st
scoreboard players operation @s mg.gfw /= #gf10 mg.st
execute if score $gfsp0 mg.st matches 200.. at @s run playsound minecraft:block.wood.hit master @a ~ ~ ~ 0.6 1.6
