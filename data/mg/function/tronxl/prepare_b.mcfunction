# XXL : préparation (zone chargée par tronxl/prepare)
execute unless score $state mg.st matches 1 run return 0
execute unless loaded -102 80 33898 run return run schedule function mg:tronxl/prepare_b 20t
execute unless loaded 102 80 34102 run return run schedule function mg:tronxl/prepare_b 20t
execute unless loaded 0 80 34000 run return run schedule function mg:tronxl/prepare_b 20t
# ⚡ Tron — préparation ($trm : 0 à pied, 1 moto)
scoreboard players set $trm mg.st 0
execute if score $game mg.st matches 201 run scoreboard players set $trm mg.st 1
function mg:tronxl/build
kill @e[tag=mg.trm]
kill @e[tag=mg.trp]
kill @e[tag=mg.trh]
scoreboard players set $tk mg.st 0
execute as @a[tag=mg.play,sort=random] run function mg:tronxl/assign
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 90
scoreboard players set $pz mg.st 34000
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 81 34000
clear @a[tag=mg.play]
spreadplayers 0 34000 10 92 under 82 false @a[tag=mg.play]
execute as @a[tag=mg.play] at @s run tp @s ~ ~ ~ facing 0 81 34000
execute as @a[tag=mg.play] run attribute @s minecraft:jump_strength base set 0
execute if score $trm mg.st matches 1 as @a[tag=mg.play] at @s run function mg:tronxl/horse
