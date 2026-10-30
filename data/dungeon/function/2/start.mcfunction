setblock -335 50 -247 air
setblock -341 56 -250 minecraft:bone_block[axis=z]
scoreboard players set Inventory DungeonFlag 2
function game:blue_light_off
title @a[tag=mg.flw] times 25 75 25
title @a[tag=mg.flw] subtitle {"text":"Bone Contagion Stronghold","color":"gray","italic":true}
title @a[tag=mg.flw] title [{"color":"#CF3E00","text":"C"},{"color":"#D64B00","text":"r"},{"color":"#DD5800","text":"u"},{"color":"#E46500","text":"c"},{"color":"#EA7200","text":"i"},{"color":"#F17F00","text":"b"},{"color":"#F88C00","text":"l"},{"color":"#FF9900","text":"e "},{"color":"#F28300","text":"o"},{"color":"#E66D00","text":"f "},{"color":"#D95700","text":"B"},{"color":"#CC4200","text":"o"},{"color":"#BF2C00","text":"n"},{"color":"#A60000","text":"e"}]
tp @a[tag=mg.flw] -9920 165 -11 90 0
function music:cob
spawnpoint @a[tag=mg.flw] -9923 147 -11
scoreboard players set $flsp mg.st 6
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
scoreboard players set Inventory Time 3
scoreboard players set Inventory DayNight 2
