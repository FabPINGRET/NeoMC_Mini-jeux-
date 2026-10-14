# @s (piège) : un prédateur marche dessus : bloqué 6 s (carnotaure 2,5 s), 4 dégâts
scoreboard players operation $tvti mg.st = @s mg.tvid
execute as @e[tag=mg.tvhos,tag=!mg.tvnetted,distance=..1.4,sort=nearest,limit=1] at @s run function mg:terra/trap_hit
execute as @e[type=minecraft:block_display,tag=mg.tvtrapd] if score @s mg.tvid = $tvti mg.st run kill @s
playsound minecraft:block.chain.break hostile @a ~ ~ ~ 1 0.6
particle minecraft:crit ~ ~0.5 ~ 0.4 0.3 0.4 0.2 15
kill @s
