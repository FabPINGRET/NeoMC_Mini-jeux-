# Brennic, seigneur des brigands : plus personne, le combat est remis à zéro
scoreboard players set $ob0 mg.st 0
bossbar set mg:olb0 players
execute as @e[tag=mg.olb_brennic] run kill @s
kill @e[tag=mg.olminion_brennic]
kill @e[tag=mg.oljar]
