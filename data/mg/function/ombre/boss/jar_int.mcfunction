# @s (vase canope) : brisé
execute on target if entity @s[tag=mg.olw] at @s run playsound minecraft:block.decorated_pot.shatter master @a ~ ~ ~ 1 1
execute at @s run particle minecraft:block{block_state:"minecraft:terracotta"} ~ ~1 ~ 0.4 0.4 0.4 0 30
execute at @s run kill @e[tag=mg.oljard,distance=..1.5]
kill @s
