# La reine du marais surgit de la lagune
execute positioned 10.5 65 -195.5 run function mg:terra/dino/spino
tag @e[tag=mg.tvlast] add mg.trboss
scoreboard players set $trspa mg.st 1
scoreboard players set $trs1 mg.st 6
scoreboard players set $trs2 mg.st 14
scoreboard players set $trs3 mg.st 18
scoreboard players set $trsr mg.st 0
bossbar set mg:trspino max 650
bossbar set mg:trspino value 650
execute positioned 10 65 -196 as @a[tag=mg.tvw,gamemode=adventure,distance=..60] run function mg:terra/rpg/cs/boss_spino
execute as @e[tag=mg.tvspino] run data merge entity @s {NoAI:1b}
scoreboard players set @e[tag=mg.tvspino] mg.tvat 120
tag @e[tag=mg.tvspino] add mg.tvroar
schedule function mg:terra/rpg/boss/wake 120t
particle minecraft:splash 10 66 -196 3 1 3 0 200 force
