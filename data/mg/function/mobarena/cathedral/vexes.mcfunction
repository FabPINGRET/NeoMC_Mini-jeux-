# Nuée de vexes autour du boss (maximum 24 en même temps)
execute store result score $vx mg.st if entity @e[type=minecraft:vex,tag=mg.mob]
execute if score $vx mg.st matches 24.. run return 0
execute at @e[tag=mg.boss,limit=1] run function mg:mobarena/cathedral/vexes_at
