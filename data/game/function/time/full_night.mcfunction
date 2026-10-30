scoreboard players set Inventory DayNight 2

execute if score moonlight_contagion bool matches 0 run scoreboard players set bot_lycan bool 1
execute if score moonlight_contagion bool matches 1 run scoreboard players set golem_lycan bool 1

#Store Moon Phase (0 is full, 4 is new)
execute in mg:floaty store result score moon_phase Value run time query day
scoreboard players operation moon_phase Value %= 8 Value

#Clear Despawn Checking
fill -9776 264 416 -9761 264 431 air replace minecraft:redstone_block

#Summon Glenfolk
setblock -9761 264 416 minecraft:redstone_block
#Summon Bugboy Forest
setblock -9761 264 418 minecraft:redstone_block
#Summon Noparentopia
setblock -9761 264 420 minecraft:redstone_block
#Summon Dwarf City
setblock -9761 264 422 minecraft:redstone_block
#Summon Warped Land
setblock -9761 264 424 minecraft:redstone_block
#Summon Magma Kingdom
setblock -9761 264 426 minecraft:redstone_block
#Summon Dryskull Desert
setblock -9761 264 428 minecraft:redstone_block
#Summon Bubble Lake
setblock -9761 264 430 minecraft:redstone_block
#Summon Isle of Ice
setblock -9764 264 417 minecraft:redstone_block
#Summon Valorforge
setblock -9764 264 419 minecraft:redstone_block
#Summon Brain Mesa
setblock -9764 264 421 minecraft:redstone_block
#Summon Dark Wilds
setblock -9764 264 423 minecraft:redstone_block
#Summon Tanglevine Jungle
setblock -9764 264 425 minecraft:redstone_block
#Summon Moldsap Woods
setblock -9764 264 427 minecraft:redstone_block
#Summon Isle of Silence
setblock -9764 264 429 minecraft:redstone_block
#Summon Windbite Tundra
setblock -9764 264 431 minecraft:redstone_block
#Summon Alabaster Pools
setblock -9767 264 416 minecraft:redstone_block
#Summon Isle of Smoke
setblock -9767 264 418 minecraft:redstone_block

execute if block -9776 304 431 minecraft:redstone_block run schedule function floaty:sched/tool/enemy_debug 2t
