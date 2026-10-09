# @s = joueur en décompte (phase 1, 5 s) : titres et sons pour lui seul ; mg.xst = ticks depuis le lancement (titre 5 au lancement)
execute if score @s mg.xst matches 20 run title @s title [{"text":"4","color":"yellow","bold":true}]
execute if score @s mg.xst matches 20 at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1
execute if score @s mg.xst matches 40 run title @s title [{"text":"3","color":"gold","bold":true}]
execute if score @s mg.xst matches 40 at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.2
execute if score @s mg.xst matches 60 run title @s title [{"text":"2","color":"red","bold":true}]
execute if score @s mg.xst matches 60 at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.4
execute if score @s mg.xst matches 80 run title @s title [{"text":"1","color":"dark_red","bold":true}]
execute if score @s mg.xst matches 80 at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.6
execute if score @s mg.xst matches 100.. run function mg:elyrace/solo/go
