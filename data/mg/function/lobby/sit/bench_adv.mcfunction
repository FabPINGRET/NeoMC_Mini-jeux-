# @s : a interagi avec une zone de banc (advancement mg:lobby_bench) ; mg.lbc le distingue des autres joueurs
advancement revoke @s only mg:lobby_bench
tag @s add mg.lbc
execute as @e[type=minecraft:interaction,tag=mg.bench,distance=..8] if data entity @s interaction run function mg:lobby/sit/bench_hit
tag @s remove mg.lbc
