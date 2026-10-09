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
tellraw @a[tag=mg.play] [{"text":"⛏ MINI UHC RUN : ","color":"gold","bold":true},{"text":"2 min 30 pour miner et t'équiper (minerais déjà cuits, minage rapide), PVP DÉSACTIVÉ. Ensuite PvP et la zone rétrécit. Pas de régénération : pommes d'or (8 lingots d'or + 1 pomme) ! Dernier en vie gagne.","color":"gray"}]
