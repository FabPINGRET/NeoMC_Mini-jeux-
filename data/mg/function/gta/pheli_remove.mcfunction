# @s : l'hélico de police repart
scoreboard players operation $gv mg.st = @s mg.gvid
execute as @e[type=minecraft:block_display] if score @s mg.gvid = $gv mg.st run kill @s
kill @s
