function music:end
title @a[tag=mg.flw] actionbar {"text":"The evil has been driven from this place...","italic":true,"color":"light_purple"}
tag @a[tag=mg.flw] remove bossroom

kill @e[tag=fungloom,distance=0..]
kill @e[tag=puffshot,distance=0..]
kill @e[tag=shellkin,distance=0..]
kill @e[tag=m_man,distance=0..]
kill @e[tag=h_slime,distance=0..]

scoreboard players set mainstory Story 7
advancement grant @a[tag=mg.flw] only main_quest:sixth_dungeon
scoreboard players set $fla7 mg.fla 1
kill @n[tag=boss_sh_loc,distance=0..]
scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1

setblock -10462 42 -55 air
setblock -10462 43 -63 air

#lord of spores
setblock -9773 244 418 minecraft:redstone_block
setblock -9773 244 420 minecraft:redstone_block
