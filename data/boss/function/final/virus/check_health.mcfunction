clone -12389 124 350 -12379 134 360 -12389 0 350

execute store result score world_virus_shell_1 Value run fill -12389 0 350 -12379 10 360 air replace minecraft:deepslate_copper_ore
execute store result score world_virus_shell_2 Value run fill -12389 0 350 -12379 10 360 air replace minecraft:copper_ore

scoreboard players operation world_virus_shell Value = world_virus_shell_1 Value
scoreboard players operation world_virus_shell Value += world_virus_shell_2 Value

execute store result bossbar boss:final value run scoreboard players get world_virus_shell Value

execute if score world_virus_shell Value matches ..35 run function boss:final/virus/one_left
