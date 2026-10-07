# Carapace (@s, à sa position) : avance, rebondit ou éclate contre un mur, touche un kart
scoreboard players remove @s mg.t 1
execute if score @s mg.t matches ..0 run return run kill @s
scoreboard players remove @s[scores={mg.kbo=1..}] mg.kbo 1
execute if entity @s[tag=mg.kred] unless score @s mg.kdd matches -1 run function mg:kart/shell_aim
execute positioned ^ ^ ^1.3 unless block ~ ~ ~ #mg:kart_pass run return run function mg:kart/shell_wall
tp @s ^ ^ ^1.3
particle minecraft:crit ~ ~0.2 ~ 0.1 0.1 0.1 0 1
execute if score @s mg.kbo matches 1.. run return 0
tag @s add mg.kcur
execute as @a[tag=mg.play,distance=..1.7,limit=1,sort=nearest] run function mg:kart/shell_hit
tag @s remove mg.kcur
