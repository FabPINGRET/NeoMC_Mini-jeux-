# $rn = points nécessaires pour le niveau ($rl + 1) = 25 × (L+1) × (L+2)
scoreboard players operation $rn mg.st = @s mg.lvl
scoreboard players add $rn mg.st 1
scoreboard players operation $rm mg.st = $rn mg.st
scoreboard players add $rm mg.st 1
scoreboard players operation $rn mg.st *= $rm mg.st
scoreboard players operation $rn mg.st *= #25 mg.st
