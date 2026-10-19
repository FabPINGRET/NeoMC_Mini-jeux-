# Grotte de givre : remis à zéro (plus personne)
scoreboard players set $od2 mg.st 0
scoreboard players set $odw2 mg.st 0
execute as @e[tag=mg.oldg2] run kill @s
bossbar set mg:oldg2 players
execute in mg:ombrelune run function mg:ombre/dg/ice/close
