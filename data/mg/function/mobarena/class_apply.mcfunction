# Mob Arena — réapplique le kit après un changement de classe en pause (@s)
clear @s
effect clear @s
function mg:mobarena/kit
execute if score $mt mg.st matches 8 run effect give @s minecraft:water_breathing infinite 0 true
effect give @s minecraft:instant_health 1 3 true
