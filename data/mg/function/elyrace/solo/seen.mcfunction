# @s = joueur en solo, mort ou vivant (@a) : activité quittée, présence, pause, chrono
# le joueur est parti en survie, dans un plot ou en visite (ces activités étaient fermées par mg.play avant le solo par joueur) :
# fin du solo AVANT toute règle de course (c<N>/player le verrait hors zone et c<N>/respawn le ramènerait sur le parcours) ;
# stop ne le ramène pas au lobby. survie/tick passe avant solo/tick (survie vue au même tick), plot/cmd après (vu au tick suivant)
execute if entity @s[tag=mg.surv] run tellraw @s [{"text":"Tu es parti en survie : contre-la-montre terminé.","color":"gray"}]
execute if entity @s[tag=mg.surv] run return run function mg:elyrace/solo/stop
execute if entity @s[tag=mg.inplot] run tellraw @s [{"text":"Tu es parti sur ton plot : contre-la-montre terminé.","color":"gray"}]
execute if entity @s[tag=mg.inplot] run return run function mg:elyrace/solo/stop
execute if entity @s[tag=mg.visit] run tellraw @s [{"text":"Tu es parti en visite de plot : contre-la-montre terminé.","color":"gray"}]
execute if entity @s[tag=mg.visit] run return run function mg:elyrace/solo/stop
# reconnexion : mg.xsl doit valoir le tick précédent ($tc - 1), sinon le joueur n'était pas en ligne (core/reconnect l'a déjà remis au lobby)
scoreboard players operation #xsl mg.st = $tc mg.st
scoreboard players remove #xsl mg.st 1
execute unless score @s mg.xsl = #xsl mg.st run return run function mg:elyrace/solo/stop
# pause désactivée à la main (mg.spectate retiré) : fin du solo
execute unless entity @s[tag=mg.spectate] run tellraw @s [{"text":"▶ Pause désactivée : contre-la-montre terminé.","color":"gray"}]
execute unless entity @s[tag=mg.spectate] run return run function mg:elyrace/solo/stop
scoreboard players operation @s mg.xsl = $tc mg.st
scoreboard players add @s mg.xst 1
