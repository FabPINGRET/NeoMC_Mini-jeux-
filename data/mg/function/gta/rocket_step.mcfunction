# Un pas de la roquette (@s, à sa position, orientée)
execute unless block ^ ^ ^0.7 #mg:ray_pass positioned ^ ^ ^0.4 run return run function mg:gta/rocket_boom
scoreboard players operation $bid mg.st = @s mg.bid
execute positioned ^ ^ ^0.7 positioned ~ ~-0.9 ~ as @e[tag=mg.gtg,distance=..1.3] unless score @s mg.bid = $bid mg.st run tag @s add mg.grhit
execute if entity @e[tag=mg.grhit] positioned ^ ^ ^0.7 run return run function mg:gta/rocket_boom
tp @s ^ ^ ^0.7
