execute as @n[tag=mem_nexus,distance=0..] at @s run fill ~ ~-1 ~ ~ ~-1 ~ minecraft:lime_concrete replace minecraft:polished_blackstone
execute if block -9948 84 357 minecraft:redstone_block as @e[tag=mem_monster,distance=0..] at @s run fill ~ ~-1 ~ ~ ~-1 ~ minecraft:lime_concrete replace minecraft:polished_blackstone

execute unless score memory_health Value = memory_lasthealth Value unless items entity @n[tag=mem_nexus,distance=0..] weapon.mainhand mace run function boss:mini/memory_contagion/reveal_contagion

scoreboard players operation memory_lasthealth Value = memory_health Value
