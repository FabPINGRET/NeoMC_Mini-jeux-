setblock 10446 53 -379 air
setblock 10440 57 -381 minecraft:mud

scoreboard players set Inventory DungeonFlag 6
function game:blue_light_off
title @a[tag=mg.flw] times 25 75 25
title @a[tag=mg.flw] subtitle {"text":"Dungeon of the Lord of Spores","color":"gray","italic":true}
title @a[tag=mg.flw] title [{"color":"#9A3EE0","text":"S"},{"color":"#9F40E5","text":"t"},{"color":"#A442EA","text":"i"},{"color":"#A944F0","text":"c"},{"color":"#AD46F5","text":"k"},{"color":"#B248FA","text":"y "},{"color":"#B74AFF","text":"H"},{"color":"#B040F9","text":"o"},{"color":"#AA36F2","text":"l"},{"color":"#A32DEC","text":"l"},{"color":"#9C23E6","text":"o"},{"color":"#8F0FD9","text":"w"}]
tp @a[tag=mg.flw] -10300 46 -71 90 0
function music:sh
spawnpoint @a[tag=mg.flw] -10302 23 -71
scoreboard players set $flsp mg.st 10
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
scoreboard players set Inventory Time 1
scoreboard players set Inventory DayNight 1
