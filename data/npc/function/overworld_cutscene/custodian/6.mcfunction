tp @a[tag=mg.flw] 10319 35 -105 0 0
setblock -9769 240 424 minecraft:redstone_block

scoreboard players set @a[tag=mg.flw] SoundtrackOverride 0
tag @a[tag=mg.flw] remove cutscene
tag @a[tag=mg.flw] remove no_warp

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
