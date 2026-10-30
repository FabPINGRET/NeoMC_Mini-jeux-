setblock 283 56 -162 minecraft:blue_terracotta
setblock 284 50 -158 air
scoreboard players set Inventory DungeonFlag 3
function game:blue_light_off
title @a[tag=mg.flw] times 25 75 25
title @a[tag=mg.flw] subtitle {"text":"Dust Contagion Stronghold","color":"gray","italic":true}
title @a[tag=mg.flw] title [{"color":"#7B22D4","text":"L"},{"color":"#8028DB","text":"i"},{"color":"#862EE1","text":"b"},{"color":"#8B34E8","text":"r"},{"color":"#913BEE","text":"a"},{"color":"#9641F5","text":"r"},{"color":"#9B47FC","text":"y "},{"color":"#9B44FD","text":"o"},{"color":"#9639F9","text":"f "},{"color":"#912EF5","text":"D"},{"color":"#8C23F2","text":"u"},{"color":"#8618EE","text":"s"},{"color":"#7C02E6","text":"t"}]
tp @a[tag=mg.flw] -9903 168 -161 90 0
function music:lod
spawnpoint @a[tag=mg.flw] -9907 155 -161
scoreboard players set $flsp mg.st 7
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
scoreboard players set @a[tag=mg.flw] sneak_last 0
scoreboard players set @a[tag=mg.flw] push_mode 0
scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1

#Push/Pull check on
setblock -9762 272 431 minecraft:redstone_block

#clean mindczar quest tag mess
tag @a[tag=mg.flw] remove anchorblade
execute if score mindczar Story matches 3 run scoreboard players set mindczar Story 4
