summon minecraft:marker ~ ~ ~ {Tags:["mg.cloud","mg.fx","mg.big","mg.cnew"]}
scoreboard players set @e[tag=mg.cnew] mg.cd 400
tag @e[tag=mg.cnew] remove mg.cnew
playsound minecraft:entity.generic.splash master @a ~ ~ ~ 1 0.6
