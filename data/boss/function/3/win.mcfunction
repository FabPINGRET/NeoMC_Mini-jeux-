bossbar set boss:lod players
playsound minecraft:entity.ravager.attack hostile @a[tag=mg.flw] -10108 159 -189 1 0.1 1
playsound minecraft:entity.firework_rocket.twinkle_far hostile @a[tag=mg.flw] -10108 159 -189 1 0.1 1
function music:end
title @a[tag=mg.flw] actionbar {"text":"The evil has been driven from this place...","italic":true,"color":"gold"}
tag @a[tag=mg.flw] remove bossroom

kill @e[tag=c_sentinel,distance=0..]
kill @e[tag=s_leech,distance=0..]
kill @e[tag=s_elemental,distance=0..]

scoreboard players set mainstory Story 3
#Grigex Grez 2nd position
setblock -9769 268 416 minecraft:redstone_block
advancement grant @a[tag=mg.flw] only main_quest:third_dungeon
scoreboard players set $fla4 mg.fla 1
scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1

setblock -10083 134 -199 air
