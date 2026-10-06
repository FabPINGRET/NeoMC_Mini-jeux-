# Ouverture du menu (@s = joueur) — chaque maillon est isolé, avec un plan B garanti
scoreboard players reset @s mg.cs
scoreboard players reset @s mg.menu

# La canne a pu être « consommée » par le clic (ou manquer) → on la (re)donne, admins comme joueurs (idempotent)
function mg:core/give_menu

# Réservé aux admins
execute unless entity @s[tag=mg.admin] run function mg:vote/open
execute unless entity @s[tag=mg.admin] run return 0

# Plan A : fenêtre (dialog). Plan B : menu texte cliquable si la fenêtre n'a pas pu s'ouvrir
scoreboard players set $dlg mg.st 0
function mg:core/menu_dialog
execute unless score $dlg mg.st matches 1 run function mg:core/menu_chat
