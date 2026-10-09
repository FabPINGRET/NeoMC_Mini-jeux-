# ⛳ Golf : nettoyage (entités, clubs, équipe, zone chargée)
kill @e[tag=mg.gfb]
kill @e[tag=mg.gff]
kill @e[tag=mg.gftg]
clear @a minecraft:warped_fungus_on_a_stick[custom_data~{golf:1}]
clear @a minecraft:warped_fungus_on_a_stick[custom_data~{golf:2}]
team leave @a[team=mg_golf]
effect clear @a[tag=mg.play] minecraft:resistance
scoreboard players reset * mg.gfs
scoreboard players reset * mg.gfd
scoreboard players reset * mg.gfi
tag @a remove mg.gfme
scoreboard players set $gfok mg.st 0
schedule clear mg:golf/wait
schedule clear mg:golf/build_1
schedule clear mg:golf/build_2
schedule clear mg:golf/build_3
schedule clear mg:golf/build_4
schedule clear mg:golf/build_5
schedule clear mg:golf/build_6
schedule clear mg:golf/build_7
schedule clear mg:golf/build_8
schedule clear mg:golf/build_9
schedule clear mg:golf/build_10
forceload remove 196 34496 404 34704
