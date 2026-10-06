# Visite du plot n° (mg.pl - 100) en spectateur (@s = joueur)
execute unless score $setup mg.st matches 1 run return run tellraw @s [{"text":"⚠ Installation manquante : un OP doit d'abord lancer ","color":"red"},{"text":"/function mg:setup","color":"yellow"}]
execute if entity @s[tag=mg.play] run return run tellraw @s [{"text":"⚠ Tu participes à la partie en cours : visite possible après.","color":"red"}]
execute if entity @s[tag=mg.out] run return run tellraw @s [{"text":"⚠ Partie en cours : visite possible après.","color":"red"}]
scoreboard players operation $v mg.t = @s mg.pl
scoreboard players remove $v mg.t 100
execute unless score $v mg.t <= $pn mg.st run return run tellraw @s [{"text":"⚠ Ce plot n'est encore à personne.","color":"red"}]
execute if score $v mg.t = @s mg.plot run return run function mg:plot/enter
execute if entity @s[tag=mg.inplot] run function mg:plot/walls_fix
tag @s remove mg.inplot
function mg:parkour/quit
tag @s add mg.visit
gamemode spectator @s
function mg:plot/visit_tp
tellraw @s [{"text":"Visite du plot n°","color":"green"},{"score":{"name":"$v","objective":"mg.t"},"color":"gold"},{"text":" en spectateur. ","color":"green"},{"text":"[autres plots]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.pl set 3"}},{"text":" ","color":"gray"},{"text":"[mon plot]","color":"green","click_event":{"action":"run_command","command":"trigger mg.pl set 1"}},{"text":" ","color":"gray"},{"text":"[spawn]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.pl set 2"}}]
