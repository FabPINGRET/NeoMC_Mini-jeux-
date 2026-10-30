setblock 10004 52 240 air
setblock 9997 58 244 minecraft:chiseled_polished_blackstone

scoreboard players set Inventory DungeonFlag 10
function game:blue_light_off
title @a[tag=mg.flw] times 25 75 25
title @a[tag=mg.flw] subtitle {"text":"Dungeon of the Lord of Smoke","color":"gray","italic":true}
title @a[tag=mg.flw] title [{"color":"#EDC31C","text":"T"},{"color":"#F2CD1D","text":"h"},{"color":"#F7D81F","text":"e "},{"color":"#FCE220","text":"A"},{"color":"#FDE522","text":"l"},{"color":"#F8DA27","text":"l"},{"color":"#F2CE2B","text":"g"},{"color":"#EDC330","text":"r"},{"color":"#EFC628","text":"a"},{"color":"#F4D11B","text":"v"},{"color":"#FFE600","text":"e"}]
tp @a[tag=mg.flw] -11489 157 410 90 0
function music:ta
spawnpoint @a[tag=mg.flw] -11492 132 410
scoreboard players set $flsp mg.st 5
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1

#START DUNGEON TICK
setblock -9770 273 431 minecraft:redstone_block
scoreboard players set @a[tag=mg.flw] twister_timer 0
