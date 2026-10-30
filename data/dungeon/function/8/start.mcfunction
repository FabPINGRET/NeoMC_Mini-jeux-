setblock 9794 49 78 minecraft:air
setblock 9797 56 77 minecraft:snow_block

scoreboard players set Inventory DungeonFlag 8
function game:blue_light_off
title @a[tag=mg.flw] times 25 75 25
title @a[tag=mg.flw] subtitle {"text":"Dungeon of the Lord of Ice","color":"gray","italic":true}
title @a[tag=mg.flw] title [{"color":"#03EEFF","text":"F"},{"color":"#1AF0FC","text":"r"},{"color":"#31F3F8","text":"o"},{"color":"#48F5F5","text":"s"},{"color":"#5EF8F1","text":"t"},{"color":"#75FAEE","text":"b"},{"color":"#8CFDEA","text":"o"},{"color":"#A3FFE7","text":"l"},{"color":"#8DFFE2","text":"t "},{"color":"#77FFDD","text":"S"},{"color":"#61FFD8","text":"p"},{"color":"#4AFFD4","text":"i"},{"color":"#34FFCF","text":"r"},{"color":"#08FFC5","text":"e"}]
tp @a[tag=mg.flw] -10618 29 382 90 0
function music:fs
spawnpoint @a[tag=mg.flw] -10618 1 382 90 0
scoreboard players set $flsp mg.st 12
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1

#Start fan
setblock -9764 273 431 minecraft:redstone_block
