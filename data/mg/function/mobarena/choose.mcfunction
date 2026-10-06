# Mob Arena — choix de classe via /trigger mg.cls set N (@s = joueur ; valeur lue dans $c) : 1..8, 9 = rouvrir la liste
execute unless entity @s[tag=mg.play] run return 0
execute if score $c mg.st matches 9 run return run function mg:mobarena/class_menu
execute if score $c mg.st matches 10 run return run function mg:mobarena/class_keep
execute unless score $c mg.st matches 1..8 run return 0
execute unless score $state mg.st matches 1..2 run return 0
execute if score $mt mg.st matches 3 run return run tellraw @s [{"text":"Ultra Hard : le kit est imposé.","color":"red"}]
execute if score $state mg.st matches 2 unless score $wt mg.st matches 1.. run return run tellraw @s [{"text":"Pas en plein combat : change de classe pendant la pause entre deux vagues.","color":"red"}]
scoreboard players operation @s mg.cl = $c mg.st
execute if score $c mg.st matches 1 run tellraw @s [{"text":"✔ Classe : ","color":"green"},{"text":"Guerrier","color":"white","bold":true}]
execute if score $c mg.st matches 2 run tellraw @s [{"text":"✔ Classe : ","color":"green"},{"text":"Archer","color":"green","bold":true}]
execute if score $c mg.st matches 3 run tellraw @s [{"text":"✔ Classe : ","color":"green"},{"text":"Tank","color":"aqua","bold":true}]
execute if score $c mg.st matches 4 run tellraw @s [{"text":"✔ Classe : ","color":"green"},{"text":"Assassin","color":"dark_gray","bold":true}]
execute if score $c mg.st matches 5 run tellraw @s [{"text":"✔ Classe : ","color":"green"},{"text":"Mage","color":"light_purple","bold":true}]
execute if score $c mg.st matches 6 run tellraw @s [{"text":"✔ Classe : ","color":"green"},{"text":"Pyromane","color":"gold","bold":true}]
execute if score $c mg.st matches 7 run tellraw @s [{"text":"✔ Classe : ","color":"green"},{"text":"Berserker","color":"dark_red","bold":true}]
execute if score $c mg.st matches 8 run tellraw @s [{"text":"✔ Classe : ","color":"green"},{"text":"Poséidon","color":"dark_aqua","bold":true}]
execute if score $state mg.st matches 2 run function mg:mobarena/class_apply
