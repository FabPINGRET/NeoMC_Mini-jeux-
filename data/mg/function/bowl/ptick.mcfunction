# @s : joueur sur sa piste, selon sa phase (0 visée, 1 boule en route, 2 quilles qui bougent, 3 requilleur, 8 attente, 9 fini)
scoreboard players add @s mg.btm 1
execute if score @s mg.bph matches 0 run return run function mg:bowl/aim
execute if score @s mg.bph matches 1 run return run function mg:bowl/rolling
execute if score @s mg.bph matches 2 run return run function mg:bowl/settle
execute if score @s mg.bph matches 3 run return run function mg:bowl/reset
execute if score @s mg.bph matches 9 run title @s actionbar [{"text":"🎳 Partie terminée : ","color":"gray"},{"score":{"name":"@s","objective":"mg.bsc"},"color":"gold","bold":true},{"text":" points — on attend les autres…","color":"gray"}]
