# Le Roi Tyran se dresse dans la caldeira
execute positioned 0.5 99 181.5 run function mg:terra/dino/rex
tag @e[tag=mg.tvlast] add mg.trboss
scoreboard players set $trra mg.st 1
scoreboard players set $trr1 mg.st 6
scoreboard players set $trr2 mg.st 9
scoreboard players set $trr3 mg.st 12
scoreboard players set $trr4 mg.st 20
scoreboard players set $trrr mg.st 0
bossbar set mg:trrex max 900
bossbar set mg:trrex value 900
execute positioned 0 99 186 as @a[tag=mg.tvw,gamemode=adventure,distance=..60] run function mg:terra/rpg/cs/boss_rex
execute as @e[tag=mg.tvrex] run data merge entity @s {NoAI:1b}
scoreboard players set @e[tag=mg.tvrex] mg.tvat 140
tag @e[tag=mg.tvrex] add mg.tvroar
schedule function mg:terra/rpg/boss/wake 140t
execute as @e[tag=mg.tvrex] run function mg:terra/rpg/boss/rex_roar
