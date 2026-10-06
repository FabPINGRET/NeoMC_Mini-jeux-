execute if score $sg mg.st matches 1 run return run function mg:sumo/prepare_xl
# Sumo — préparation (centre 0 ~ 4900) : rayon selon le nombre de joueurs (1-4 → 7, 5-8 → 9, 9+ → 11)
scoreboard players set $sr2 mg.st 10
execute if score $n0 mg.st matches ..8 run scoreboard players set $sr2 mg.st 8
execute if score $n0 mg.st matches ..4 run scoreboard players set $sr2 mg.st 6
execute if score $sr2 mg.st matches 10 run function mg:sumo/disk_l
execute if score $sr2 mg.st matches 8 run function mg:sumo/disk_m
execute if score $sr2 mg.st matches 6 run function mg:sumo/disk_s
kill @e[type=minecraft:item,x=-30,y=50,z=4870,dx=60,dy=60,dz=60]

# Chute sous la plateforme = une vie perdue
scoreboard players set $yd mg.st 72

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 92
scoreboard players set $pz mg.st 4900

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 92 4900
scoreboard players set @a[tag=mg.play] mg.lv 3
execute if score $sr2 mg.st matches 10 run spreadplayers 0 4900 3 9 under 85 false @a[tag=mg.play]
execute if score $sr2 mg.st matches 8 run spreadplayers 0 4900 3 7 under 85 false @a[tag=mg.play]
execute if score $sr2 mg.st matches 6 run spreadplayers 0 4900 2 5 under 85 false @a[tag=mg.play]
