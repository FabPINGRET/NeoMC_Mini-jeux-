# Choix de classe via /trigger mg.cls set N (@s = joueur) — 1..6 = classe, 9 = rouvrir le menu
execute store result score $c mg.st run scoreboard players get @s mg.cls
scoreboard players reset @s mg.cls
execute if score $game mg.st matches 6 run return run function mg:mobarena/choose
execute unless score $pc mg.st matches 1 run return 0
execute unless entity @s[tag=mg.play] run return 0
execute unless score $state mg.st matches 1 run return run tellraw @s [{"text":"La partie a commencé : la classe est figée.","color":"red"}]
execute if score $c mg.st matches 9 run return run function mg:pvp2/menu
execute unless score $c mg.st matches 1..6 run return 0
scoreboard players operation @s mg.cl = $c mg.st
execute if score $c mg.st matches 1 run tellraw @s [{"text":"✔ Classe : ","color":"green"},{"text":"Guerrier","color":"white","bold":true}]
execute if score $c mg.st matches 2 run tellraw @s [{"text":"✔ Classe : ","color":"green"},{"text":"Archer","color":"green","bold":true}]
execute if score $c mg.st matches 3 run tellraw @s [{"text":"✔ Classe : ","color":"green"},{"text":"Tank","color":"aqua","bold":true}]
execute if score $c mg.st matches 4 run tellraw @s [{"text":"✔ Classe : ","color":"green"},{"text":"Assassin","color":"dark_gray","bold":true}]
execute if score $c mg.st matches 5 run tellraw @s [{"text":"✔ Classe : ","color":"green"},{"text":"Mage","color":"light_purple","bold":true}]
execute if score $c mg.st matches 6 run tellraw @s [{"text":"✔ Classe : ","color":"green"},{"text":"Pyromane","color":"gold","bold":true}]
