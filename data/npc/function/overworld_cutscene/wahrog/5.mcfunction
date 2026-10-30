tag @a[tag=mg.flw] remove targeted
tag @a[tag=mg.flw] remove cutscene
tag @a[tag=mg.flw] remove no_warp
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 0

tp @a[tag=mg.flw] -9864 109 557 180 0
schedule function floaty:sched/npc/overworld_cutscene/wahrog/6 2s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
