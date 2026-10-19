# Cryptes de Valdor : remis à zéro (plus personne)
scoreboard players set $od0 mg.st 0
scoreboard players set $odw0 mg.st 0
execute as @e[tag=mg.oldg0] run kill @s
bossbar set mg:oldg0 players
execute in mg:ombrelune run function mg:ombre/dg/crypt/close
