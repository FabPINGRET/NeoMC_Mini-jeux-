# Piétinement : onde de choc autour du Roi
scoreboard players set $trr1 mg.st 8
scoreboard players set @s mg.tvat 10
execute unless entity @a[tag=mg.tvw,gamemode=adventure,distance=..8] run return 0
particle minecraft:explosion ~ ~0.5 ~ 3 0.2 3 0 12
particle minecraft:block{block_state:"minecraft:blackstone"} ~ ~0.3 ~ 4 0.2 4 0 120
playsound minecraft:entity.generic.explode hostile @a ~ ~ ~ 1.5 0.5
execute as @a[tag=mg.tvw,gamemode=adventure,distance=..8] run damage @s 9 minecraft:mob_attack by @e[tag=mg.tvrex,limit=1]
