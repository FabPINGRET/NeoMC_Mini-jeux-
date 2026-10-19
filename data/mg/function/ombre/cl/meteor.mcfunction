# @s (météore, chaque tick) : chute puis impact
scoreboard players remove @s mg.olst 1
execute if score @s mg.olst matches 1.. run particle minecraft:flame ~ ~10 ~ 0.4 3 0.4 0.05 12 force
execute if score @s mg.olst matches 1.. run particle minecraft:dust{color:[1.0,0.3,0.1],scale:2} ~ ~0.2 ~ 3 0 3 0 10 force
execute if score @s mg.olst matches 1.. run return 0
particle minecraft:explosion_emitter ~ ~1 ~ 0 0 0 0 1 force
particle minecraft:lava ~ ~1 ~ 3 1 3 0 60 force
playsound minecraft:entity.generic.explode player @a ~ ~ ~ 2 0.6
scoreboard players operation $own mg.st = @s mg.olo
tag @a remove mg.olcast
execute as @a[tag=mg.olw] if score @s mg.olpid = $own mg.st run tag @s add mg.olcast
execute store result storage mg:ombre s.d int 1 run scoreboard players get @s mg.olpw
execute as @e[tag=mg.olm,distance=..6] at @s run function mg:ombre/cl/fire_hit with storage mg:ombre s
tag @a remove mg.olcast
kill @s
