# Compte à rebours (chaque tick, état 1)
# Kart : retenu tant que les pilotes choisissent leur kart
execute if score $game mg.st matches 61 if function mg:kart/hold run return 0
scoreboard players remove $timer mg.st 1

execute if score $timer mg.st matches 100 run title @a[tag=!mg.surv] title [{"text":"5","color":"yellow","bold":true}]
execute if score $timer mg.st matches 80 run title @a[tag=!mg.surv] title [{"text":"4","color":"yellow","bold":true}]
execute if score $timer mg.st matches 60 run title @a[tag=!mg.surv] title [{"text":"3","color":"gold","bold":true}]
execute if score $timer mg.st matches 40 run title @a[tag=!mg.surv] title [{"text":"2","color":"red","bold":true}]
execute if score $timer mg.st matches 20 run title @a[tag=!mg.surv] title [{"text":"1","color":"dark_red","bold":true}]
execute if score $timer mg.st matches 100 as @a at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1
execute if score $timer mg.st matches 80 as @a at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1
execute if score $timer mg.st matches 60 as @a at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.2
execute if score $timer mg.st matches 40 as @a at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.4
execute if score $timer mg.st matches 20 as @a at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.6

execute if score $timer mg.st matches ..0 run function mg:core/begin
