# TNT Tag — préparation : carte $ttm (0 classique centre 0 ~ 6100, 1 Collines, 2 Canyon, 3 Village perché)
tag @a remove mg.bomb
execute if score $ar mg.st matches 1.. run return run function mg:var/mode/tnttag_prepare
execute unless score $ttm mg.st matches 0..3 run scoreboard players set $ttm mg.st 0
execute if score $ttm mg.st matches 1 run return run function mg:tnttag/map/setup_1
execute if score $ttm mg.st matches 2 run return run function mg:tnttag/map/setup_2
execute if score $ttm mg.st matches 3 run return run function mg:tnttag/map/setup_3
function mg:tnttag/build
kill @e[type=minecraft:item,x=-25,y=70,z=6075,dx=50,dy=30,dz=50]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 6100
# Éliminé sous y 71
scoreboard players set $tty mg.st 71
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 81 6100
spreadplayers 0 6100 4 13 under 90 false @a[tag=mg.play]
