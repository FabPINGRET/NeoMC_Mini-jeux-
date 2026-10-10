# 🚗 Autos tamponneuses — préparation ($atx = coups au départ)
function mg:autotamp/build
kill @e[type=#mg:at_boats,tag=mg.atb]
kill @e[tag=mg.ats]
summon minecraft:marker 14.0 65 37400.0 {Tags:["mg.ats","mg.fx"]}
summon minecraft:marker 12.1 65 37407.0 {Tags:["mg.ats","mg.fx"]}
summon minecraft:marker 7.0 65 37412.1 {Tags:["mg.ats","mg.fx"]}
summon minecraft:marker 0.0 65 37414.0 {Tags:["mg.ats","mg.fx"]}
summon minecraft:marker -7.0 65 37412.1 {Tags:["mg.ats","mg.fx"]}
summon minecraft:marker -12.1 65 37407.0 {Tags:["mg.ats","mg.fx"]}
summon minecraft:marker -14.0 65 37400.0 {Tags:["mg.ats","mg.fx"]}
summon minecraft:marker -12.1 65 37393.0 {Tags:["mg.ats","mg.fx"]}
summon minecraft:marker -7.0 65 37387.9 {Tags:["mg.ats","mg.fx"]}
summon minecraft:marker -0.0 65 37386.0 {Tags:["mg.ats","mg.fx"]}
summon minecraft:marker 7.0 65 37387.9 {Tags:["mg.ats","mg.fx"]}
summon minecraft:marker 12.1 65 37393.0 {Tags:["mg.ats","mg.fx"]}
execute as @e[type=minecraft:marker,tag=mg.ats] at @s run tp @s ~ ~ ~ facing 0 65 37400
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 82
scoreboard players set $pz mg.st 37400
clear @a[tag=mg.play]
effect clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
team join mg_at @a[tag=mg.play]
tag @e remove mg.atu
execute as @a[tag=mg.play] run function mg:autotamp/place
scoreboard players operation @a[tag=mg.play] mg.atl = $atx mg.st
scoreboard players set @a mg.atp 0
scoreboard players set $att mg.st 0
