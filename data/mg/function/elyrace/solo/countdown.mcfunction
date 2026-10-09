# Compte à rebours du solo (état 1, appelé par core/countdown) : titres et sons pour le joueur seulement
# déconnexion pendant le compte à rebours : fin immédiate
execute unless entity @a[tag=mg.play] run return run function mg:elyrace/solo/end
scoreboard players remove $timer mg.st 1
execute if score $timer mg.st matches 80 run title @a[tag=mg.play] title [{"text":"4","color":"yellow","bold":true}]
execute if score $timer mg.st matches 80 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1
execute if score $timer mg.st matches 60 run title @a[tag=mg.play] title [{"text":"3","color":"gold","bold":true}]
execute if score $timer mg.st matches 60 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.2
execute if score $timer mg.st matches 40 run title @a[tag=mg.play] title [{"text":"2","color":"red","bold":true}]
execute if score $timer mg.st matches 40 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.4
execute if score $timer mg.st matches 20 run title @a[tag=mg.play] title [{"text":"1","color":"dark_red","bold":true}]
execute if score $timer mg.st matches 20 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.6
execute if score $timer mg.st matches ..0 run function mg:core/begin
