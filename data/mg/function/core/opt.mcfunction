# Options du menu (@s = joueur, mg.opt = valeur)
execute if score @s mg.opt matches 1 run function mg:core/opt_spec
execute if score @s mg.opt matches 2 run function mg:core/opt_sidebar
execute if score @s mg.opt matches 11 run function mg:parkour/quit
execute if score @s mg.opt matches 7 run function mg:core/menu_mob
execute if score @s mg.opt matches 8 run function mg:core/menu_sheep
execute if score @s mg.opt matches 10 run function mg:core/menu_quake
execute if score @s mg.opt matches 9 unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Seul un admin peut arrêter la partie.","color":"red"}]
execute if score @s mg.opt matches 9 if entity @s[tag=mg.admin] if score $state mg.st matches 1..2 run function mg:core/abort
execute if score @s mg.opt matches 12 unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Seul un admin peut lancer le jeu le plus voté.","color":"red"}]
execute if score @s mg.opt matches 12 if entity @s[tag=mg.admin] run function mg:vote/launch
execute if score @s mg.opt matches 13 if entity @s[tag=mg.admin] run function mg:vote/reset
scoreboard players reset @s mg.opt
