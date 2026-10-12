execute unless score $evf mg.st matches 1 run bossbar set mg:ev name [{"text":"Événement : ","color":"white"},{"text":"💰 Pluie de pièces","color":"gold","bold":true},{"text":" dans 1 min","color":"gray"}]
execute unless score $evf mg.st matches 1 run tellraw @a [{"text":"🎉 ÉVÉNEMENT SURPRISE au spawn dans 1 minute : ","color":"light_purple","bold":true},{"text":"💰 Pluie de pièces","color":"gold","bold":true},{"text":"\nDes pièces tombent du ciel ! Pépite = 1, lingot = 5. Le plus riche gagne.","color":"gray"}]
execute if score $evf mg.st matches 1 run bossbar set mg:ev name [{"text":"Événement : ","color":"white"},{"text":"💰 Pluie de pièces","color":"gold","bold":true},{"text":" dans 10 s","color":"gray"}]
execute if score $evf mg.st matches 1 run tellraw @a [{"text":"🎉 ÉVÉNEMENT SURPRISE au spawn dans 10 secondes : ","color":"light_purple","bold":true},{"text":"💰 Pluie de pièces","color":"gold","bold":true},{"text":"\nDes pièces tombent du ciel ! Pépite = 1, lingot = 5. Le plus riche gagne.","color":"gray"}]
bossbar set mg:ev color yellow
execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.bell.use master @s ~ ~ ~ 1 0.8
