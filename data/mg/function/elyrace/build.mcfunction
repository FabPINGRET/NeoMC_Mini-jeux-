# (OP) Reconstruit tous les parcours, l'un après l'autre (chacun en tranches chargées de force)
# pas pendant une partie de la course : build_abort libérerait la zone de départ chargée par fl_add
execute if score $game mg.st matches 66 unless score $state mg.st matches 0 run return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d'élytres : construction impossible pendant une partie.","color":"red"}]
# ni pendant un contre-la-montre solo (il ne passe pas par $state)
execute if entity @a[tag=mg.xso] run return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d'élytres : construction impossible pendant un contre-la-montre solo.","color":"red"}]
function mg:elyrace/build_abort
function mg:elyrace/forget
function mg:elyrace/build_next
