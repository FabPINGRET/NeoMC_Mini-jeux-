# Départ : survie, pas de régénération naturelle, inventaire lâché à la mort
scoreboard players set $uht mg.st 0
scoreboard players set #-1 mg.st -1
scoreboard players set $zr mg.st 42
gamerule natural_health_regeneration false
gamerule keep_inventory false
gamemode survival @a[tag=mg.play]
team join mg_green @a[tag=mg.play]
give @a[tag=mg.play] minecraft:iron_pickaxe[enchantments={efficiency:5},unbreakable={}]
give @a[tag=mg.play] minecraft:iron_axe[enchantments={efficiency:5},unbreakable={}]
give @a[tag=mg.play] minecraft:iron_shovel[enchantments={efficiency:5},unbreakable={}]
give @a[tag=mg.play] minecraft:crafting_table
give @a[tag=mg.play] minecraft:bread 10
effect give @a[tag=mg.play] minecraft:haste infinite 2 true
scoreboard players reset @a mg.uoi
scoreboard players reset @a mg.uog
scoreboard players reset @a mg.uod
scoreboard players reset @a mg.uor
scoreboard players reset @a mg.uol
effect give @a[tag=mg.play] minecraft:instant_health 1 4 true
scoreboard players set @a mg.deaths 0
summon minecraft:cow 35 82 34365 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -25 75 34373 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow 14 79 34403 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow 31 80 34410 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow 13 76 34426 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -1 80 34384 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -25 75 34371 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -26 80 34417 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow 36 79 34378 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -4 78 34369 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow 16 77 34393 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -13 78 34422 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 17 80 34380 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 7 76 34423 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken -8 78 34383 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken -6 81 34392 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken -28 78 34386 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 12 81 34411 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken -17 80 34408 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 25 78 34429 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 6 80 34416 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 26 79 34427 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken -35 80 34407 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 17 79 34421 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep -5 78 34373 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep 15 75 34433 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep -25 79 34414 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep 4 80 34396 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep 19 78 34366 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep 22 80 34401 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep 1 79 34368 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep -22 74 34364 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig 8 79 34399 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig -28 76 34379 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig -3 77 34365 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig -33 80 34395 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig -18 79 34392 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig -10 80 34387 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
tellraw @a[tag=mg.play] [{"text":"⛏ MINI UHC RUN : ","color":"gold","bold":true},{"text":"2 min 30 pour miner et t'équiper (minerais déjà cuits, minage rapide, coffres, rochers à minerais, animaux), PVP DÉSACTIVÉ. Ensuite PvP et la zone rétrécit. Pas de régénération : pommes d'or (8 lingots d'or + 1 pomme) ! Dernier en vie gagne.","color":"gray"}]
