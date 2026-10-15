# Décor saisonnier reposé après un redémarrage (appelé par core/tick tant que $thrs >= 1)
scoreboard players add $thrs mg.st 1
execute if score $thrs mg.st matches ..100 run return 0
scoreboard players set $thrs mg.st 0
function mg:lobby/theme/sync
execute if score $theme mg.st matches 1 run function mg:lobby/theme/halloween/place
execute if score $theme mg.st matches 2 run function mg:lobby/theme/noel/place
execute if score $theme mg.st matches 1.. store result storage mg:lobby theme int 1 run scoreboard players get $theme mg.st
