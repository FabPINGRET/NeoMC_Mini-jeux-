bossbar set boss:cob players
playsound minecraft:entity.enderman.scream hostile @a[tag=mg.flw] -10152 155 -31 1 0.1 1
playsound minecraft:entity.firework_rocket.twinkle_far hostile @a[tag=mg.flw] -10152 155 -31 1 0.1 1
function music:end
title @a[tag=mg.flw] actionbar {"text":"The evil has been driven from this place...","italic":true,"color":"gray"}
setblock -10151 138 -15 air
kill @e[tag=ck_eye,distance=0..]
kill @e[tag=o_archer,distance=0..]
kill @e[tag=o_infantry,distance=0..]
kill @e[tag=boneclaw,distance=0..]
kill @e[tag=bone_spur,distance=0..]

fill -10154 156 -28 -10154 157 -28 minecraft:blue_stained_glass
setblock -10154 157 -34 minecraft:blue_stained_glass
tag @a[tag=mg.flw] remove bossroom
effect give @a[tag=mg.flw] minecraft:fire_resistance 10 10 true

scoreboard players set mainstory Story 2
#Hide Smoke Doctor
setblock -9769 268 418 minecraft:redstone_block
advancement grant @a[tag=mg.flw] only main_quest:second_dungeon
scoreboard players set $fla3 mg.fla 1
#Open East Gate
setblock -9769 268 424 minecraft:redstone_block
#Open West Gate
setblock -9769 268 426 minecraft:redstone_block
#Empty Jail
setblock -9769 268 428 minecraft:redstone_block
#Ramdak return home
setblock -9769 268 430 minecraft:redstone_block
#Thorheal return home
setblock -9773 268 416 minecraft:redstone_block
scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1

setblock -10132 138 -60 air
