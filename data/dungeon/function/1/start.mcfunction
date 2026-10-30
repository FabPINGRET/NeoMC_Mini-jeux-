setblock -4 52 -29 air
setblock -2 56 -23 minecraft:sculk
scoreboard players set Inventory DungeonFlag 1
function game:blue_light_off
title @a[tag=mg.flw] times 25 75 25
title @a[tag=mg.flw] subtitle {"text":"Bloom Contagion Stronghold","color":"gray","italic":true}
title @a[tag=mg.flw] title [{"color":"#CF006E","text":"S"},{"color":"#D50E79","text":"a"},{"color":"#DC1D85","text":"n"},{"color":"#E22B90","text":"c"},{"color":"#E9399C","text":"t"},{"color":"#EF47A7","text":"u"},{"color":"#F556B3","text":"m "},{"color":"#FC64BE","text":"o"},{"color":"#FF67C4","text":"f "},{"color":"#FF60C4","text":"P"},{"color":"#FF59C4","text":"e"},{"color":"#FF52C4","text":"t"},{"color":"#FF4BC3","text":"a"},{"color":"#FF44C3","text":"l"},{"color":"#FF36C3","text":"s"}]
tp @a[tag=mg.flw] -9882 203 272 90 0
function music:sop
spawnpoint @a[tag=mg.flw] -9885 191 272 90 0
scoreboard players set $flsp mg.st 4
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1
