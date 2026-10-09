# Départ
scoreboard players set $kht mg.st 0
execute as @a[tag=mg.play] run function mg:koth3/kit
scoreboard players set @a mg.deaths 0
execute if score $khm mg.st matches 0 run scoreboard objectives setdisplay sidebar mg.kh
execute if score $khm mg.st matches 1 run scoreboard players set Rouge mg.kh 0
execute if score $khm mg.st matches 1 run scoreboard players set Bleu mg.kh 0
execute if score $khm mg.st matches 1 run scoreboard objectives setdisplay sidebar mg.kh
execute if score $khm mg.st matches 1 run scoreboard players reset @a mg.kh
tellraw @a[tag=mg.play] [{"text":"👑 KING OF THE HILL : ","color":"gold","bold":true},{"text":"reste sur le sommet en or SANS adversaire : +1 point par seconde. Solo : 60 points, équipes : 90. 5 minutes max. Réapparition illimitée.","color":"gray"}]
