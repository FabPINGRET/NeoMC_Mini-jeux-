# Quakecraft — préparation (carte $qm : 0 néon, 1 volcan XL, 2 jungle XL, 3 désert, 4 glacier mini)
scoreboard players set $qcd mg.st 22
execute if score $ar mg.st matches 1.. run return run function mg:var/mode/quake_prepare
execute if score $qm mg.st matches 0 run function mg:quake/build
execute if score $qm mg.st matches 0 run scoreboard players set $qg mg.st 25
execute if score $qm mg.st matches 0 run scoreboard players set $qt mg.st 9600
execute if score $qm mg.st matches 0 run scoreboard players set $pz mg.st 7300
execute if score $qm mg.st matches 1 run function mg:quake/build_1
execute if score $qm mg.st matches 1 run scoreboard players set $qg mg.st 30
execute if score $qm mg.st matches 1 run scoreboard players set $qt mg.st 12000
execute if score $qm mg.st matches 1 run scoreboard players set $pz mg.st 7600
execute if score $qm mg.st matches 2 run function mg:quake/build_2
execute if score $qm mg.st matches 2 run scoreboard players set $qg mg.st 30
execute if score $qm mg.st matches 2 run scoreboard players set $qt mg.st 12000
execute if score $qm mg.st matches 2 run scoreboard players set $pz mg.st 7900
execute if score $qm mg.st matches 3 run function mg:quake/build_3
execute if score $qm mg.st matches 3 run scoreboard players set $qg mg.st 25
execute if score $qm mg.st matches 3 run scoreboard players set $qt mg.st 9600
execute if score $qm mg.st matches 3 run scoreboard players set $pz mg.st 8200
execute if score $qm mg.st matches 4 run function mg:quake/build_4
execute if score $qm mg.st matches 4 run scoreboard players set $qg mg.st 20
execute if score $qm mg.st matches 4 run scoreboard players set $qt mg.st 7200
execute if score $qm mg.st matches 4 run scoreboard players set $pz mg.st 8500
execute if score $qm mg.st matches 5 run function mg:dust/build
execute if score $qm mg.st matches 5 run scoreboard players set $qg mg.st 20
execute if score $qm mg.st matches 5 run scoreboard players set $qt mg.st 7200
execute if score $qm mg.st matches 5 run scoreboard players set $pz mg.st 11100
execute if score $qm mg.st matches 6 run function mg:mirage/build
execute if score $qm mg.st matches 6 run scoreboard players set $qg mg.st 20
execute if score $qm mg.st matches 6 run scoreboard players set $qt mg.st 7200
execute if score $qm mg.st matches 6 run scoreboard players set $pz mg.st 11300
execute if score $qm mg.st matches 7 run function mg:nuketown/build
execute if score $qm mg.st matches 7 run scoreboard players set $qg mg.st 20
execute if score $qm mg.st matches 7 run scoreboard players set $qt mg.st 7200
execute if score $qm mg.st matches 7 run scoreboard players set $pz mg.st 11500
kill @e[distance=0..,type=minecraft:item]
scoreboard players reset @a mg.qs
tag @a remove mg.prot
tag @a remove mg.qdd
tag @a remove mg.qsh
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
gamemode adventure @a[tag=mg.play]
execute if score $qm mg.st matches 0 run spawnpoint @a[tag=mg.play] 13 81 7313
execute if score $qm mg.st matches 1 run spawnpoint @a[tag=mg.play] 28 81 7628
execute if score $qm mg.st matches 2 run spawnpoint @a[tag=mg.play] 28 81 7928
execute if score $qm mg.st matches 3 run spawnpoint @a[tag=mg.play] 13 81 8213
execute if score $qm mg.st matches 4 run spawnpoint @a[tag=mg.play] 7 81 8507
execute if score $qm mg.st matches 5 run spawnpoint @a[tag=mg.play] 0 81 11116
execute if score $qm mg.st matches 6 run spawnpoint @a[tag=mg.play] 0 81 11316
execute if score $qm mg.st matches 7 run spawnpoint @a[tag=mg.play] 0 81 11513
scoreboard players set @a[tag=mg.play] mg.qk 0
scoreboard players set @a[tag=mg.play] mg.cd 0
function mg:quake/spread_all
