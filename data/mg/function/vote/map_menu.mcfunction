# Macro : ouvre la fenêtre $(d), sinon le menu chat des cartes du jeu $(n). Généré.
scoreboard players set $dlg mg.st 0
$execute store success score $dlg mg.st run function mg:rate/d/$(d) with storage mg:rate lab
execute if score $dlg mg.st matches 1 run return 0
$execute if score $dlg mg.st matches 0 run function mg:vote/map_chat {n:$(n)}
