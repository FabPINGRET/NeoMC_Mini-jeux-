# Ouvre la fenêtre du dé de @s : variante selon ses objets (1 dé double, 2 dé triple, 4 tuyau), objets absents grisés
scoreboard players set $rc mg.st 0
execute if score @s mg.mid matches 1.. run scoreboard players add $rc mg.st 1
execute if score @s mg.mit matches 1.. run scoreboard players add $rc mg.st 2
execute if score @s mg.mip matches 1.. run scoreboard players add $rc mg.st 4
execute if score $rc mg.st matches 0 run dialog show @s mg:party_roll_0
execute if score $rc mg.st matches 1 run dialog show @s mg:party_roll_1
execute if score $rc mg.st matches 2 run dialog show @s mg:party_roll_2
execute if score $rc mg.st matches 3 run dialog show @s mg:party_roll_3
execute if score $rc mg.st matches 4 run dialog show @s mg:party_roll_4
execute if score $rc mg.st matches 5 run dialog show @s mg:party_roll_5
execute if score $rc mg.st matches 6 run dialog show @s mg:party_roll_6
execute if score $rc mg.st matches 7 run dialog show @s mg:party_roll_7
