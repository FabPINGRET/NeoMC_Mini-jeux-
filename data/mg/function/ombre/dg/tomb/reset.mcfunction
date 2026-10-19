# Tombeaux d'Azhar : remis à zéro (plus personne)
scoreboard players set $od4 mg.st 0
scoreboard players set $odw4 mg.st 0
execute as @e[tag=mg.oldg4] run kill @s
bossbar set mg:oldg4 players
execute in mg:ombrelune run function mg:ombre/dg/tomb/close
