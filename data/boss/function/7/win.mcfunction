function music:end
title @a[tag=mg.flw] actionbar {"text":"The evil has been driven from this place...","italic":true,"color":"gray"}
tag @a[tag=mg.flw] remove bossroom

kill @e[tag=chiseler,distance=0..]
kill @e[tag=stonestack,distance=0..]
kill @e[tag=obelisk,distance=0..]
kill @e[tag=knucklehead,distance=0..]
kill @e[tag=c_brute,distance=0..]

scoreboard players set mainstory Story 8
advancement grant @a[tag=mg.flw] only main_quest:seventh_dungeon
scoreboard players set $fla8 mg.fla 1
scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1

#lord of stone
setblock -9773 244 422 minecraft:redstone_block
