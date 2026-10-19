# Ysh'tar, la reine-araignée : plus personne, le combat est remis à zéro
scoreboard players set $ob1 mg.st 0
bossbar set mg:olb1 players
execute as @e[tag=mg.olb_ystar] run kill @s
kill @e[tag=mg.olminion_ystar]
kill @e[tag=mg.oljar]
