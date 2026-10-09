# Lance le mini-jeu tiré ($mgid, fixé par roulette_stop) comme si l'admin l'avait choisi ; core/return_lobby reviendra au plateau
title @a[tag=!mg.surv] reset
clear @a[tag=!mg.surv] minecraft:echo_shard
execute as @a[tag=mg.mpp,tag=!mg.spectate] run function mg:core/attr_reset
execute as @a[tag=mg.mpp,tag=!mg.spectate,gamemode=spectator] run gamemode adventure @s
execute as @e[type=minecraft:armor_stand,tag=mg.mpfocus] run data merge entity @s {Glowing:0b}
tag @e[type=minecraft:armor_stand] remove mg.mpfocus
team leave @a[tag=mg.mpp]
bossbar set mg:party visible false
scoreboard players set $mpl mg.st 1
scoreboard players set $state mg.st 0
execute if entity @a[tag=mg.mpa] as @a[tag=mg.mpa,limit=1] run function mg:party/launch_as
execute unless entity @a[tag=mg.mpa] as @a[tag=mg.mpp,limit=1] run function mg:party/launch_as
scoreboard players set $mpl mg.st 0
execute if score $state mg.st matches 0 as @a[tag=mg.mpp] run function mg:core/reset_player
execute if score $state mg.st matches 0 run function mg:party/end
execute if score $state mg.st matches 0 run tellraw @a [{"text":"[Mini Party] Plus aucun participant : partie arrêtée.","color":"red"}]
