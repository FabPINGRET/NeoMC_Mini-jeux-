execute unless score $evf mg.st matches 1 run bossbar set mg:ev name [{"text":"Événement : ","color":"white"},{"text":"🗝 Chasse au trésor","color":"aqua","bold":true},{"text":" dans 1 min","color":"gray"}]
execute unless score $evf mg.st matches 1 run tellraw @a [{"text":"🎉 ÉVÉNEMENT SURPRISE au spawn dans 1 minute : ","color":"light_purple","bold":true},{"text":"🗝 Chasse au trésor","color":"aqua","bold":true},{"text":"\nUn coffre est caché sur l'île. Suis les indices, le premier qui le trouve gagne.","color":"gray"}]
execute if score $evf mg.st matches 1 run bossbar set mg:ev name [{"text":"Événement : ","color":"white"},{"text":"🗝 Chasse au trésor","color":"aqua","bold":true},{"text":" dans 10 s","color":"gray"}]
execute if score $evf mg.st matches 1 run tellraw @a [{"text":"🎉 ÉVÉNEMENT SURPRISE au spawn dans 10 secondes : ","color":"light_purple","bold":true},{"text":"🗝 Chasse au trésor","color":"aqua","bold":true},{"text":"\nUn coffre est caché sur l'île. Suis les indices, le premier qui le trouve gagne.","color":"gray"}]
bossbar set mg:ev color blue
execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.bell.use master @s ~ ~ ~ 1 0.8
