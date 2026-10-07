# Splegg — préparation (centre 0 ~ 4200) ; $sg = 1 → version XXL
execute if score $sg mg.st matches 1 run return run function mg:splegg/prepare_xxl
# 3 étages (y 80 / 74 / 68) : élimination sous le dernier
scoreboard players set $yd mg.st 62
# Taille du plateau selon les joueurs : 1-2 → 19x19, 3-4 → 25x25, 5-7 → 31x31, 8+ → 37x37
scoreboard players set $sr2 mg.st 18
execute if score $n0 mg.st matches ..7 run scoreboard players set $sr2 mg.st 15
execute if score $n0 mg.st matches ..4 run scoreboard players set $sr2 mg.st 12
execute if score $n0 mg.st matches ..2 run scoreboard players set $sr2 mg.st 9
execute if score $sr2 mg.st matches 18 run function mg:splegg/floor_xl
execute if score $sr2 mg.st matches 15 run function mg:splegg/floor_l
execute if score $sr2 mg.st matches 12 run function mg:splegg/floor_m
execute if score $sr2 mg.st matches 9 run function mg:splegg/floor_s

kill @e[distance=0..,type=minecraft:egg]
kill @e[type=minecraft:chicken,x=-40,y=60,z=4160,dx=80,dy=60,dz=80]
kill @e[type=minecraft:item,x=-40,y=55,z=4160,dx=80,dy=60,dz=80]

# Perchoir spectateur + point de réapparition
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 92
scoreboard players set $pz mg.st 4200

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 92 4200
# Dispersion sur le plateau (marge de 2 blocs avec le bord) : sx = rayon - 2
execute if score $sr2 mg.st matches 18 run spreadplayers 0 4200 3 16 under 85 false @a[tag=mg.play]
execute if score $sr2 mg.st matches 15 run spreadplayers 0 4200 3 13 under 85 false @a[tag=mg.play]
execute if score $sr2 mg.st matches 12 run spreadplayers 0 4200 3 10 under 85 false @a[tag=mg.play]
execute if score $sr2 mg.st matches 9 run spreadplayers 0 4200 3 7 under 85 false @a[tag=mg.play]
