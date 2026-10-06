# TNT Tag — tick de jeu

# Protection anti retour immédiat
scoreboard players remove @a[tag=mg.play,scores={mg.cd=1..}] mg.cd 1

# Nettoyage : un spectateur ne peut pas garder la bombe
execute as @a[tag=mg.bomb,tag=!mg.play] run function mg:tnttag/unequip

# Chute / sortie de l'arène → éliminé
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.t=..70}] run function mg:tnttag/out
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:tnttag/out

# Pas de bombe alors qu'il reste 2+ survivants → nouvelle bombe
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $alive mg.st matches 2.. unless entity @a[tag=mg.bomb,tag=mg.play] run function mg:tnttag/new_round

# Minuteur
scoreboard players remove $tt mg.st 1
scoreboard players operation $sec mg.st = $tt mg.st
scoreboard players add $sec mg.st 19
scoreboard players operation $sec mg.st /= $c20 mg.st
execute if score $tt mg.st matches 1.. as @a[tag=mg.bomb,tag=mg.play] at @s run particle minecraft:flame ~ ~2.2 ~ 0.2 0.2 0.2 0.02 2
execute if score $tt mg.st matches 1.. run title @a[tag=mg.play] actionbar [{"text":"✹ ","color":"red"},{"selector":"@a[tag=mg.bomb,tag=mg.play]","color":"gold"},{"text":" — explosion dans ","color":"gray"},{"score":{"name":"$sec","objective":"mg.st"},"color":"red","bold":true},{"text":" s","color":"gray"}]
execute if score $tt mg.st matches 200 as @a[tag=mg.bomb,tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @a ~ ~ ~ 1.5 1
execute if score $tt mg.st matches 100 as @a[tag=mg.bomb,tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @a ~ ~ ~ 1.5 1.3
execute if score $tt mg.st matches 60 as @a[tag=mg.bomb,tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @a ~ ~ ~ 1.5 1.5
execute if score $tt mg.st matches 40 as @a[tag=mg.bomb,tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @a ~ ~ ~ 1.5 1.7
execute if score $tt mg.st matches 20 as @a[tag=mg.bomb,tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @a ~ ~ ~ 1.5 2
execute if score $tt mg.st matches 10 as @a[tag=mg.bomb,tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @a ~ ~ ~ 1.5 2
execute if score $tt mg.st matches ..0 if score $alive mg.st matches 1.. run function mg:tnttag/explode

# Victoire
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] run function mg:core/win_player
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw
