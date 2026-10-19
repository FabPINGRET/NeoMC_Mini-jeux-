# Hrimgar, le géant du givre : plus personne, le combat est remis à zéro
scoreboard players set $ob2 mg.st 0
bossbar set mg:olb2 players
execute as @e[tag=mg.olb_hrimgar] run kill @s
kill @e[tag=mg.olminion_hrimgar]
kill @e[tag=mg.oljar]
