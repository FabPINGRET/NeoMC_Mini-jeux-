# Vitesse (centièmes de bloc par tick) : 80 sur la route, 38 dans l'herbe, 105 en étoile, 125 en boost
scoreboard players set $kmx mg.st 80
execute if score $kro mg.st matches 0 if score $kg mg.st matches 1 run scoreboard players set $kmx mg.st 38
execute if score @s mg.kst matches 1.. run scoreboard players set $kmx mg.st 105
execute if score @s mg.kbo matches 1.. run scoreboard players set $kmx mg.st 125
execute if score @s mg.khi matches 1.. run return run function mg:kart/speed_hit

execute if score $kf mg.st matches 1 if score $kb mg.st matches 0 run scoreboard players add @s mg.ksp 4
execute if score $kb mg.st matches 1 if score $kf mg.st matches 0 if score @s mg.ksp matches 1.. run scoreboard players remove @s mg.ksp 9
execute if score $kb mg.st matches 1 if score $kf mg.st matches 0 if score @s mg.ksp matches ..0 run scoreboard players remove @s mg.ksp 3
execute if score $kf mg.st matches 0 if score $kb mg.st matches 0 if score @s mg.ksp matches 3.. run scoreboard players remove @s mg.ksp 2
execute if score $kf mg.st matches 0 if score $kb mg.st matches 0 if score @s mg.ksp matches ..-3 run scoreboard players add @s mg.ksp 2
execute if score $kf mg.st matches 0 if score $kb mg.st matches 0 if score @s mg.ksp matches -2..2 run scoreboard players set @s mg.ksp 0
execute if score @s mg.kbo matches 1.. if score @s mg.ksp < $kmx mg.st run scoreboard players operation @s mg.ksp = $kmx mg.st
execute if score @s mg.ksp > $kmx mg.st run scoreboard players remove @s mg.ksp 5
execute if score @s mg.ksp matches ..-31 run scoreboard players set @s mg.ksp -30
