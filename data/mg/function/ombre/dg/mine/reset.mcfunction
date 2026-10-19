# Mines profondes : remis à zéro (plus personne)
scoreboard players set $od6 mg.st 0
scoreboard players set $odw6 mg.st 0
execute as @e[tag=mg.oldg6] run kill @s
bossbar set mg:oldg6 players
execute in mg:ombrelune run function mg:ombre/dg/mine/close
