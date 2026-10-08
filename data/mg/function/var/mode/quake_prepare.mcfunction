# Quakecraft sur une autre carte ($ar) — appelé par quake/prepare. Généré.
kill @e[distance=0..,type=minecraft:item]
scoreboard players reset @a mg.qs
tag @a remove mg.prot
tag @a remove mg.qdd
tag @a remove mg.qsh
execute if score $ar mg.st matches 1 run scoreboard players set $qg mg.st 25
execute if score $ar mg.st matches 1 run scoreboard players set $qt mg.st 9600
execute if score $ar mg.st matches 2 run scoreboard players set $qg mg.st 25
execute if score $ar mg.st matches 2 run scoreboard players set $qt mg.st 9600
execute if score $ar mg.st matches 3 run scoreboard players set $qg mg.st 25
execute if score $ar mg.st matches 3 run scoreboard players set $qt mg.st 9600
execute if score $ar mg.st matches 4 run scoreboard players set $qg mg.st 20
execute if score $ar mg.st matches 4 run scoreboard players set $qt mg.st 7200
execute if score $ar mg.st matches 5 run scoreboard players set $qg mg.st 25
execute if score $ar mg.st matches 5 run scoreboard players set $qt mg.st 9600
execute if score $ar mg.st matches 6 run scoreboard players set $qg mg.st 30
execute if score $ar mg.st matches 6 run scoreboard players set $qt mg.st 12000
execute if score $ar mg.st matches 7 run scoreboard players set $qg mg.st 20
execute if score $ar mg.st matches 7 run scoreboard players set $qt mg.st 7200
execute if score $ar mg.st matches 8 run scoreboard players set $qg mg.st 30
execute if score $ar mg.st matches 8 run scoreboard players set $qt mg.st 12000
execute if score $ar mg.st matches 9 run scoreboard players set $qg mg.st 30
execute if score $ar mg.st matches 9 run scoreboard players set $qt mg.st 12000
execute if score $ar mg.st matches 10 run scoreboard players set $qg mg.st 20
execute if score $ar mg.st matches 10 run scoreboard players set $qt mg.st 7200
execute if score $ar mg.st matches 11 run scoreboard players set $qg mg.st 20
execute if score $ar mg.st matches 11 run scoreboard players set $qt mg.st 7200
execute if score $ar mg.st matches 12 run scoreboard players set $qg mg.st 20
execute if score $ar mg.st matches 12 run scoreboard players set $qt mg.st 7200
execute if score $ar mg.st matches 13 run scoreboard players set $qg mg.st 25
execute if score $ar mg.st matches 13 run scoreboard players set $qt mg.st 9600
execute if score $ar mg.st matches 14 run scoreboard players set $qg mg.st 25
execute if score $ar mg.st matches 14 run scoreboard players set $qt mg.st 9600
execute if score $ar mg.st matches 15 run scoreboard players set $qg mg.st 25
execute if score $ar mg.st matches 15 run scoreboard players set $qt mg.st 9600
execute if score $ar mg.st matches 16 run scoreboard players set $qg mg.st 25
execute if score $ar mg.st matches 16 run scoreboard players set $qt mg.st 9600
execute if score $ar mg.st matches 17 run scoreboard players set $qg mg.st 20
execute if score $ar mg.st matches 17 run scoreboard players set $qt mg.st 7200
execute if score $ar mg.st matches 18 run scoreboard players set $qg mg.st 30
execute if score $ar mg.st matches 18 run scoreboard players set $qt mg.st 12000
scoreboard players set $qcd mg.st 22
execute if score $dif mg.st matches 1 run scoreboard players set $qcd mg.st 16
execute if score $dif mg.st matches 3 run scoreboard players set $qcd mg.st 28
execute if score $dif mg.st matches 4 run scoreboard players set $qcd mg.st 34
function mg:var/arena/setup
scoreboard players set @a[tag=mg.play] mg.qk 0
scoreboard players set @a[tag=mg.play] mg.cd 0
