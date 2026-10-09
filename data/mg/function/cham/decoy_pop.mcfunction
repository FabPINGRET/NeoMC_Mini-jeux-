# @s (zone d'un leurre) touchée par un chasseur ($cmhunt) : le leurre éclate, le chasseur est ralenti 3 s
scoreboard players operation $cmv mg.st = @s mg.cmdn
execute as @e[type=minecraft:block_display,tag=mg.cmdd] if score @s mg.cmdn = $cmv mg.st run kill @s
particle minecraft:poof ~ ~1 ~ 0.4 0.6 0.4 0.05 25
particle minecraft:witch ~ ~1 ~ 0.4 0.6 0.4 0 15
playsound minecraft:entity.illusioner.cast_spell player @a ~ ~ ~ 1 1.4
effect give @a[tag=mg.cmhunt] minecraft:slowness 3 2 true
title @a[tag=mg.cmhunt] actionbar {"text":"👥 C'était un leurre !","color":"light_purple","bold":true}
kill @s
