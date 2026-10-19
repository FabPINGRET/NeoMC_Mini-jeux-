# Nyxar, dragon de la Lune Noire : plus personne, le combat est remis à zéro
scoreboard players set $ob8 mg.st 0
bossbar set mg:olb8 players
execute as @e[tag=mg.olb_nyxar] run kill @s
kill @e[tag=mg.olminion_nyxar]
kill @e[tag=mg.oljar]
