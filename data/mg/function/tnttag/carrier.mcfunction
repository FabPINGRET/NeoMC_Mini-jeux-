# Effets du porteur de la bombe, chaque tick (@s, positionné) : mèche, fumée, battement de cœur qui s'accélère
particle minecraft:flame ~ ~2.2 ~ 0.15 0.15 0.15 0.02 2
particle minecraft:smoke ~ ~0.3 ~ 0.25 0.1 0.25 0.01 2
execute if score $tt mg.st matches ..100 run particle minecraft:large_smoke ~ ~2.3 ~ 0.1 0.1 0.1 0.02 1
execute if score $tt mg.st matches ..60 run particle minecraft:lava ~ ~2.2 ~ 0.2 0.2 0.2 0 1
# Battement de cœur (que pour lui) : toutes les 20 ticks, puis 10, puis 5
scoreboard players operation $tm mg.st = $tt mg.st
scoreboard players operation $tm mg.st %= $c20 mg.st
execute if score $tt mg.st matches 101.. if score $tm mg.st matches 0 run playsound minecraft:block.note_block.basedrum master @s ~ ~ ~ 1 0.7
execute if score $tt mg.st matches 41..100 if score $tm mg.st matches 0 run playsound minecraft:block.note_block.basedrum master @s ~ ~ ~ 1 0.9
execute if score $tt mg.st matches 41..100 if score $tm mg.st matches 10 run playsound minecraft:block.note_block.basedrum master @s ~ ~ ~ 1 0.9
execute if score $tt mg.st matches 1..40 if score $tm mg.st matches 0 run playsound minecraft:block.note_block.basedrum master @s ~ ~ ~ 1 1.2
execute if score $tt mg.st matches 1..40 if score $tm mg.st matches 5 run playsound minecraft:block.note_block.basedrum master @s ~ ~ ~ 1 1.2
execute if score $tt mg.st matches 1..40 if score $tm mg.st matches 10 run playsound minecraft:block.note_block.basedrum master @s ~ ~ ~ 1 1.2
execute if score $tt mg.st matches 1..40 if score $tm mg.st matches 15 run playsound minecraft:block.note_block.basedrum master @s ~ ~ ~ 1 1.2
# Dernières secondes : compte à rebours en gros pour le porteur, sifflement de mèche pour tous
execute if score $tt mg.st matches 60 run title @s title [{"text":"3","color":"gold","bold":true}]
execute if score $tt mg.st matches 40 run title @s title [{"text":"2","color":"red","bold":true}]
execute if score $tt mg.st matches 20 run title @s title [{"text":"1","color":"dark_red","bold":true}]
execute if score $tt mg.st matches 60 run title @s subtitle [{"text":"Passe-la vite !","color":"gray"}]
execute if score $tt mg.st matches 30 run playsound minecraft:entity.creeper.primed master @a ~ ~ ~ 1.5 1
