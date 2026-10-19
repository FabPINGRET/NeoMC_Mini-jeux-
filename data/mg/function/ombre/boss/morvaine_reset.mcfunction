# Morvaine, la mère-sorcière : plus personne, le combat est remis à zéro
scoreboard players set $ob3 mg.st 0
bossbar set mg:olb3 players
execute as @e[tag=mg.olb_morvaine] run kill @s
kill @e[tag=mg.olminion_morvaine]
kill @e[tag=mg.oljar]
