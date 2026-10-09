$execute as @e[type=minecraft:block_display,tag=mg.cmd] if score @s mg.cmid = $cmid mg.st run tp @s ~ ~ ~ $(y) 0
execute as @e[type=minecraft:interaction,tag=mg.cmi] if score @s mg.cmid = $cmid mg.st run tp @s ~ ~ ~
