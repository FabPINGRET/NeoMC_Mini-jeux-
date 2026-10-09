# Ouvre la fenêtre de menu (dialog) — isolée pour qu'un souci de dialog ne casse jamais menu_use
# $dlg = 1 si la fenêtre a bien été envoyée au joueur
execute store success score $dlg mg.st run function mg:rate/d/menu with storage mg:rate lab
