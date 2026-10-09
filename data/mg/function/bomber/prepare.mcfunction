# 💣 Bombardier : préparation (construction en étapes pendant le compte à rebours)
fill -88 170 32312 88 170 32488 minecraft:barrier
scoreboard players set $bbs mg.st 0
execute if data storage mg:bomber v1 run scoreboard players set $bbs mg.st 40
function mg:bomber/build_step
kill @e[tag=mg.bomb]
kill @e[tag=mg.bsm]
scoreboard players set $bdes mg.st 0
scoreboard players set $bpct mg.st 0
scoreboard players set $bidn mg.st 0
scoreboard players reset * mg.bmb
execute as @a[tag=mg.play] run function mg:bomber/join
gamemode adventure @a[tag=mg.play]
clear @a[tag=mg.play]
spreadplayers 0 32400 6 50 under 173 false @a[tag=mg.play]
execute as @a[tag=mg.play] at @s run tp @s ~ 171 ~ ~ 60
bossbar add mg:bomber {"text":"🏙 Ville détruite : 0 %","color":"red"}
bossbar set mg:bomber max 160552
bossbar set mg:bomber value 0
bossbar set mg:bomber color red
bossbar set mg:bomber style notched_10
bossbar set mg:bomber players @a[tag=mg.play]
