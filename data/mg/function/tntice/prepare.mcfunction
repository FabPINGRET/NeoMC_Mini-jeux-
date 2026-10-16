# ✷ TNT Run glace — préparation
function mg:tntice/build
kill @e[type=minecraft:item,x=-19,y=50,z=41681,dx=38,dy=50,dz=38]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 92
scoreboard players set $pz mg.st 41700
scoreboard players set $dk mg.st 9
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 92 41700
execute if score $game mg.st matches 244 run spreadplayers 0 41700 4 13 under 86 false @a[tag=mg.play]
execute if score $game mg.st matches 245 run spreadplayers 0 41700 4 16 under 86 false @a[tag=mg.play]
