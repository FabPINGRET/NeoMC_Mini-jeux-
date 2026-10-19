# Temple englouti : remis à zéro (plus personne)
scoreboard players set $od3 mg.st 0
scoreboard players set $odw3 mg.st 0
execute as @e[tag=mg.oldg3] run kill @s
bossbar set mg:oldg3 players
execute in mg:ombrelune run function mg:ombre/dg/sunken/close
