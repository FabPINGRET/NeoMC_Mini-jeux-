# Course d'élytres : préparation (parcours $xc : 0 = au hasard parmi les parcours construits)
execute if score $xc mg.st matches 0 run function mg:elyrace/pick
# parcours pas construit (ou pas encore écrit) : on n'envoie personne dedans, partie annulée
execute if score $xc mg.st matches 0 run return run function mg:elyrace/not_built
execute if score $xc mg.st matches 1 unless data storage mg:elyrace v1 run return run function mg:elyrace/not_built
execute if score $xc mg.st matches 2 run return run function mg:elyrace/not_available
# restes d'une partie précédente
tag @a remove mg.xw1
tag @a remove mg.xtp
execute if score $xc mg.st matches 1 run function mg:elyrace/c1/setup
gamemode adventure @a[tag=mg.play]
clear @a[tag=mg.play]
scoreboard players set @a[tag=mg.play] mg.deaths 0
scoreboard players set @a[tag=mg.play] mg.xa 0
scoreboard players set @a[tag=mg.play] mg.xo 0
scoreboard players set @a[tag=mg.play] mg.xc 0
scoreboard players set @a[tag=mg.play] mg.xh 3
scoreboard players set @a[tag=mg.play] mg.xp 0
scoreboard players set @a[tag=mg.play] mg.xx 0
scoreboard players set @a[tag=mg.play] mg.xg 0
scoreboard players set @a[tag=mg.play] mg.xn 0
scoreboard players set @a[tag=mg.play] mg.xl 0
scoreboard players set @a[tag=mg.play] mg.xk 0
scoreboard players set @a[tag=mg.play] mg.xf 0
scoreboard players set @a[tag=mg.play] mg.xb1 0
scoreboard players set @a[tag=mg.play] mg.xb2 0
scoreboard players set @a[tag=mg.play] mg.xb3 0
scoreboard players set $xt mg.st 0
scoreboard players set $xf mg.st 0
scoreboard players set $xw mg.st 0
scoreboard players set $xe mg.st 0
scoreboard players set #k10 mg.st 10
scoreboard players set #k20 mg.st 20
scoreboard players set #k100 mg.st 100
scoreboard players set #krel mg.st 30
scoreboard players set $ri mg.st 0
execute as @a[tag=mg.play] run function mg:elyrace/equip
execute as @a[tag=mg.play] run function mg:elyrace/place_one
scoreboard objectives setdisplay sidebar mg.xa
