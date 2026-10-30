setblock 10467 48 102 air
setblock 10468 51 108 minecraft:mossy_cobblestone

scoreboard players set Inventory DungeonFlag 5
function game:blue_light_off
title @a[tag=mg.flw] times 25 75 25
title @a[tag=mg.flw] subtitle {"text":"Dungeon of the Lord of Forest","color":"gray","italic":true}
title @a[tag=mg.flw] title [{"color":"#54CC0E","text":"S"},{"color":"#53CF0E","text":"e"},{"color":"#53D30E","text":"r"},{"color":"#52D60E","text":"p"},{"color":"#52D90E","text":"e"},{"color":"#51DC0E","text":"n"},{"color":"#50E00E","text":"t "},{"color":"#50E30E","text":"K"},{"color":"#4FE60E","text":"i"},{"color":"#4EE60F","text":"n"},{"color":"#4CE111","text":"g"},{"color":"#4BDD13","text":"'"},{"color":"#49D815","text":"s "},{"color":"#47D417","text":"T"},{"color":"#45CF19","text":"o"},{"color":"#44CB1B","text":"m"},{"color":"#40C21F","text":"b"}]
tp @a[tag=mg.flw] -10137 92 299 90 0
function music:skt
spawnpoint @a[tag=mg.flw] -10139 84 299
scoreboard players set $flsp mg.st 9
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1
