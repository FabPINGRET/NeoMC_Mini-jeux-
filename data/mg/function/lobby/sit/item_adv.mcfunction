# @s : a consommé l'objet 🎉 Emotes (clic droit) : fenêtre des emotes si possible ; l'objet est rendu par item_tick
advancement revoke @s only mg:lobby_emote
tag @s add mg.lsg
tag @s add mg.lsw
execute unless function mg:lobby/sit/can run return 0
scoreboard players add $itm mg.lsn 1
function mg:lobby/sit/menu
