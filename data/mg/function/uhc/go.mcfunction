# Départ : survie, pas de régénération naturelle, inventaire lâché à la mort
scoreboard players set $uht mg.st 0
scoreboard players set #-1 mg.st -1
scoreboard players set $zr mg.st 42
gamerule natural_health_regeneration false
gamerule keep_inventory false
gamemode survival @a[tag=mg.play]
team join mg_green @a[tag=mg.play]
give @a[tag=mg.play] minecraft:stone_pickaxe[enchantments={efficiency:3},unbreakable={}]
give @a[tag=mg.play] minecraft:stone_axe[enchantments={efficiency:3},unbreakable={}]
give @a[tag=mg.play] minecraft:stone_shovel[enchantments={efficiency:3},unbreakable={}]
give @a[tag=mg.play] minecraft:crafting_table
give @a[tag=mg.play] minecraft:bread 10
effect give @a[tag=mg.play] minecraft:haste infinite 1 true
effect give @a[tag=mg.play] minecraft:instant_health 1 4 true
scoreboard players set @a mg.deaths 0
summon minecraft:cow 13 77 22426 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -1 77 22384 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -25 77 22371 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -26 75 22417 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow 36 77 22378 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -4 76 22369 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow 16 81 22393 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -13 77 22422 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow 17 77 22380 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow 7 78 22423 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -8 77 22383 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -6 79 22392 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken -28 78 22386 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 12 75 22411 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken -17 76 22408 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 25 77 22429 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 6 77 22416 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 26 77 22427 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken -35 73 22407 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 17 77 22421 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken -5 77 22373 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 15 75 22433 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken -25 74 22414 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 4 82 22396 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep 19 76 22366 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep 22 80 22401 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep 1 76 22368 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep -22 77 22364 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep 8 81 22399 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep -28 76 22379 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep -3 77 22365 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep -33 78 22395 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig -18 77 22392 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig -10 79 22387 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig -29 77 22374 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig 6 77 22405 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig -3 77 22388 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig -36 77 22393 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
tellraw @a[tag=mg.play] [{"text":"⛏ MINI UHC RUN : ","color":"gold","bold":true},{"text":"2 min 30 pour miner et t'équiper (minerais déjà cuits, minage rapide, coffres, rochers à minerais, animaux), PVP DÉSACTIVÉ. Ensuite PvP et la zone rétrécit. Pas de régénération : pommes d'or (8 lingots d'or + 1 pomme) ! Dernier en vie gagne.","color":"gray"}]
