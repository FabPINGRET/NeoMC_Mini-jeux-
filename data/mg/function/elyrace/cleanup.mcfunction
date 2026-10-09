# Nettoyage de la Course d'élytres (appelé au retour au lobby) ; fin d'un solo : tick de la fin ($xse, délai de 30 s) puis drapeau $xs à 0
execute if score $xs mg.st matches 1 run scoreboard players operation $xse mg.st = $tc mg.st
scoreboard players set $xs mg.st 0
tag @a remove mg.xw1
tag @a remove mg.xtp
function mg:elyrace/fl_remove
scoreboard objectives setdisplay sidebar
