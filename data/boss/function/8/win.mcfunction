function music:end
title @a[tag=mg.flw] actionbar {"text":"The evil has been driven from this place...","italic":true,"color":"aqua"}
tag @a[tag=mg.flw] remove bossroom
tag @a[tag=mg.flw] remove targeted

kill @e[tag=zephrovolt,distance=0..]
kill @e[tag=hailman,distance=0..]
kill @e[tag=mirro,distance=0..]
kill @e[tag=glacriarch,distance=0..]
kill @e[tag=frodrone,distance=0..]

scoreboard players set mainstory Story 9
advancement grant @a[tag=mg.flw] only main_quest:eighth_dungeon
scoreboard players set $fla9 mg.fla 1
scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1

#lord of ice
setblock -9773 244 424 minecraft:redstone_block

#Stop Fans
setblock -9764 273 431 air

fill -10844 89 370 -10842 98 368 air replace light
fill -10841 89 371 -10839 98 369 air replace light
fill -10838 89 372 -10836 98 370 air replace light
fill -10835 89 373 -10833 98 371 air replace light
fill -10830 89 372 -10832 98 392 air replace light
fill -10833 89 393 -10835 98 391 air replace light
fill -10836 89 394 -10838 98 392 air replace light
fill -10839 89 395 -10841 98 393 air replace light
fill -10842 89 396 -10844 98 394 air replace light

execute positioned -10843 88 395 run function dungeon:8/stop_fan
execute positioned -10840 88 394 run function dungeon:8/stop_fan
execute positioned -10837 88 393 run function dungeon:8/stop_fan
execute positioned -10834 88 392 run function dungeon:8/stop_fan
execute positioned -10831 88 391 run function dungeon:8/stop_fan
execute positioned -10831 88 388 run function dungeon:8/stop_fan
execute positioned -10831 88 385 run function dungeon:8/stop_fan
execute positioned -10831 88 382 run function dungeon:8/stop_fan
execute positioned -10831 88 379 run function dungeon:8/stop_fan
execute positioned -10831 88 376 run function dungeon:8/stop_fan
execute positioned -10831 88 373 run function dungeon:8/stop_fan
execute positioned -10834 88 372 run function dungeon:8/stop_fan
execute positioned -10837 88 371 run function dungeon:8/stop_fan
execute positioned -10840 88 370 run function dungeon:8/stop_fan
execute positioned -10843 88 369 run function dungeon:8/stop_fan

#vendors

#valorforge
setblock -9773 244 428 minecraft:redstone_block
#glenfolk castle
setblock -9773 244 430 minecraft:redstone_block
#glenfolk dwarf city
setblock -9761 240 416 minecraft:redstone_block
setblock -9761 240 418 minecraft:redstone_block
