# @s a vaincu un monstre : XP (et la moitié aux joueurs à 24 blocs)
$function mg:ombre/xp {n:$(n)}
$scoreboard players set $xk mg.st $(n)
scoreboard players operation $xk mg.st /= #2 mg.st
execute store result storage mg:ombre s.n int 1 run scoreboard players get $xk mg.st
execute at @s as @a[tag=mg.olw,distance=0.1..24] run function mg:ombre/xpm with storage mg:ombre s
