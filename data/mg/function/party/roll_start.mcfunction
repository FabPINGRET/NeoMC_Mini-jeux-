clear @a[tag=!mg.surv] minecraft:echo_shard
execute at @e[type=minecraft:armor_stand,tag=mg.mpfocus,limit=1] run tp @e[type=minecraft:text_display,tag=mg.mpdice,limit=1] ~ ~3 ~
scoreboard players set $mph mg.st 2
scoreboard players set $mpw mg.st 50
