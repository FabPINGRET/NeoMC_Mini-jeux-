# Boîte mystère : 1 Ray Gun, 2 Sniper, 2 Mitraillette, 2 Fusil à pompe, 1 Fusil (sur 8)
execute store result score $zx mg.st run random value 1..8
scoreboard players set $zgn mg.st 4
execute if score $zx mg.st matches 1 run scoreboard players set $zgn mg.st 6
execute if score $zx mg.st matches 2..3 run scoreboard players set $zgn mg.st 5
execute if score $zx mg.st matches 4..5 run scoreboard players set $zgn mg.st 2
execute if score $zx mg.st matches 6..7 run scoreboard players set $zgn mg.st 3
execute as @a[tag=mg.zbuyer] run function mg:zm2/give_gun
particle minecraft:witch 22.5 82.5 35773.5 0.4 0.4 0.4 0.1 30
playsound minecraft:block.chest.open master @a 22.5 82 35773.5 1 0.8
playsound minecraft:entity.player.levelup master @a 22.5 82 35773.5 0.6 1.6
execute if score $zgn mg.st matches 1 run title @a[tag=mg.zbuyer] actionbar [{"text":"❓ Boîte mystère : ","color":"light_purple"},{"text":"Pistolet M1911","color":"gray","bold":true}]
execute if score $zgn mg.st matches 2 run title @a[tag=mg.zbuyer] actionbar [{"text":"❓ Boîte mystère : ","color":"light_purple"},{"text":"Mitraillette MP5","color":"aqua","bold":true}]
execute if score $zgn mg.st matches 3 run title @a[tag=mg.zbuyer] actionbar [{"text":"❓ Boîte mystère : ","color":"light_purple"},{"text":"Fusil à pompe","color":"gold","bold":true}]
execute if score $zgn mg.st matches 4 run title @a[tag=mg.zbuyer] actionbar [{"text":"❓ Boîte mystère : ","color":"light_purple"},{"text":"Fusil M14","color":"yellow","bold":true}]
execute if score $zgn mg.st matches 5 run title @a[tag=mg.zbuyer] actionbar [{"text":"❓ Boîte mystère : ","color":"light_purple"},{"text":"Sniper","color":"light_purple","bold":true}]
execute if score $zgn mg.st matches 6 run title @a[tag=mg.zbuyer] actionbar [{"text":"❓ Boîte mystère : ","color":"light_purple"},{"text":"Ray Gun","color":"green","bold":true}]
execute if score $zgn mg.st matches 6 run tellraw @a[tag=mg.play] [{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a tiré le RAY GUN !","color":"green","bold":true}]
