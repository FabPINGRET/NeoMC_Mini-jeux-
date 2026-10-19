# Malveth, l'archimage : plus personne, le combat est remis à zéro
scoreboard players set $ob7 mg.st 0
bossbar set mg:olb7 players
execute as @e[tag=mg.olb_malveth] run kill @s
kill @e[tag=mg.olminion_malveth]
kill @e[tag=mg.oljar]
