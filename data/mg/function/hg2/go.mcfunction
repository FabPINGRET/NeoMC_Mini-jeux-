# Départ : 10 s figés sur les socles
scoreboard players set $hgt mg.st 0
scoreboard players set #-1 mg.st -1
scoreboard players set $zr mg.st 52
gamerule keep_inventory false
scoreboard players set @a mg.deaths 0
team join mg_green @a[tag=mg.play]
tellraw @a[tag=mg.play] [{"text":"🏹 MINI HUNGER GAMES : ","color":"gold","bold":true},{"text":"fouille les coffres (les meilleurs sont à la corne d'abondance au centre). PvP après 20 s, coffres remplis à 2 min 30, la zone rétrécit à partir de 3 min. Dernier en vie gagne !","color":"gray"}]
