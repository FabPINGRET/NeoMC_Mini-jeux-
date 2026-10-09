# @s = joueur en solo, mort ou vivant (@a) : présence, pause, chrono
# reconnexion : mg.xsl doit valoir le tick précédent ($tc - 1), sinon le joueur n'était pas en ligne (core/reconnect l'a déjà remis au lobby)
scoreboard players operation #xsl mg.st = $tc mg.st
scoreboard players remove #xsl mg.st 1
execute unless score @s mg.xsl = #xsl mg.st run return run function mg:elyrace/solo/stop
# reprise manuelle de la pause (mg.spectate retiré) : fin du solo
execute unless entity @s[tag=mg.spectate] run tellraw @s [{"text":"▶ Pause désactivée : contre-la-montre terminé.","color":"gray"}]
execute unless entity @s[tag=mg.spectate] run return run function mg:elyrace/solo/stop
scoreboard players operation @s mg.xsl = $tc mg.st
scoreboard players add @s mg.xst 1
