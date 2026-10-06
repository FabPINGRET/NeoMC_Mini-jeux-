# Construction (4 min = 4800 ticks)
scoreboard players add $bbt mg.st 1
execute as @a[tag=mg.play,scores={mg.bi=0..}] run function mg:bb/confine
execute as @a[tag=mg.play,scores={mg.bi=-1}] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.bi=-1,mg.t=..50}] run tp @s -639.5 65 13650.5

scoreboard players operation $bbq mg.st = $bbt mg.st
scoreboard players operation $bbq mg.st %= $bbc20 mg.st
execute if score $bbq mg.st matches 0 run function mg:bb/bar

execute if score $bbt mg.st matches 3600 run tellraw @a[tag=mg.play] [{"text":"⏱ Plus qu'1 minute !","color":"gold"}]
execute if score $bbt mg.st matches 4200 run tellraw @a[tag=mg.play] [{"text":"⏱ 30 secondes !","color":"gold"}]
execute if score $bbt mg.st matches 4500 run tellraw @a[tag=mg.play] [{"text":"⏱ 15 secondes !","color":"red"}]
execute if score $bbt mg.st matches 4700 run title @a[tag=mg.play] title [{"text":"5","color":"red","bold":true}]
execute if score $bbt mg.st matches 4720 run title @a[tag=mg.play] title [{"text":"4","color":"red","bold":true}]
execute if score $bbt mg.st matches 4740 run title @a[tag=mg.play] title [{"text":"3","color":"red","bold":true}]
execute if score $bbt mg.st matches 4760 run title @a[tag=mg.play] title [{"text":"2","color":"red","bold":true}]
execute if score $bbt mg.st matches 4780 run title @a[tag=mg.play] title [{"text":"1","color":"red","bold":true}]
execute if score $bbt mg.st matches 4700 run execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.2
execute if score $bbt mg.st matches 4720 run execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.2
execute if score $bbt mg.st matches 4740 run execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.4
execute if score $bbt mg.st matches 4760 run execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.4
execute if score $bbt mg.st matches 4780 run execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.6
execute if score $bbt mg.st matches 4800.. run function mg:bb/vote_start
