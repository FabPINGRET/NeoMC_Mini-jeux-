# @s = joueur qui traverse un anneau d'or : un or de plus (mg.xu), soit -2 s sur son temps final (elyrace/bonus) ;
# c<N>/rings ne l'appelle qu'une fois par or et par course : le bonus est gardé à la réapparition
scoreboard players add @s mg.xu 1
execute at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.4
execute at @s run particle minecraft:totem_of_undying ~ ~1 ~ 0.4 0.4 0.4 0.3 25
title @s times 5 50 15
title @s subtitle [{"text":"★ -2 s","color":"gold"}]
title @s title ""
tellraw @s [{"text":"★ Anneau d'or ! ","color":"gold","bold":true},{"text":"Bonus de temps : -2 s sur ton temps final.","color":"gray"}]
