# ⚡ Tron — préparation ($trm : 0 à pied, 1 moto)
scoreboard players set $trm mg.st 0
execute if score $game mg.st matches 85 run scoreboard players set $trm mg.st 1
function mg:tron/build
kill @e[tag=mg.trm]
kill @e[tag=mg.trp]
kill @e[tag=mg.trh]
scoreboard players set $tk mg.st 0
execute as @a[tag=mg.play,sort=random] run function mg:tron/assign
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 20000
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 81 20000
clear @a[tag=mg.play]
spreadplayers 0 20000 7 24 under 82 false @a[tag=mg.play]
execute as @a[tag=mg.play] at @s run tp @s ~ ~ ~ facing 0 81 20000
execute as @a[tag=mg.play] run attribute @s minecraft:jump_strength base set 0
execute if score $trm mg.st matches 1 as @a[tag=mg.play] at @s run function mg:tron/horse
