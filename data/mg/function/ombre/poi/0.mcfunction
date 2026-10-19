# @s découvre « Havreclair »
scoreboard players operation $b mg.st = @s mg.olpo
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.olpo += #p0 mg.st
