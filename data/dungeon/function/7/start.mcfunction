setblock 10085 181 1280 air
setblock 10085 186 1282 minecraft:chiseled_tuff

scoreboard players set Inventory DungeonFlag 7
function game:blue_light_off
title @a[tag=mg.flw] times 25 75 25
title @a[tag=mg.flw] subtitle {"text":"Dungeon of the Lord of Stone","color":"gray","italic":true}
title @a[tag=mg.flw] title [{"color":"#9AAD9E","text":"S"},{"color":"#9DB3A0","text":"h"},{"color":"#A1B9A3","text":"r"},{"color":"#A4BFA5","text":"u"},{"color":"#A7C4A7","text":"n"},{"color":"#AACAAA","text":"k"},{"color":"#AED0AC","text":"e"},{"color":"#B1D6AF","text":"n "},{"color":"#B4DCB1","text":"T"},{"color":"#B8E2B3","text":"e"},{"color":"#BBE8B6","text":"m"},{"color":"#BEEDB8","text":"p"},{"color":"#C1F3BA","text":"l"},{"color":"#C8FFBF","text":"e"}]
tp @a[tag=mg.flw] -10186 117 -378 90 0
function music:st
spawnpoint @a[tag=mg.flw] -10189 95 -378 90 0
scoreboard players set $flsp mg.st 11
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1
