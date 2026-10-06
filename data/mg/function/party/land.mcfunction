# Arrivée sur la case (@s) : effet selon le type, puis pause de 2,5 s (embranchement = case bleue)
function mg:party/case_type
execute if score $ct mg.st matches 0..1 run function mg:party/eff_blue
execute if score $ct mg.st matches 5 run function mg:party/eff_blue
execute if score $ct mg.st matches 2 run function mg:party/eff_red
execute if score $ct mg.st matches 3 run function mg:party/eff_event
execute if score $ct mg.st matches 4 run function mg:party/eff_trap
scoreboard players set $mph mg.st 4
scoreboard players set $mpw mg.st 50
