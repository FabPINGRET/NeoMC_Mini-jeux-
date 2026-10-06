# Calcule $bh2 = 2 × PV du boss (pour tester le passage à 50 %)
execute unless entity @e[tag=mg.boss] run return 0
execute store result score $bh mg.st run data get entity @e[tag=mg.boss,limit=1] Health 1
scoreboard players operation $bh2 mg.st = $bh mg.st
scoreboard players operation $bh2 mg.st += $bh mg.st
