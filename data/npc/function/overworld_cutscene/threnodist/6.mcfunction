spawnpoint @a[tag=mg.flw] 285 80 1454 180 0
scoreboard players set $flsp mg.st 36
setblock 288 78 1452 minecraft:redstone_torch

scoreboard players set @a[tag=mg.flw] SoundtrackOverride 0
tag @a[tag=mg.flw] remove cutscene
tag @a[tag=mg.flw] remove no_warp

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
