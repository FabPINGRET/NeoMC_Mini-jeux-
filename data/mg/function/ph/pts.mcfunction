# Points des cacheurs : regardé par un chercheur (+2), en mouvement (+1)
execute as @a[tag=mg.phs,gamemode=!spectator] at @s anchored eyes positioned ^ ^ ^0.5 run function mg:ph/look
execute as @e[type=minecraft:interaction,tag=mg.phlk] run function mg:ph/looked
scoreboard players add @a[tag=mg.phh,scores={mg.phs=..4}] mg.phpt 1
