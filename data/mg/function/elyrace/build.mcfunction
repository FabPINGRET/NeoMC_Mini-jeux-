# (OP) Construit le Canyon du Couchant en 11 tranches de 96 blocs (chargées de force une à une)
# pas pendant une partie de la course : build_abort libérerait la zone de départ chargée par fl_add
execute if score $game mg.st matches 66 unless score $state mg.st matches 0 run return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d'élytres : construction impossible pendant une partie.","color":"red"}]
function mg:elyrace/build_abort
data remove storage mg:elyrace v1
scoreboard players set $xbk mg.st 1
scoreboard players set $xbw mg.st 0
forceload add -16 26848 79 27151
schedule function mg:elyrace/build_wait 20t
