scoreboard players set @a[tag=mg.flw] SoundtrackOverride 0
tag @a[tag=mg.flw] remove cutscene
tag @a[tag=mg.flw] remove no_warp

#control sigil give
setblock -9773 240 418 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
