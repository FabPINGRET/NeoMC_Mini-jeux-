# Turf Wars — tick de jeu

# Nouvelles flèches : équipe du tireur, non ramassables
execute as @e[type=minecraft:arrow,tag=!mg.ar] at @s run function mg:turf/arrow_new
# Flèches plantées → conversion de la colonne
execute as @e[type=minecraft:arrow,tag=mg.ar,nbt={inGround:1b}] at @s run function mg:turf/landed

# Score latéral
scoreboard players operation Rouge mg.ts = $nr mg.st
scoreboard players operation Bleu mg.ts = $nb mg.st

# Actionbar permanente : rouge / bleu et objectif
title @a[tag=mg.play] actionbar [{"text":"Rouge ","color":"red"},{"score":{"name":"$nr","objective":"mg.st"},"color":"red","bold":true},{"text":"  |  Objectif 28  |  ","color":"gray"},{"text":"Bleu ","color":"blue"},{"score":{"name":"$nb","objective":"mg.st"},"color":"blue","bold":true}]

# Minuteur 6 min
scoreboard players remove $tl mg.st 1
execute if score $tl mg.st matches 1200 run tellraw @a[tag=mg.play] [{"text":"▮ Plus qu'une minute !","color":"gold"}]

# Victoire : 90 % conquis (28 colonnes sur 31), ou à la fin du temps le plus de colonnes
execute if score $nr mg.st matches 28.. run return run function mg:core/win_red
execute if score $nb mg.st matches 28.. run return run function mg:core/win_blue
execute if score $tl mg.st matches ..0 if score $nr mg.st > $nb mg.st run return run function mg:core/win_red
execute if score $tl mg.st matches ..0 if score $nb mg.st > $nr mg.st run return run function mg:core/win_blue
execute if score $tl mg.st matches ..0 run return run function mg:core/draw
