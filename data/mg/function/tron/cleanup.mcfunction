execute as @a run ride @s dismount
kill @e[tag=mg.trm]
kill @e[tag=mg.trp]
execute as @e[tag=mg.trh] run tp @s ~ -100 ~
kill @e[tag=mg.trh]
execute as @a run attribute @s minecraft:jump_strength base reset
scoreboard players reset @a mg.trc
scoreboard players reset @a mg.trs
