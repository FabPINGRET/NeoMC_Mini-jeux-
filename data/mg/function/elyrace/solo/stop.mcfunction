# @s = joueur : SEULE SORTIE d'un contre-la-montre solo (arrivée + 30 ticks, abandon, reprise de la pause, 3 min, reconnexion,
# arrêt admin, départ d'une course de groupe). Rien d'autre ne retire mg.xso.
# 1) plus aucune détection : le tag et les scores de course d'abord (mg.xse, délai de 30 s, est posé plus bas)
tag @s remove mg.xso
scoreboard players reset @s mg.xph
scoreboard players reset @s mg.xst
scoreboard players reset @s mg.xsl
# (mg.xcr appartient à la partie de groupe si une partie l'a pris comme participant)
execute unless entity @s[tag=mg.play] run scoreboard players reset @s mg.xcr
# 2) la pause d'avant le solo : rétablie (mg.xsp0 = il était déjà en pause ; sinon la pause est retirée, même si une partie tourne)
execute unless entity @s[tag=mg.xsp0] run tag @s remove mg.spectate
tag @s remove mg.xsp0
scoreboard players operation @s mg.xse = $tc mg.st
# 3) retour au lobby, sauf si une partie l'a pris (participant, ou spectateur placé par core/reconnect_spec)
function mg:core/unfreeze
execute unless entity @s[tag=mg.play] unless entity @s[tag=mg.out] run function mg:core/reset_player
