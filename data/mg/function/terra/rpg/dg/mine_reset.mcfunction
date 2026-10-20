scoreboard players set $trda2 mg.st 0
execute as @e[tag=mg.trdg_mine] at @s run tp @s ~ -400 ~
kill @e[tag=mg.trdg_mine]
scoreboard players set $trdc2 mg.st 10
bossbar set mg:trdg2 players
