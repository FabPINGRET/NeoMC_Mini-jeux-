# Mob Arena — Pyromane : lance une boule de feu dans la direction du regard (@s = joueur)
# direction = marker 1 bloc devant les yeux moins la position des yeux (x1000)
kill @e[type=minecraft:snowball,distance=..4]
execute anchored eyes positioned ^ ^ ^1 run summon minecraft:marker ~ ~ ~ {Tags:["mg.fbm"]}
execute store result score $fx mg.st run data get entity @e[type=minecraft:marker,tag=mg.fbm,limit=1] Pos[0] 1000
execute store result score $fy mg.st run data get entity @e[type=minecraft:marker,tag=mg.fbm,limit=1] Pos[1] 1000
execute store result score $fz mg.st run data get entity @e[type=minecraft:marker,tag=mg.fbm,limit=1] Pos[2] 1000
kill @e[type=minecraft:marker,tag=mg.fbm]
execute store result score $px0 mg.st run data get entity @s Pos[0] 1000
execute store result score $py0 mg.st run data get entity @s Pos[1] 1000
execute store result score $pz0 mg.st run data get entity @s Pos[2] 1000
scoreboard players operation $fx mg.st -= $px0 mg.st
scoreboard players operation $fy mg.st -= $py0 mg.st
scoreboard players remove $fy mg.st 1620
scoreboard players operation $fz mg.st -= $pz0 mg.st
function mg:mobarena/class/fireball_spawn
execute at @s run playsound minecraft:entity.blaze.shoot master @a ~ ~ ~ 0.8 1
