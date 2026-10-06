# Quakecraft — @s vient de lancer une grenade (snowball) : un marqueur suit la boule jusqu'à l'impact
scoreboard players reset @s mg.us
scoreboard players add $gid mg.st 1
scoreboard players operation @s mg.gi = $gid mg.st
tag @e[type=minecraft:snowball,tag=!mg.grs,distance=..5,sort=nearest,limit=1] add mg.grt
execute at @e[type=minecraft:snowball,tag=mg.grt,limit=1] run summon minecraft:marker ~ ~ ~ {Tags:["mg.grm","mg.grn"]}
scoreboard players operation @e[type=minecraft:marker,tag=mg.grn,limit=1] mg.gi = $gid mg.st
scoreboard players set @e[type=minecraft:marker,tag=mg.grn,limit=1] mg.t 40
tag @e[type=minecraft:marker,tag=mg.grn] remove mg.grn
tag @e[type=minecraft:snowball,tag=mg.grt] add mg.grs
tag @e[type=minecraft:snowball,tag=mg.grt] remove mg.grt
execute at @s run playsound minecraft:entity.snowball.throw master @a ~ ~ ~ 0.8 0.6
