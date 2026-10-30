bossbar set boss:sop players
kill @e[tag=a_sunflower,distance=0..]
kill @e[tag=b_peahead,distance=0..]

setblock -9930 167 167 air
setblock -9934 167 149 air
playsound minecraft:entity.enderman.scream hostile @a[tag=mg.flw] -9934 179 148 1 0.1 1
playsound minecraft:entity.firework_rocket.twinkle_far hostile @a[tag=mg.flw] -9934 179 148 1 0.1 1
function music:end
title @a[tag=mg.flw] actionbar {"text":"The evil has been driven from this place...","italic":true,"color":"light_purple"}
schedule clear floaty:sched/boss/1/cherry_explode
tag @a[tag=mg.flw] remove bossroom

scoreboard players set mainstory Story 1
#Robbo Position 1
setblock -9765 268 430 minecraft:redstone_block
advancement grant @a[tag=mg.flw] only main_quest:first_dungeon
scoreboard players set $fla1 mg.fla 1
scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1
