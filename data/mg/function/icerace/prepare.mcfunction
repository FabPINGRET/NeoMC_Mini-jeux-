# Course de bateaux sur glace — préparation (circuit centré 0 ~ 13200)
function mg:icerace/build
kill @e[tag=mg.ib]
kill @e[distance=0..,type=minecraft:item]
scoreboard players set $px mg.st -10
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 13200

gamemode adventure @a[tag=mg.play]
scoreboard players set @a[tag=mg.play] mg.cp 0
scoreboard players set @a[tag=mg.play] mg.lp 0
scoreboard players set @a[tag=mg.play] mg.rp 0
scoreboard players set $ri mg.st 0
execute as @a[tag=mg.play] run function mg:icerace/place_one
execute as @a[tag=mg.play] run spawnpoint @s -20 81 13229
