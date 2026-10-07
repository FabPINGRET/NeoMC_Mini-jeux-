# Trajectoire (mg.khd, dixièmes de degré) : suit le nez du kart, avec retard en dérapage (glisse) et juste après
execute if score @s mg.khi matches 1.. run return 0
scoreboard players operation $kyn mg.st = $kyaw mg.st
scoreboard players operation $kyn mg.st += $kt mg.st
execute unless score @s mg.kdr matches 1.. unless score @s mg.krc matches 1.. run return run scoreboard players operation @s mg.khd = $kyn mg.st
scoreboard players operation $kdf mg.st = $kyn mg.st
scoreboard players operation $kdf mg.st -= @s mg.khd
execute if score $kdf mg.st matches 1801.. run scoreboard players remove $kdf mg.st 3600
execute if score $kdf mg.st matches ..-1801 run scoreboard players add $kdf mg.st 3600
scoreboard players set $kfac mg.st 22
execute if score @s mg.kdr matches 0 run scoreboard players set $kfac mg.st 45
scoreboard players operation $kdf mg.st *= $kfac mg.st
scoreboard players operation $kdf mg.st /= #k100 mg.st
scoreboard players operation @s mg.khd += $kdf mg.st
scoreboard players remove @s[scores={mg.krc=1..}] mg.krc 1
