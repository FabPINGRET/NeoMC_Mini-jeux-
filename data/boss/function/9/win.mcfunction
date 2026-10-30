function music:end
title @a[tag=mg.flw] actionbar {"text":"The evil has been driven from this place...","italic":true,"color":"blue"}
tag @a[tag=mg.flw] remove bossroom

scoreboard players set mainstory Story 10
advancement grant @a[tag=mg.flw] only main_quest:ninth_dungeon
scoreboard players set $fla10 mg.fla 1
scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1
bossbar set boss:wm players

kill @e[tag=encruster,distance=0..]
kill @e[tag=i_thought,distance=0..]
kill @e[tag=f_notion,distance=0..]
kill @e[tag=doubt,distance=0..]

# stop boss tick
setblock -11245 -34 -132 air

#lord of water
setblock -9773 244 426 minecraft:redstone_block

#NOT IN COMMAND TREE
#tea party
setblock 10658 79 -77 minecraft:redstone_block
setblock 10682 79 -65 minecraft:redstone_block
setblock 10682 79 -55 minecraft:redstone_block
setblock 10659 79 -52 minecraft:redstone_block

#xenemund stolen
setblock 330 77 1610 minecraft:redstone_block

#COMMAND TREE
#tea party
setblock -9761 240 420 minecraft:redstone_block
setblock -9761 240 422 minecraft:redstone_block
setblock -9761 240 424 minecraft:redstone_block
setblock -9761 240 426 minecraft:redstone_block

#xenemund stolen
setblock -9761 240 428 minecraft:redstone_block
