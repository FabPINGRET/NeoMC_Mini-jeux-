scoreboard players set Inventory DungeonFlag 12
function game:blue_light_off
title @a[tag=mg.flw] times 25 75 25
title @a[tag=mg.flw] subtitle {"text":"Domain of the World Virus","color":"dark_aqua","italic":true}
title @a[tag=mg.flw] title [{"color":"#00FFFF","text":"V"},{"color":"#09ECF0","text":"i"},{"color":"#11DAE1","text":"r"},{"color":"#1AC7D3","text":"i"},{"color":"#22B4C4","text":"o"},{"color":"#338FA6","text":"n"}]
tp @a[tag=mg.flw] -12134 55 336 90 -5
function music:virion
spawnpoint @a[tag=mg.flw] -12134 55 336
scoreboard players set $flsp mg.st 15
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
#Start Glass Death Tick
setblock -9772 273 431 minecraft:redstone_block

#setblock 151 81 -7 air
