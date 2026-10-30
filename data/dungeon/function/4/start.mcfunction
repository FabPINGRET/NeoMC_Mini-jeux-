setblock 9900 56 -242 minecraft:iron_block
setblock 9895 49 -246 air

scoreboard players set Inventory DungeonFlag 4
function game:blue_light_off
title @a[tag=mg.flw] times 25 75 25
title @a[tag=mg.flw] subtitle {"text":"Dungeon of the Lord of Flame","color":"gray","italic":true}
title @a[tag=mg.flw] title [{"color":"#C46C4C","text":"E"},{"color":"#BE6949","text":"m"},{"color":"#B76646","text":"b"},{"color":"#9C6649","text":"e"},{"color":"#6C6952","text":"r "},{"color":"#3C6C5C","text":"D"},{"color":"#498972","text":"e"},{"color":"#56A689","text":"p"},{"color":"#5CB494","text":"o"},{"color":"#5CB494","text":"t"}]
tp @a[tag=mg.flw] -9914 120 -355 90 0
function music:ed
spawnpoint @a[tag=mg.flw] -9919 108 -355
scoreboard players set $flsp mg.st 8
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1
