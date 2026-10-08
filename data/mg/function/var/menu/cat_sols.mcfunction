# Catégorie « ❄ Jeux de sol » (@s = joueur) — fenêtre, sinon menu texte complet. Généré.
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run dialog show @s mg:cat_sols
execute unless score $dlg mg.st matches 1 run function mg:core/menu_chat
