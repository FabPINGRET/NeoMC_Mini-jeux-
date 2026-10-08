# $skz = 700 - t × 11 / 72  (t ≤ 3600) → mg:sky z.r
scoreboard players operation $skz mg.st = $skt mg.st
scoreboard players operation $skz mg.st *= #11 mg.st
scoreboard players operation $skz mg.st /= #72 mg.st
scoreboard players operation $skz mg.st *= #-1 mg.st
scoreboard players add $skz mg.st 700
execute if score $skz mg.st matches ..150 run scoreboard players set $skz mg.st 150
execute store result storage mg:sky z.r double 0.1 run scoreboard players get $skz mg.st
