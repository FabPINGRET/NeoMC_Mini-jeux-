# @s a abattu un monstre : XP × zone (selon sa position), partage de moitié aux colons à 24 blocs, compteur
scoreboard players add @s mg.trkt 1
$scoreboard players set $xk mg.st $(n)
scoreboard players set $zm mg.st 2
execute if score @s mg.trrg matches 1 run scoreboard players set $zm mg.st 3
execute if score @s mg.trrg matches 2 run scoreboard players set $zm mg.st 4
execute if score @s mg.trrg matches 3 run scoreboard players set $zm mg.st 5
execute if score @s mg.trrg matches 4 run scoreboard players set $zm mg.st 6
scoreboard players operation $xk mg.st *= $zm mg.st
scoreboard players operation $xk mg.st /= #2 mg.st
execute store result storage mg:terra s.xp int 1 run scoreboard players get $xk mg.st
function mg:terra/rpg/xpm with storage mg:terra s
scoreboard players operation $xk mg.st /= #2 mg.st
execute store result storage mg:terra s.xp int 1 run scoreboard players get $xk mg.st
execute at @s as @a[tag=mg.tvw,distance=0.1..24] run function mg:terra/rpg/xpm with storage mg:terra s
