# Menu des thèmes de Mob Arena (@s = joueur) — fenêtre, sinon menu texte
execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Le menu est réservé aux admins.","color":"red"}]
execute unless entity @s[tag=mg.admin] run return 0
scoreboard players set $dlg mg.st 0
function mg:core/menu_mob_dialog
execute unless score $dlg mg.st matches 1 run function mg:core/menu_mob_chat
