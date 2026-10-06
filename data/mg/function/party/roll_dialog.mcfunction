# Fenêtre du dé de @s, construite à la volée : étoiles, pièces et nombre de chaque objet (objets absents grisés)
execute store result storage mg:party rl.s int 1 run scoreboard players get @s mg.mpk
execute store result storage mg:party rl.c int 1 run scoreboard players get @s mg.mpm
execute store result storage mg:party rl.d int 1 run scoreboard players get @s mg.mid
execute store result storage mg:party rl.t int 1 run scoreboard players get @s mg.mit
execute store result storage mg:party rl.p int 1 run scoreboard players get @s mg.mip
data modify storage mg:party rl.k1 set value "aqua"
data modify storage mg:party rl.k2 set value "light_purple"
data modify storage mg:party rl.k3 set value "yellow"
data modify storage mg:party rl.x1 set value 21
data modify storage mg:party rl.x2 set value 22
data modify storage mg:party rl.x3 set value 23
execute unless score @s mg.mid matches 1.. run data modify storage mg:party rl.k1 set value "dark_gray"
execute unless score @s mg.mit matches 1.. run data modify storage mg:party rl.k2 set value "dark_gray"
execute unless score @s mg.mip matches 1.. run data modify storage mg:party rl.k3 set value "dark_gray"
execute unless score @s mg.mid matches 1.. run data modify storage mg:party rl.x1 set value 29
execute unless score @s mg.mit matches 1.. run data modify storage mg:party rl.x2 set value 29
execute unless score @s mg.mip matches 1.. run data modify storage mg:party rl.x3 set value 29
function mg:party/roll_dialog_m with storage mg:party rl
