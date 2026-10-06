# Arène PvP — carte Poussière (style Dust, centre 0 ~ 11100)
function mg:dust/build
scoreboard players reset @a mg.pk
kill @e[type=minecraft:item,x=-24,y=60,z=11076,dx=48,dy=40,dz=48]

# Perchoir spectateur au-dessus de la carte
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 11100

execute if score $pc mg.st matches 1 run scoreboard players set @a[tag=mg.play] mg.cl 1
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 81 11116
spreadplayers 0 11100 6 18 under 84 false @a[tag=mg.play]
execute if score $pc mg.st matches 1 as @a[tag=mg.play] run function mg:pvp2/menu
