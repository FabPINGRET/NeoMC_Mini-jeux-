# Un pas du rayon (0,5 bloc) : bloc plein = fin ; joueur touché = tête puis corps ; air = on avance
execute unless loaded ~ ~ ~ run return 0
tp @e[type=minecraft:marker,tag=mg.dlend,distance=..1,limit=1] ~ ~ ~
execute unless block ~ ~ ~ #mg:ray_pass run return run particle minecraft:electric_spark ~ ~ ~ 0.1 0.1 0.1 0.1 4
# tête : 0,4 autour des yeux (1,62 debout, 1,27 accroupi : mg.dlcr), testée AVANT le corps
execute positioned ~ ~-1.62 ~ as @a[tag=mg.dl,tag=!mg.dlsh,tag=!mg.dlp,tag=!mg.dlcr,distance=..0.4,limit=1,sort=nearest] if score @s mg.dli = $dli mg.st run return run function mg:duel/hit_head
execute positioned ~ ~-1.27 ~ as @a[tag=mg.dl,tag=!mg.dlsh,tag=!mg.dlp,tag=mg.dlcr,distance=..0.4,limit=1,sort=nearest] if score @s mg.dli = $dli mg.st run return run function mg:duel/hit_head
# corps (zone resserrée sous la tête : un tir à la tête ne devient pas un tir au corps)
execute positioned ~ ~-0.7 ~ as @a[tag=mg.dl,tag=!mg.dlsh,tag=!mg.dlp,tag=!mg.dlcr,distance=..0.8,limit=1,sort=nearest] if score @s mg.dli = $dli mg.st run return run function mg:duel/hit_body
execute positioned ~ ~-0.5 ~ as @a[tag=mg.dl,tag=!mg.dlsh,tag=!mg.dlp,tag=mg.dlcr,distance=..0.75,limit=1,sort=nearest] if score @s mg.dli = $dli mg.st run return run function mg:duel/hit_body
scoreboard players remove $rs mg.st 1
execute if score $rs mg.st matches 1.. positioned ^ ^ ^0.5 run function mg:duel/ray
