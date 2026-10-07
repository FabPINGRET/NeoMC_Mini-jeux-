# Vitesse (centièmes de bloc par tick) : 100 sur la route, 45 dans l'herbe, 115 en méga, 125 en étoile, 150 en boost
scoreboard players set $kmx mg.st 100
execute if score @s mg.kty matches 2 run scoreboard players set $kmx mg.st 110
execute if score @s mg.kty matches 3 run scoreboard players set $kmx mg.st 93
execute if score @s mg.kty matches 4 run scoreboard players set $kmx mg.st 104
execute if score $kro mg.st matches 0 if score $kg mg.st matches 1 if score @s mg.kty matches 1 run scoreboard players set $kmx mg.st 45
execute if score $kro mg.st matches 0 if score $kg mg.st matches 1 if score @s mg.kty matches 2 run scoreboard players set $kmx mg.st 45
execute if score $kro mg.st matches 0 if score $kg mg.st matches 1 if score @s mg.kty matches 3 run scoreboard players set $kmx mg.st 52
execute if score $kro mg.st matches 0 if score $kg mg.st matches 1 if score @s mg.kty matches 4 run scoreboard players set $kmx mg.st 58
execute if score $kro mg.st matches 0 if score $kg mg.st matches 1 unless score @s mg.kty matches 1..4 run scoreboard players set $kmx mg.st 45
execute if score @s mg.kmg matches 1.. run scoreboard players set $kmx mg.st 115
execute if score @s mg.kst matches 1.. run scoreboard players set $kmx mg.st 125
execute if score @s mg.kbo matches 1.. run scoreboard players set $kmx mg.st 150
execute if score @s mg.khi matches 1.. run return run function mg:kart/speed_hit

scoreboard players set $kac mg.st 5
execute if score @s mg.kty matches 2 run scoreboard players set $kac mg.st 4
execute if score @s mg.kty matches 3 run scoreboard players set $kac mg.st 7
execute if score @s mg.kty matches 4 run scoreboard players set $kac mg.st 3
execute if score $kf mg.st matches 1 if score $kb mg.st matches 0 run scoreboard players operation @s mg.ksp += $kac mg.st
execute if score $kb mg.st matches 1 if score $kf mg.st matches 0 if score @s mg.ksp matches 1.. run scoreboard players remove @s mg.ksp 10
execute if score $kb mg.st matches 1 if score $kf mg.st matches 0 if score @s mg.ksp matches ..0 run scoreboard players remove @s mg.ksp 3
execute if score $kf mg.st matches 0 if score $kb mg.st matches 0 if score @s mg.ksp matches 3.. run scoreboard players remove @s mg.ksp 2
execute if score $kf mg.st matches 0 if score $kb mg.st matches 0 if score @s mg.ksp matches ..-3 run scoreboard players add @s mg.ksp 2
execute if score $kf mg.st matches 0 if score $kb mg.st matches 0 if score @s mg.ksp matches -2..2 run scoreboard players set @s mg.ksp 0
execute if score @s mg.kbo matches 1.. if score @s mg.ksp < $kmx mg.st run scoreboard players operation @s mg.ksp = $kmx mg.st
execute if score @s mg.ksp > $kmx mg.st run scoreboard players remove @s mg.ksp 6
execute if score @s mg.ksp matches ..-36 run scoreboard players set @s mg.ksp -35
