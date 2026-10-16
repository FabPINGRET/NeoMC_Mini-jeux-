# Le Roi Tyran est vaincu : la faille se révèle
scoreboard players set $trra mg.st 0
scoreboard players set $trrc mg.st 180
kill @e[tag=mg.trgey]
bossbar set mg:trrex players
execute positioned 0 99 186 as @a[tag=mg.tvw,distance=..64] run function mg:terra/rpg/boss/rex_reward
particle minecraft:reverse_portal 0.5 101 177 1 2 0.3 0.1 300 force
