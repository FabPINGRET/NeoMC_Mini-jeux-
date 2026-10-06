# Crée la boule de feu 1,2 bloc devant les yeux (@s = joueur) — isolé : NBT du projectile
execute anchored eyes positioned ^ ^ ^1.2 run summon minecraft:small_fireball ~ ~ ~ {Tags:["mg.fbn"],acceleration_power:0.06d,Motion:[0.0d,0.0d,0.0d]}
data modify entity @e[type=minecraft:small_fireball,tag=mg.fbn,limit=1] Owner set from entity @s UUID
execute store result entity @e[type=minecraft:small_fireball,tag=mg.fbn,limit=1] Motion[0] double 0.0007 run scoreboard players get $fx mg.st
execute store result entity @e[type=minecraft:small_fireball,tag=mg.fbn,limit=1] Motion[1] double 0.0007 run scoreboard players get $fy mg.st
execute store result entity @e[type=minecraft:small_fireball,tag=mg.fbn,limit=1] Motion[2] double 0.0007 run scoreboard players get $fz mg.st
tag @e[type=minecraft:small_fireball,tag=mg.fbn] remove mg.fbn
