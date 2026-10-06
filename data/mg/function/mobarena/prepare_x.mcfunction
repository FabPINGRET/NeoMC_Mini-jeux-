# Mob Arena — préparation des thèmes à 20 vagues (6 cathédrale, 7 laboratoire, 8 temple, 9 forge, 10 vaisseau)
scoreboard players set $wmax mg.st 20
scoreboard players set $bt mg.st 0
scoreboard players set $lvl mg.st 0
scoreboard players set $bmax mg.st 1
scoreboard players set $k12 mg.st 12
scoreboard players set $k15 mg.st 15
scoreboard players set $k20 mg.st 20
scoreboard players set $k80 mg.st 80
scoreboard players set $k100 mg.st 100
scoreboard players set $k200 mg.st 200
scoreboard players set $k400 mg.st 400
kill @e[tag=mg.mob]
kill @e[tag=mg.alembic]
kill @e[tag=mg.cloud]
kill @e[tag=mg.meteor]
bossbar set mg:boss visible false
execute if score $mt mg.st matches 6 run forceload add -24 9070 24 9130
execute if score $mt mg.st matches 7 run forceload add -24 9470 24 9530
execute if score $mt mg.st matches 8 run forceload add -32 9868 32 9932
execute if score $mt mg.st matches 9 run forceload add -40 10260 40 10340
execute if score $mt mg.st matches 10 run forceload add -32 10668 32 10732
execute if score $mt mg.st matches 6 run data modify storage mg:mw p set value "cathedral"
execute if score $mt mg.st matches 6 run scoreboard players set $pz mg.st 9100
execute if score $mt mg.st matches 7 run data modify storage mg:mw p set value "lab"
execute if score $mt mg.st matches 7 run scoreboard players set $pz mg.st 9500
execute if score $mt mg.st matches 8 run data modify storage mg:mw p set value "temple"
execute if score $mt mg.st matches 8 run scoreboard players set $pz mg.st 9900
execute if score $mt mg.st matches 9 run data modify storage mg:mw p set value "forge"
execute if score $mt mg.st matches 9 run scoreboard players set $pz mg.st 10300
execute if score $mt mg.st matches 10 run data modify storage mg:mw p set value "ship"
execute if score $mt mg.st matches 10 run scoreboard players set $pz mg.st 10700
kill @e[type=minecraft:item]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 82
scoreboard players set $wv mg.st 0
scoreboard players set $wt mg.st 100
gamemode adventure @a[tag=mg.play]
execute if score $mt mg.st matches 6 as @a[tag=mg.play] run spawnpoint @s 0 65 9086
execute if score $mt mg.st matches 7 as @a[tag=mg.play] run spawnpoint @s 0 65 9488
execute if score $mt mg.st matches 8 as @a[tag=mg.play] run spawnpoint @s 0 68 9880
execute if score $mt mg.st matches 9 as @a[tag=mg.play] run spawnpoint @s 0 66 10290
execute if score $mt mg.st matches 10 as @a[tag=mg.play] run spawnpoint @s 0 65 10685

# Classes : tout le monde repart Guerrier, puis choisit
scoreboard players set @a[tag=mg.play] mg.cl 1
execute as @a[tag=mg.play] run function mg:mobarena/class_menu
scoreboard players set $gl mg.st 0
scoreboard players reset @a mg.us

# Construction de l'arène + placement des joueurs : 0,75 s plus tard (le temps que les chunks soient bien chargés)
schedule function mg:mobarena/xbuild 15t
