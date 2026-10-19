# Sethkar, le pharaon-liche : plus personne, le combat est remis à zéro
scoreboard players set $ob4 mg.st 0
bossbar set mg:olb4 players
execute as @e[tag=mg.olb_sethkar] run kill @s
kill @e[tag=mg.olminion_sethkar]
kill @e[tag=mg.oljar]
