# Menu Mini Party (@s, mg.dice 5..9) : caméra, vue libre, objets, classement, règles
execute unless score $mp mg.st matches 1 unless score @s mg.dice matches 9 run tellraw @s [{"text":"Aucune Mini Party en cours.","color":"gray"}]
execute if score $mp mg.st matches 1 unless entity @s[tag=mg.mpp] if score @s mg.dice matches 5..7 run tellraw @s [{"text":"Tu ne participes pas à la Mini Party en cours.","color":"gray"}]
execute if score $mp mg.st matches 1 if entity @s[tag=mg.mpp] if score @s mg.dice matches 5..6 unless score $game mg.st matches 59 run tellraw @s [{"text":"La caméra est disponible sur le plateau.","color":"gray"}]
execute if score $mp mg.st matches 1 if entity @s[tag=mg.mpp] if score $game mg.st matches 59 if score @s mg.dice matches 5 run function mg:party/cam_on
execute if score $mp mg.st matches 1 if entity @s[tag=mg.mpp] if score $game mg.st matches 59 if score @s mg.dice matches 6 run function mg:party/cam_free
execute if score $mp mg.st matches 1 if entity @s[tag=mg.mpp] if score @s mg.dice matches 7 run function mg:party/menu_inv
execute if score $mp mg.st matches 1 if score @s mg.dice matches 8 run function mg:party/menu_rank
execute if score @s mg.dice matches 9 run function mg:party/menu_rules
scoreboard players set @s mg.dice 0
