# @s : mort ou chute → lâche le drapeau, réapparaît dans sa base
scoreboard players set @s mg.deaths 0
execute if entity @s[tag=mg.cfcr] run function mg:ctf3/drop_red
execute if entity @s[tag=mg.cfcb] run function mg:ctf3/drop_blue
effect clear @s minecraft:glowing
function mg:ctf3/spawn
function mg:ctf3/kit
effect give @s minecraft:resistance 3 4 true
effect give @s minecraft:instant_health 1 4 true
