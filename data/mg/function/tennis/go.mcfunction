# Départ
scoreboard players reset @a mg.qs
scoreboard players set $tntm mg.st 0
scoreboard players set @a[tag=mg.play] mg.tngw 0
execute if entity @e[type=minecraft:mannequin,tag=mg.tnrob] run scoreboard players set Robot mg.tngw 0
scoreboard objectives setdisplay sidebar mg.tngw
tellraw @a[tag=mg.play] [{"text":"🎾 TENNIS : ","color":"yellow","bold":true},{"text":"clic droit avec la raquette quand la balle est à portée pour la renvoyer, dans la direction de ton regard. Frappe tôt (balle encore loin) = coup fort et long ; accroupi = lob. Au service : clic droit pour lancer la balle. La balle doit passer le filet et rebondir une fois dans le camp adverse. Jeux en 4 points (2 d'écart), premier à 3 jeux !","color":"gray"}]
execute if score $tncourts mg.st matches 1.. run tellraw @a[tag=mg.play] [{"text":"  Court 1 : ","color":"gold"},{"selector":"@e[scores={mg.tnc=1,mg.tns=1},type=!minecraft:marker]","color":"aqua"},{"text":" contre ","color":"gray"},{"selector":"@e[scores={mg.tnc=1,mg.tns=2},type=!minecraft:marker]","color":"red"}]
execute if score $tncourts mg.st matches 2.. run tellraw @a[tag=mg.play] [{"text":"  Court 2 : ","color":"gold"},{"selector":"@e[scores={mg.tnc=2,mg.tns=1},type=!minecraft:marker]","color":"aqua"},{"text":" contre ","color":"gray"},{"selector":"@e[scores={mg.tnc=2,mg.tns=2},type=!minecraft:marker]","color":"red"}]
execute if score $tncourts mg.st matches 3.. run tellraw @a[tag=mg.play] [{"text":"  Court 3 : ","color":"gold"},{"selector":"@e[scores={mg.tnc=3,mg.tns=1},type=!minecraft:marker]","color":"aqua"},{"text":" contre ","color":"gray"},{"selector":"@e[scores={mg.tnc=3,mg.tns=2},type=!minecraft:marker]","color":"red"}]
execute if score $tncourts mg.st matches 4.. run tellraw @a[tag=mg.play] [{"text":"  Court 4 : ","color":"gold"},{"selector":"@e[scores={mg.tnc=4,mg.tns=1},type=!minecraft:marker]","color":"aqua"},{"text":" contre ","color":"gray"},{"selector":"@e[scores={mg.tnc=4,mg.tns=2},type=!minecraft:marker]","color":"red"}]
