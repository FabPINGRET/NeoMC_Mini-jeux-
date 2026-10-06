# Mouton de feu : un tapis de flammes (7x7) qui SE PROPAGE (jusqu'à 17x17), retiré après 7 s
fill ~-3 ~ ~-3 ~3 ~ ~3 minecraft:fire replace minecraft:air
particle minecraft:flame ~ ~1 ~ 2 0.5 2 0.1 100
playsound minecraft:item.firecharge.use master @a ~ ~ ~ 1.2 0.8
summon minecraft:marker ~ ~ ~ {Tags:["mg.fx","mg.fxn"]}
scoreboard players set @e[tag=mg.fxn,limit=1] mg.t 140
tag @e[tag=mg.fxn] remove mg.fxn
kill @s
