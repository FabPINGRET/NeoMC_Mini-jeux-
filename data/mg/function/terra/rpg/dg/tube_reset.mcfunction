scoreboard players set $trda3 mg.st 0
execute as @e[tag=mg.trdg_tube] at @s run tp @s ~ -400 ~
kill @e[tag=mg.trdg_tube]
scoreboard players set $trdc3 mg.st 10
bossbar set mg:trdg3 players
