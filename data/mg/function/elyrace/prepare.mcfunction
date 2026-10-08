# Course d'élytres : préparation (parcours 1 : Canyon du Couchant)
# parcours pas (entièrement) construit : on n'envoie personne dedans, partie annulée
execute unless data storage mg:elyrace v1 run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d'élytres : le parcours n'est pas (entièrement) construit, lance /function mg:elyrace/build","color":"red"}]
execute unless data storage mg:elyrace v1 run tellraw @a[tag=mg.play] [{"text":"🪽 Le parcours n'est pas encore construit : partie annulée.","color":"red"}]
execute unless data storage mg:elyrace v1 run return run function mg:core/draw
# restes d'une partie précédente
tag @a remove mg.xw1
tag @a remove mg.xtp
function mg:elyrace/fl_add
function mg:elyrace/gate_on
# perchoir des spectateurs (éliminés / reconnectés)
scoreboard players set $px mg.st 24
scoreboard players set $py mg.st 270
scoreboard players set $pz mg.st 27000
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
execute as @a[tag=mg.play] run spawnpoint @s 24 251 27000
scoreboard objectives setdisplay sidebar mg.xa
