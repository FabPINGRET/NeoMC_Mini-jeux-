# Trigger mg.pl (@s = joueur) : 1 = aller sur son plot, 2 = retour au spawn, 3 = liste des plots, 101..115 = visiter le plot n°1..15 en spectateur
execute if entity @s[tag=mg.dl] run tellraw @s [{"text":"⚔ Duel en cours : termine-le (ou abandonne-le) avant.","color":"red"}]
execute if entity @s[tag=mg.dl] run scoreboard players reset @s mg.pl
# Depuis la survie ou un monde (GTA, Terra Nova, Ombrelune, Filon : tag mg.surv), l'inventaire serait perdu : retour au lobby d'abord
execute if entity @s[tag=mg.surv] unless score @s mg.pl matches 3 run tellraw @s [{"text":"⚠ Les plots se rejoignent depuis le lobby : reviens-y d'abord (menu Échap → ≡ Menu → Retour au lobby).","color":"red"}]
execute if entity @s[tag=mg.surv] unless score @s mg.pl matches 3 run return run scoreboard players reset @s mg.pl
execute if score @s mg.pl matches 1 run function mg:plot/enter
execute if score @s mg.pl matches 2 run function mg:plot/leave
execute if score @s mg.pl matches 3 run function mg:plot/list
execute if score @s mg.pl matches 101..115 run function mg:plot/visit
scoreboard players reset @s mg.pl
