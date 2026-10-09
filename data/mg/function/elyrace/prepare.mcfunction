# Course d'élytres : préparation (parcours $xc : 0 = au hasard parmi les parcours construits)
execute if score $xc mg.st matches 0 run function mg:elyrace/pick
# parcours pas construit (ou pas encore écrit) : on n'envoie personne dedans, partie annulée
execute if score $xc mg.st matches 0 run return run function mg:elyrace/not_built
execute if score $xc mg.st matches 1 unless data storage mg:elyrace v2 run return run function mg:elyrace/not_built
execute if score $xc mg.st matches 2 unless data storage mg:elyrace c2v2 run return run function mg:elyrace/not_built
# restes d'une partie précédente
tag @a remove mg.xw1
tag @a remove mg.xtp
# les contre-la-montre solo en cours s'arrêtent : le groupe prend la plateforme, le portillon et le chrono $xt
tellraw @a[tag=mg.xso] [{"text":"🪽 Une course de groupe démarre : ton contre-la-montre solo est arrêté.","color":"red"}]
execute as @a[tag=mg.xso] run function mg:elyrace/solo/stop
execute if score $xc mg.st matches 1 run function mg:elyrace/c1/setup
execute if score $xc mg.st matches 2 run function mg:elyrace/c2/setup
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
# parcours de chaque participant (le répartiteur par joueur respawn / hud / place_tp le lit, comme le solo) : avant place_one
scoreboard players operation @a[tag=mg.play] mg.xcr = $xc mg.st
scoreboard players set $ri mg.st 0
execute as @a[tag=mg.play] run function mg:elyrace/equip
execute as @a[tag=mg.play] run function mg:elyrace/place_one
# tableau des anneaux de la course de groupe
scoreboard objectives setdisplay sidebar mg.xa
