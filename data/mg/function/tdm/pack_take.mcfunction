# Pack ramassé (@s = joueur à 1 PV) : PV remis à 2
scoreboard players set @s mg.tmhp 2
execute at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.8 1.6
execute at @s run particle minecraft:heart ~ ~1.2 ~ 0.4 0.4 0.4 0 8
title @s actionbar {"text":"❤ Soigné","color":"green","bold":true}
