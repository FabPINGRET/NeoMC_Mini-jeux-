# Puits des âmes : remis à zéro (plus personne)
scoreboard players set $od7 mg.st 0
scoreboard players set $odw7 mg.st 0
execute as @e[tag=mg.oldg7] run kill @s
bossbar set mg:oldg7 players
execute in mg:ombrelune run function mg:ombre/dg/souls/close
