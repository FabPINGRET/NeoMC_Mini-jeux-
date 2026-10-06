clear @a minecraft:echo_shard
execute at @a[tag=mg.mpcur,limit=1] run tp @e[type=minecraft:text_display,tag=mg.mpdice,limit=1] ~ ~3.6 ~
scoreboard players set $mph mg.st 2
scoreboard players set $mpw mg.st 30
