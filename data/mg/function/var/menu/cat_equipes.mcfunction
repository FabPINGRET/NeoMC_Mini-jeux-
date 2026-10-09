# Catégorie « ⚑ Équipes » (@s = joueur) — fenêtre, sinon menu texte complet. Généré.
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run function mg:rate/d/cat_equipes with storage mg:rate lab
execute unless score $dlg mg.st matches 1 run function mg:core/menu_chat
