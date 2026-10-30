scoreboard players set simpletoid_bet Value 2

execute positioned 9948 39 -68 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute positioned 9948 39 -68 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Xytheros","color":"#D47453"},{"text":"> Ok, I'll bet on ","color":"white"},{"text":"Horsepowah","color":"green"},{"text":" for the next race.","color":"white"}]
