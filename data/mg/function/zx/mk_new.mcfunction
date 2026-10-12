# @s : grenade singe qui vient d'être lancée (le lanceur est le joueur le plus proche)
tag @s add mg.zms
scoreboard players add $zmid mg.st 1
scoreboard players operation @s mg.zmi = $zmid mg.st
summon minecraft:marker ~ ~ ~ {Tags:["mg.zent","mg.zmt","mg.zmn"]}
scoreboard players operation @e[type=minecraft:marker,tag=mg.zmn] mg.zmi = $zmid mg.st
scoreboard players operation @e[type=minecraft:marker,tag=mg.zmn] mg.zmo = @p[tag=mg.play] mg.zid
tag @e[tag=mg.zmn] remove mg.zmn
