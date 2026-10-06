# Force le menu texte (/trigger mg.menu set 2) — @s = joueur
scoreboard players reset @s mg.menu
execute unless entity @s[tag=mg.admin] run function mg:vote/chat
execute unless entity @s[tag=mg.admin] run return 0
function mg:core/menu_chat
