# @s (voiture PNJ, à sa position) : la carrosserie suit
scoreboard players operation $gv mg.st = @s mg.gvid
execute as @e[type=minecraft:block_display,tag=mg.gtrd] if score @s mg.gvid = $gv mg.st run tp @s ~ ~ ~ ~ 0
execute as @e[type=minecraft:interaction,tag=mg.gtint] if score @s mg.gvid = $gv mg.st run tp @s ~ ~ ~
