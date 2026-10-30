bossbar set boss:ed players
playsound minecraft:entity.ravager.hurt hostile @a[tag=mg.flw] -10058 116 -355 3 0.1 1
playsound minecraft:entity.firework_rocket.twinkle_far hostile @a[tag=mg.flw] -10058 116 -355 3 0.1 1
playsound minecraft:entity.strider.death master @a[tag=mg.flw] -10058 116 -355 4 0.1
function music:end
title @a[tag=mg.flw] actionbar {"text":"The evil has been driven from this place...","italic":true,"color":"red"}
tag @a[tag=mg.flw] remove bossroom

kill @e[type=magma_cube,distance=0..]
kill @e[tag=magmount,distance=0..]
kill @e[tag=r_knight,distance=0..]
kill @e[tag=wisp,distance=0..]
kill @e[tag=m_imp,distance=0..]

scoreboard players set mainstory Story 5
advancement grant @a[tag=mg.flw] only main_quest:fourth_dungeon
scoreboard players set $fla5 mg.fla 1
schedule function floaty:sched/boss/4/cutscene/lord_1 2.4s
scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1

spawnpoint @a[tag=mg.flw] 9900 57 -241 0 0
scoreboard players set $flsp mg.st 1

setblock -10061 95 -367 air

#COMMAND TREE FOR OVERWORLD CHANGES

#hide Zalvorn
setblock -9769 252 418 minecraft:redstone_block

#open bridge to dark wilds
setblock -9761 244 428 minecraft:redstone_block

#return lord of flame
setblock -9761 244 430 minecraft:redstone_block

#free prisoners
setblock -9765 244 416 minecraft:redstone_block
setblock -9765 244 418 minecraft:redstone_block
setblock -9765 244 420 minecraft:redstone_block
setblock -9765 244 422 minecraft:redstone_block

#dark gill guild
setblock -9765 244 424 minecraft:redstone_block
setblock -9765 244 426 minecraft:redstone_block
setblock -9765 244 428 minecraft:redstone_block

#remove valor tower germ eater
setblock -9765 244 430 minecraft:redstone_block

#remove street germ eaters
setblock -9769 244 416 minecraft:redstone_block
setblock -9769 244 418 minecraft:redstone_block
setblock -9769 244 420 minecraft:redstone_block
setblock -9769 244 422 minecraft:redstone_block
setblock -9769 244 424 minecraft:redstone_block

#valor tower attendants
setblock -9769 244 426 minecraft:redstone_block
setblock -9769 244 428 minecraft:redstone_block
setblock -9769 244 430 minecraft:redstone_block

#open valor tower brendeloy
setblock -9769 240 418 minecraft:redstone_block
