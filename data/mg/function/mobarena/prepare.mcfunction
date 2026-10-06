# Mob Arena — préparation
execute if score $mt mg.st matches 6..10 run return run function mg:mobarena/prepare_x
scoreboard players set $wmax mg.st 10
function mg:mobarena/build
function mg:mobarena/clean

# Thème : $mt 0 classique, 1 nether, 2 end, 3 ultra hard, 4 volant, 5 araignée
data modify storage mg:mw p set value "waves"
execute if score $mt mg.st matches 1 run data modify storage mg:mw p set value "nether"
execute if score $mt mg.st matches 2 run data modify storage mg:mw p set value "end"
execute if score $mt mg.st matches 3 run data modify storage mg:mw p set value "ultra"
execute if score $mt mg.st matches 4 run data modify storage mg:mw p set value "volant"
execute if score $mt mg.st matches 5 run data modify storage mg:mw p set value "spider"
execute if score $mt mg.st matches 1 run function mg:mobarena/skin_nether
execute if score $mt mg.st matches 2 run function mg:mobarena/skin_end
execute if score $mt mg.st matches 3 run function mg:mobarena/skin_ultra
execute if score $mt mg.st matches 4 run function mg:mobarena/skin_volant
execute if score $mt mg.st matches 5 run function mg:mobarena/skin_spider
kill @e[tag=mg.mob]
kill @e[type=minecraft:item,x=-16,y=60,z=1784,dx=32,dy=15,dz=32]

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 80
scoreboard players set $pz mg.st 1800
scoreboard players set $wv mg.st 0
scoreboard players set $wt mg.st 100

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 80 1800
spreadplayers 0 1800 2 8 under 66 false @a[tag=mg.play]

# Classes : tout le monde repart Guerrier, puis choisit
scoreboard players set @a[tag=mg.play] mg.cl 1
execute as @a[tag=mg.play] run function mg:mobarena/class_menu
scoreboard players set $gl mg.st 0
scoreboard players reset @a mg.us
