# Fin de la construction → phase de notation
scoreboard players set $bbp mg.st 2
scoreboard players set $bbk mg.st -1
clear @a[tag=mg.play]
gamemode spectator @a[tag=mg.play]
title @a[tag=mg.play] title [{"text":"⏱ Temps écoulé !","color":"gold","bold":true}]
title @a[tag=mg.play] subtitle [{"text":"Place au vote : note chaque construction de 1 à 5","color":"gray"}]
tellraw @a[tag=mg.play] [{"text":"\n★ PLACE AU VOTE ! ","color":"gold","bold":true},{"text":"Chaque construction est présentée 18 secondes. Note-la de 1 à 5 (fenêtre automatique, boutons dans le chat ou ","color":"gray"},{"text":"/trigger mg.bb set 1..5","color":"yellow"},{"text":"). Tu ne peux pas noter ta propre construction.","color":"gray"}]
execute if score $bbs mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"(Mode test solo : tu peux noter ta propre construction.)","color":"dark_gray","italic":true}]
function mg:bb/vote_next
