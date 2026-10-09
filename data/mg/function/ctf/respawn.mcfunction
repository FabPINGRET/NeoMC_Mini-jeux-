# @s : mort ou chute → lâche le drapeau, réapparaît dans sa base
scoreboard players set @s mg.deaths 0
execute if entity @s[tag=mg.cfcr] run function mg:ctf/drop_red
execute if entity @s[tag=mg.cfcb] run function mg:ctf/drop_blue
effect clear @s minecraft:glowing
function mg:ctf/spawn
function mg:ctf/kit
effect give @s minecraft:resistance 3 4 true
effect give @s minecraft:instant_health 1 4 true
