advancement grant @a[tag=mg.flw] only main_quest:quest_5
scoreboard players set $fla47 mg.fla 1

bossbar set boss:zalvorn players

scoreboard players set zalvorn Story 3

#command tree disappear pygmy
setblock -9769 252 424 minecraft:redstone_block
setblock -9769 252 426 minecraft:redstone_block

#command tree disappear zalvorn
setblock -9769 252 428 minecraft:redstone_block

#command tree pupu-nini back at his post
setblock -9769 252 430 minecraft:redstone_block

scoreboard players set @a[tag=mg.flw] SoundtrackOverride 0
tag @a[tag=mg.flw] remove cutscene
tag @a[tag=mg.flw] remove no_warp

tp @a[tag=mg.flw] 214 43 117 180 0
spawnpoint @a[tag=mg.flw] 214 43 117
scoreboard players set $flsp mg.st 40

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
