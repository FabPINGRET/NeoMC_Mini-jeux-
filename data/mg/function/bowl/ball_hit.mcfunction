# @s : quille percutée par la boule → part dans l'axe du choc (+ un peu de hasard), la boule ralentit et dévie
scoreboard players set #k mg.st 500
scoreboard players operation @s mg.bvx = #dx mg.st
scoreboard players operation @s mg.bvx *= #bvz mg.st
scoreboard players operation @s mg.bvx /= #k mg.st
execute store result score #r mg.st run random value -60..60
scoreboard players operation @s mg.bvx += #r mg.st
scoreboard players operation @s mg.bvz = #dz mg.st
scoreboard players operation @s mg.bvz *= #bvz mg.st
scoreboard players operation @s mg.bvz /= #k mg.st
scoreboard players set #k mg.st 4
scoreboard players operation #q mg.st = #bvz mg.st
scoreboard players operation #q mg.st /= #k mg.st
scoreboard players operation @s mg.bvz += #q mg.st
scoreboard players set #k mg.st 8
scoreboard players operation #q mg.st = #bvz mg.st
scoreboard players operation #q mg.st /= #k mg.st
scoreboard players operation #bvz mg.st -= #q mg.st
scoreboard players set #k mg.st 5
scoreboard players operation #q mg.st = @s mg.bvx
scoreboard players operation #q mg.st /= #k mg.st
scoreboard players operation #bvx mg.st -= #q mg.st
execute at @s run playsound minecraft:entity.zombie.attack_wooden_door master @a[tag=!mg.surv,distance=..30] ~ ~ ~ 0.7 1.4
function mg:bowl/pin_fall
