# @s (mob) soufflé par la roquette : vitesse dans la direction explosion → mob (contexte : explosion, tourné vers @s, levé de 22°)
summon minecraft:marker ^ ^ ^1 {Tags:["mg.zkb"]}
execute store result score $kvx mg.st run data get entity @e[type=minecraft:marker,tag=mg.zkb,limit=1] Pos[0] 1000
execute store result score $kvy mg.st run data get entity @e[type=minecraft:marker,tag=mg.zkb,limit=1] Pos[1] 1000
execute store result score $kvz mg.st run data get entity @e[type=minecraft:marker,tag=mg.zkb,limit=1] Pos[2] 1000
kill @e[type=minecraft:marker,tag=mg.zkb]
scoreboard players operation $kvx mg.st -= $kbx mg.st
scoreboard players operation $kvy mg.st -= $kby mg.st
scoreboard players operation $kvz mg.st -= $kbz mg.st
execute store result entity @s Motion[0] double 0.0014 run scoreboard players get $kvx mg.st
execute store result entity @s Motion[1] double 0.0016 run scoreboard players get $kvy mg.st
execute store result entity @s Motion[2] double 0.0014 run scoreboard players get $kvz mg.st
