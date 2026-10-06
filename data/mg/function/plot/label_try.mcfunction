# Met le pseudo du propriétaire sur le panneau dès que celui-ci est chargé (@s = propriétaire)
execute store result storage mg:plot cur.n int 1 run scoreboard players get @s mg.plot
execute if function mg:plot/label_found run tag @s remove mg.plabel
function mg:plot/label_get with storage mg:plot cur
