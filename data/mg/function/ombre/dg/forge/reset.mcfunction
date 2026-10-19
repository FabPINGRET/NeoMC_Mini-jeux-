# Forge écarlate : remis à zéro (plus personne)
scoreboard players set $od5 mg.st 0
scoreboard players set $odw5 mg.st 0
execute as @e[tag=mg.oldg5] run kill @s
bossbar set mg:oldg5 players
execute in mg:ombrelune run function mg:ombre/dg/forge/close
