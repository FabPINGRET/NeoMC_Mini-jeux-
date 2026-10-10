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
summon minecraft:cow 35 75 34765 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -25 74 34773 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow 14 81 34803 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow 31 80 34810 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow 13 81 34826 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -1 82 34784 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -25 74 34771 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -26 82 34817 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow 36 80 34778 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -4 78 34769 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow 16 81 34793 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:cow -13 77 34822 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 17 82 34780 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 7 76 34823 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken -8 81 34783 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken -6 82 34792 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken -28 76 34786 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 12 79 34811 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken -17 81 34808 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 25 75 34829 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 6 78 34816 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 26 76 34827 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken -35 78 34807 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:chicken 17 81 34821 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep -5 80 34773 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep 15 81 34833 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep -25 83 34814 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep 4 82 34796 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep 19 78 34766 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep 22 81 34801 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep 1 78 34768 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:sheep -22 74 34764 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig 8 81 34799 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig -28 76 34779 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig -3 77 34765 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig -33 75 34795 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig -18 78 34792 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
summon minecraft:pig -10 79 34787 {Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}
tellraw @a[tag=mg.play] [{"text":"⛏ MINI UHC RUN : ","color":"gold","bold":true},{"text":"2 min 30 pour miner et t'équiper (minerais déjà cuits, minage rapide, coffres, rochers à minerais, animaux), PVP DÉSACTIVÉ. Ensuite PvP et la zone rétrécit. Pas de régénération : pommes d'or (8 lingots d'or + 1 pomme) ! Dernier en vie gagne.","color":"gray"}]
