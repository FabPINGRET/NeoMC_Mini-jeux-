# Ray Gun : explosion (2,5 blocs)
scoreboard players set $gstop mg.st 1
particle minecraft:dust{color:[0.3,1.0,0.4],scale:2.5} ~ ~ ~ 0.6 0.6 0.6 0 30
playsound minecraft:entity.generic.explode player @a ~ ~ ~ 0.5 1.8
execute as @e[tag=mg.gtg,tag=!mg.ghd,distance=..2.5] run function mg:gun/hit
