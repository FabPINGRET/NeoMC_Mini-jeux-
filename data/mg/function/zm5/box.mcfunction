# Boîte mystère : Ray Gun 1, Sniper 2, Mitraillette MP5 2, Fusil à pompe 2, Fusil M14 2, Mitrailleuse RPK 2, Revolver Python 2, Lance-roquettes 2, Grenades singe 3, Batte cloutée 2 (sur 20)
execute store result score $zx mg.st run random value 1..20
execute if score $zx mg.st matches 1..1 run scoreboard players set $zgn mg.st 6
execute if score $zx mg.st matches 2..3 run scoreboard players set $zgn mg.st 5
execute if score $zx mg.st matches 4..5 run scoreboard players set $zgn mg.st 2
execute if score $zx mg.st matches 6..7 run scoreboard players set $zgn mg.st 3
execute if score $zx mg.st matches 8..9 run scoreboard players set $zgn mg.st 4
execute if score $zx mg.st matches 10..11 run scoreboard players set $zgn mg.st 7
execute if score $zx mg.st matches 12..13 run scoreboard players set $zgn mg.st 8
execute if score $zx mg.st matches 14..15 run scoreboard players set $zgn mg.st 10
execute if score $zx mg.st matches 16..18 run scoreboard players set $zgn mg.st 11
execute if score $zx mg.st matches 19..20 run scoreboard players set $zgn mg.st 12
execute as @a[tag=mg.zbuyer] run function mg:zm5/give_gun
particle minecraft:witch 0.5 82.5 39378.5 0.4 0.4 0.4 0.1 30
playsound minecraft:block.chest.open master @a 0.5 82 39378.5 1 0.8
playsound minecraft:entity.player.levelup master @a 0.5 82 39378.5 0.6 1.6
execute if score $zgn mg.st matches 1 run title @a[tag=mg.zbuyer] actionbar [{"text":"❓ Boîte mystère : ","color":"light_purple"},{"text":"Pistolet M1911","color":"gray","bold":true}]
execute if score $zgn mg.st matches 2 run title @a[tag=mg.zbuyer] actionbar [{"text":"❓ Boîte mystère : ","color":"light_purple"},{"text":"Mitraillette MP5","color":"aqua","bold":true}]
execute if score $zgn mg.st matches 3 run title @a[tag=mg.zbuyer] actionbar [{"text":"❓ Boîte mystère : ","color":"light_purple"},{"text":"Fusil à pompe","color":"gold","bold":true}]
execute if score $zgn mg.st matches 4 run title @a[tag=mg.zbuyer] actionbar [{"text":"❓ Boîte mystère : ","color":"light_purple"},{"text":"Fusil M14","color":"yellow","bold":true}]
execute if score $zgn mg.st matches 5 run title @a[tag=mg.zbuyer] actionbar [{"text":"❓ Boîte mystère : ","color":"light_purple"},{"text":"Sniper","color":"light_purple","bold":true}]
execute if score $zgn mg.st matches 6 run title @a[tag=mg.zbuyer] actionbar [{"text":"❓ Boîte mystère : ","color":"light_purple"},{"text":"Ray Gun","color":"green","bold":true}]
execute if score $zgn mg.st matches 7 run title @a[tag=mg.zbuyer] actionbar [{"text":"❓ Boîte mystère : ","color":"light_purple"},{"text":"Mitrailleuse RPK","color":"red","bold":true}]
execute if score $zgn mg.st matches 8 run title @a[tag=mg.zbuyer] actionbar [{"text":"❓ Boîte mystère : ","color":"light_purple"},{"text":"Revolver Python","color":"dark_aqua","bold":true}]
execute if score $zgn mg.st matches 10 run title @a[tag=mg.zbuyer] actionbar [{"text":"❓ Boîte mystère : ","color":"light_purple"},{"text":"Lance-roquettes","color":"red","bold":true}]
execute if score $zgn mg.st matches 11 run title @a[tag=mg.zbuyer] actionbar [{"text":"❓ Boîte mystère : ","color":"light_purple"},{"text":"Grenades singe","color":"gold","bold":true}]
execute if score $zgn mg.st matches 12 run title @a[tag=mg.zbuyer] actionbar [{"text":"❓ Boîte mystère : ","color":"light_purple"},{"text":"Batte cloutée","color":"gold","bold":true}]
execute if score $zgn mg.st matches 6 run tellraw @a[tag=mg.play] [{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a tiré le RAY GUN !","color":"green","bold":true}]
