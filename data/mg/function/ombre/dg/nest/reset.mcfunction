# Nid des tisseuses : remis à zéro (plus personne)
scoreboard players set $od1 mg.st 0
scoreboard players set $odw1 mg.st 0
execute as @e[tag=mg.oldg1] run kill @s
bossbar set mg:oldg1 players
execute in mg:ombrelune run function mg:ombre/dg/nest/close
