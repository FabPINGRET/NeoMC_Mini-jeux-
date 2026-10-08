# The Dropper : Aventure — chaque tick
scoreboard players add $dat mg.st 1
scoreboard players remove @a[tag=mg.play,scores={mg.cd=1..}] mg.cd 1
execute as @a[tag=mg.play] at @s if block ~ ~ ~ minecraft:water run function mg:dropadv/success
execute as @a[tag=mg.play] at @s if block ~ ~ ~ minecraft:lava run function mg:dropadv/fail
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.cd=0,mg.t=..298}] at @s if data entity @s {OnGround:1b} unless block ~ ~ ~ minecraft:water run function mg:dropadv/fail
execute as @a[tag=mg.play,scores={mg.t=..36}] run function mg:dropadv/fail
scoreboard players operation $dam mg.st = $dat mg.st
scoreboard players operation $dam mg.st %= #k10 mg.st
execute if score $dam mg.st matches 0 as @a[tag=mg.play] run function mg:dropadv/hud
execute if score $dat mg.st matches 12000.. run return run function mg:dropadv/timeout
execute unless entity @a[tag=mg.play] run function mg:core/draw
