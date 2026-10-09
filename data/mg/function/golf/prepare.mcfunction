# ⛳ Golf — préparation (pendant le compte à rebours) : zone chargée, parcours construit si besoin, joueurs au départ 1
scoreboard players set $gfok mg.st 0
scoreboard players set $gfh mg.st 0
scoreboard players set $gfw mg.st 0
scoreboard players set $gfn mg.st 0
scoreboard players set $gfwait mg.st 0
scoreboard players set $gfpc mg.st 0
scoreboard players set #gf2 mg.st 2
scoreboard players set #gf4 mg.st 4
scoreboard players set #gf10 mg.st 10
scoreboard players set #gf100 mg.st 100
scoreboard players set #gf1000 mg.st 1000
scoreboard players set #gf10000 mg.st 10000
scoreboard players set #gfm1 mg.st -1
scoreboard players set #gfdrag mg.st 990
scoreboard players set #gf5 mg.st 5
scoreboard players set #gf8 mg.st 8
scoreboard players set #gfest1 mg.st 93
scoreboard players set #gfest2 mg.st 16
scoreboard players set $px mg.st 300
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 34600
gamemode adventure @a[tag=mg.play]
clear @a[tag=mg.play]
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
effect give @a[tag=mg.play] minecraft:resistance infinite 4 true
team join mg_golf @a[tag=mg.play]
scoreboard players reset * mg.gft
scoreboard players reset * mg.gfd
scoreboard players reset * mg.gfi
scoreboard players set @a[tag=mg.play] mg.gft 0
scoreboard players set @a[tag=mg.play] mg.gfs 2
scoreboard players set @a[tag=mg.play] mg.gfc 0
execute as @a[tag=mg.play] run function mg:golf/assign
kill @e[tag=mg.gfb]
kill @e[tag=mg.gff]
kill @e[tag=mg.gftg]
forceload add 196 34496 404 34704
schedule function mg:golf/wait 10t
