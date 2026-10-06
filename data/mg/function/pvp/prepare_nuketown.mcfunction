# Arène PvP — carte Nuketown (style Nuketown, centre 0 ~ 11500)
function mg:nuketown/build
scoreboard players reset @a mg.pk
kill @e[type=minecraft:item,x=-26,y=60,z=11481,dx=52,dy=40,dz=40]

# Perchoir spectateur au-dessus de la carte
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 11500

execute if score $pc mg.st matches 1 run scoreboard players set @a[tag=mg.play] mg.cl 1
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 81 11513
spreadplayers 0 11500 6 15 under 84 false @a[tag=mg.play]
execute if score $pc mg.st matches 1 as @a[tag=mg.play] run function mg:pvp2/menu
