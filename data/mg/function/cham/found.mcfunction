# @s (caméléon) trouvé par @a[tag=mg.cmhunt]
tag @s add mg.cmout
scoreboard players operation $cmid mg.st = @s mg.cmid
execute at @s run particle minecraft:dust{color:[1.0,0.3,0.6],scale:2} ~ ~0.8 ~ 0.4 0.6 0.4 0 40
execute at @s run particle minecraft:totem_of_undying ~ ~1 ~ 0.3 0.5 0.3 0.3 20
execute as @e[tag=mg.cmd] if score @s mg.cmid = $cmid mg.st run kill @s
execute as @e[tag=mg.cmi] if score @s mg.cmid = $cmid mg.st run kill @s
scoreboard players add @a[tag=mg.cmhunt] mg.cmf 1
scoreboard players add @a[tag=mg.cmhunt] mg.cmpts 25
clear @s
effect clear @s
attribute @s minecraft:scale base set 1
gamemode spectator @s
title @s title {"text":"🔍 Trouvé !","color":"red","bold":true}
title @s subtitle [{"text":"par ","color":"gray"},{"selector":"@a[tag=mg.cmhunt]","color":"red"}]
title @a[tag=mg.cmhunt] actionbar [{"text":"🎯 Trouvé : ","color":"green","bold":true},{"selector":"@s","color":"yellow"},{"text":"  +25","color":"gold"}]
tellraw @a[tag=mg.cmx] [{"text":"🦎 ","color":"green"},{"selector":"@s","color":"yellow"},{"text":" a été trouvé par ","color":"gray"},{"selector":"@a[tag=mg.cmhunt]","color":"red"}]
execute as @a[tag=mg.cmx] at @s run playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.6
