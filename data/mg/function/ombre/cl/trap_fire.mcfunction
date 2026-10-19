# @s (piège) : un monstre marche dessus
scoreboard players operation $own mg.st = @s mg.olo
tag @a remove mg.olcast
execute as @a[tag=mg.olw] if score @s mg.olpid = $own mg.st run tag @s add mg.olcast
execute store result storage mg:ombre s.d int 1 run scoreboard players get @s mg.olpw
execute as @e[tag=mg.olm,distance=..1.4,sort=nearest,limit=1] at @s run function mg:ombre/cl/trap_hit with storage mg:ombre s
playsound minecraft:block.chain.break hostile @a ~ ~ ~ 1 0.6
particle minecraft:crit ~ ~0.5 ~ 0.4 0.3 0.4 0.2 15
tag @a remove mg.olcast
function mg:ombre/cl/trap_rm
