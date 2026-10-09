# @s : rebond sur le côté (kickback), perd la moitié de sa vitesse latérale
scoreboard players operation @s mg.bvx *= #km1 mg.st
scoreboard players set #k mg.st 2
scoreboard players operation @s mg.bvx /= #k mg.st
execute at @s run playsound minecraft:block.wood.hit master @a[tag=!mg.surv,distance=..30] ~ ~ ~ 0.6 1.2
