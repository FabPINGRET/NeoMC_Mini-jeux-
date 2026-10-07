# Dropper : Défi — chaque tick
scoreboard players remove @a[tag=mg.play,scores={mg.cd=1..}] mg.cd 1
scoreboard players add $dct mg.st 1
execute if score $dcph mg.st matches 2 run return run function mg:dropadv/c_inter
execute as @a[tag=mg.play,scores={mg.cd=0}] at @s if block ~ ~ ~ minecraft:water run function mg:dropadv/c_win
execute if score $dcph mg.st matches 2 run return 0
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.cd=0,mg.t=..198}] at @s if data entity @s {OnGround:1b} unless block ~ ~ ~ minecraft:water run function mg:dropadv/c_fail
execute as @a[tag=mg.play,scores={mg.t=..91}] run function mg:dropadv/c_fail
scoreboard players operation $dam mg.st = $dct mg.st
scoreboard players operation $dam mg.st %= #k10 mg.st
execute if score $dam mg.st matches 0 as @a[tag=mg.play] run function mg:dropadv/c_hud
execute if score $dct mg.st matches 1800.. run function mg:dropadv/c_timeout
execute unless entity @a[tag=mg.play] run function mg:core/draw
