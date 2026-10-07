# Rattrapage : joueur hors-jeu tombé dans le vide (@s = joueur, position exécutée)
execute at @s unless entity @s[y=-2058,dy=2048] run return 0
tp @s 0.5 64 0.5
tellraw @s [{"text":"Ouf ! Rattrapé de justesse.","color":"aqua","italic":true}]
function mg:core/fall_heal
advancement grant @s only mg:secrets/vide
