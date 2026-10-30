setblock -9827 246 567 air
setblock -9832 248 564 minecraft:chiseled_quartz_block

scoreboard players set Inventory DungeonFlag 9
function game:blue_light_off
title @a[tag=mg.flw] times 25 75 25
title @a[tag=mg.flw] subtitle {"text":"Dungeon of the Lord of Water","color":"gray","italic":true}
title @p[tag=mg.flw] title [{"color":"#17B9FF","text":"W"},{"color":"#18BAFF","text":"e"},{"color":"#19BCFF","text":"l"},{"color":"#1ABDFF","text":"l"},{"color":"#1BBEFF","text":"s"},{"color":"#1CC0FF","text":"p"},{"color":"#1DC1FF","text":"r"},{"color":"#1EC2FF","text":"i"},{"color":"#22C1FF","text":"n"},{"color":"#28BCFF","text":"g "},{"color":"#2DB7FF","text":"M"},{"color":"#33B2FF","text":"a"},{"color":"#39ADFF","text":"n"},{"color":"#3FA8FF","text":"o"},{"color":"#4A9EFF","text":"r"}]
tp @a[tag=mg.flw] -10793 126 -60 90 13
function music:wm
spawnpoint @a[tag=mg.flw] -10799 80 -57 90 0
scoreboard players set $flsp mg.st 13
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1
