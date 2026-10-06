# Sous-menu de vote PvP (@s = joueur) : fenêtre, sinon chat cliquable
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run dialog show @s mg:vote_pvp
execute unless score $dlg mg.st matches 1 run function mg:vote/chat
