# Arène PvP — préparation
execute if score $pm mg.st matches 1 run return run function mg:pvp/prepare_dust
execute if score $pm mg.st matches 2 run return run function mg:pvp/prepare_mirage
execute if score $pm mg.st matches 3 run return run function mg:pvp/prepare_nuketown
function mg:pvp/build
scoreboard players reset @a mg.pk
kill @e[type=minecraft:item,x=-14,y=60,z=886,dx=28,dy=10,dz=28]

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 80
scoreboard players set $pz mg.st 900

execute if score $pc mg.st matches 1 run scoreboard players set @a[tag=mg.play] mg.cl 1
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 80 900
spreadplayers 0 900 5 12 under 66 false @a[tag=mg.play]
execute if score $pc mg.st matches 1 as @a[tag=mg.play] run function mg:pvp2/menu
