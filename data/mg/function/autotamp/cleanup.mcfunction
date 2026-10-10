kill @e[type=#mg:at_boats,tag=mg.atb]
kill @e[tag=mg.ats]
bossbar remove mg:autotamp
team leave @a[team=mg_at]
tag @a remove mg.atw
scoreboard players reset * mg.atl
scoreboard players reset * mg.atid
effect clear @a[tag=mg.play] minecraft:resistance
effect clear @a[tag=mg.play] minecraft:saturation
