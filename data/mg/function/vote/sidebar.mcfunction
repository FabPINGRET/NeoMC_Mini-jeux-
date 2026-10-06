# Affiche les votes dans le lobby (sinon remet l'affichage habituel)
execute store result score $vn mg.st if entity @a[scores={mg.vc=1..}]
execute if score $state mg.st matches 0 if score $vn mg.st matches 1.. run scoreboard objectives setdisplay sidebar mg.vb
execute if score $state mg.st matches 0 if score $vn mg.st matches 0 if score $sb mg.st matches 1 run scoreboard objectives setdisplay sidebar mg.wins
execute if score $state mg.st matches 0 if score $vn mg.st matches 0 unless score $sb mg.st matches 1 run scoreboard objectives setdisplay sidebar
