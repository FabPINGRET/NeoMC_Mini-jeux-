summon minecraft:marker ~ ~ ~ {Tags:["mg.yb","mg.ynw"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.ynw] mg.yo 0
scoreboard players set @e[type=minecraft:marker,tag=mg.ynw] mg.yr 3
scoreboard players set @e[type=minecraft:marker,tag=mg.ynw] mg.yt 40
tag @e[tag=mg.ynw] remove mg.ynw
function mg:bman/bomb_show
particle minecraft:cloud ~ ~3 ~ 0.2 0.2 0.2 0.02 8 force
playsound minecraft:entity.tnt.primed master @a ~ ~ ~ 0.6 1.6
