# @s : quille debout ; touchée par la quille en mouvement (#px #pz, vitesse #S) si distance < 0,45
scoreboard players operation #dx mg.st = @s mg.bx
scoreboard players operation #dx mg.st -= #px mg.st
execute unless score #dx mg.st matches -450..450 run return 0
scoreboard players operation #dz mg.st = @s mg.bz
scoreboard players operation #dz mg.st -= #pz mg.st
execute unless score #dz mg.st matches -450..450 run return 0
scoreboard players operation #d2 mg.st = #dx mg.st
scoreboard players operation #d2 mg.st *= #dx mg.st
scoreboard players operation #q mg.st = #dz mg.st
scoreboard players operation #q mg.st *= #dz mg.st
scoreboard players operation #d2 mg.st += #q mg.st
execute if score #d2 mg.st matches 202500.. run return 0
scoreboard players set #k mg.st 450
scoreboard players set #k3 mg.st 3
scoreboard players set #k4 mg.st 4
scoreboard players operation @s mg.bvx = #dx mg.st
scoreboard players operation @s mg.bvx *= #S mg.st
scoreboard players operation @s mg.bvx /= #k mg.st
scoreboard players operation @s mg.bvx *= #k3 mg.st
scoreboard players operation @s mg.bvx /= #k4 mg.st
scoreboard players operation @s mg.bvz = #dz mg.st
scoreboard players operation @s mg.bvz *= #S mg.st
scoreboard players operation @s mg.bvz /= #k mg.st
scoreboard players operation @s mg.bvz *= #k3 mg.st
scoreboard players operation @s mg.bvz /= #k4 mg.st
scoreboard players set #k mg.st 5
scoreboard players operation #mvx mg.st *= #k3 mg.st
scoreboard players operation #mvx mg.st /= #k mg.st
scoreboard players operation #mvz mg.st *= #k3 mg.st
scoreboard players operation #mvz mg.st /= #k mg.st
scoreboard players operation #q mg.st = @s mg.bvx
scoreboard players operation #q mg.st /= #k3 mg.st
scoreboard players operation #mvx mg.st -= #q mg.st
scoreboard players operation #q mg.st = @s mg.bvz
scoreboard players operation #q mg.st /= #k3 mg.st
scoreboard players operation #mvz mg.st -= #q mg.st
execute at @s run playsound minecraft:block.wood.break master @a[tag=!mg.surv,distance=..30] ~ ~ ~ 0.6 1.6
function mg:bowl/pin_fall
