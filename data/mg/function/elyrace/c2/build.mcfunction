# (OP) Reconstruit le parcours 2 (Pic Blanc) seul, en 12 tranches de 96 blocs (chargées de force une à une)
# pas pendant une partie de la course : build_abort libérerait la zone de départ chargée par fl_add
execute if score $game mg.st matches 66 unless score $state mg.st matches 0 run return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d'élytres : construction impossible pendant une partie.","color":"red"}]
function mg:elyrace/build_abort
data remove storage mg:elyrace c2v2
function mg:elyrace/c2/build_start
