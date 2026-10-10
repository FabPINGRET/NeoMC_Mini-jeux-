# @s = joueur : SEULE SORTIE d'un contre-la-montre solo (arrivée + 30 ticks, abandon, pause désactivée, survie / plot / visite, 3 min,
# reconnexion, arrêt admin, départ d'une course de groupe, désinstallation). Rien d'autre ne retire mg.xso.
# 1) plus aucune détection : le tag et les scores de course d'abord (mg.xse, délai de 30 s, est posé plus bas)
tag @s remove mg.xso
scoreboard players reset @s mg.xph
scoreboard players reset @s mg.xst
scoreboard players reset @s mg.xsl
# (mg.xcr appartient à la partie de groupe si une partie l'a pris comme participant)
execute unless entity @s[tag=mg.play] run scoreboard players reset @s mg.xcr
# gravité normale (0,08), sans condition : celle de course (elyrace/grav_on) ne doit pas suivre le joueur au lobby
function mg:core/attr_reset_g
# 2) la pause d'avant le solo : rétablie (mg.xsp0 = il était déjà en pause ; sinon la pause est retirée, même si une partie tourne)
execute unless entity @s[tag=mg.xsp0] run tag @s remove mg.spectate
tag @s remove mg.xsp0
scoreboard players operation @s mg.xse = $tc mg.st
# 3) retour au lobby, sauf si une partie l'a pris (participant, ou spectateur placé par core/reconnect_spec)
# ou s'il est parti en survie, dans un plot ou en visite (reset_player l'y arracherait : position de survie corrompue, boucle avec le plot)
function mg:core/unfreeze
execute unless entity @s[tag=mg.play] unless entity @s[tag=mg.out] unless entity @s[tag=mg.surv] unless entity @s[tag=mg.inplot] unless entity @s[tag=mg.visit] run function mg:core/reset_player
# plot ou visite : le point de réapparition du parcours ne doit pas rester (même point que reset_player ; survie : survie/restore l'a déjà posé)
execute if entity @s[tag=mg.inplot] in minecraft:overworld run spawnpoint @s 0 64 0
execute if entity @s[tag=mg.visit] in minecraft:overworld run spawnpoint @s 0 64 0
