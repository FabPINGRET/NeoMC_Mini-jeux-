scoreboard players set $trda1 mg.st 0
execute as @e[tag=mg.trdg_pic] at @s run tp @s ~ -400 ~
kill @e[tag=mg.trdg_pic]
scoreboard players set $trdc1 mg.st 10
bossbar set mg:trdg1 players
