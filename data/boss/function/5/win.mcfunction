function music:end
title @a[tag=mg.flw] actionbar {"text":"The evil has been driven from this place...","italic":true,"color":"green"}
tag @a[tag=mg.flw] remove bossroom

kill @e[tag=r_soul,distance=0..]
kill @e[tag=cuauhtli,distance=0..]

kill @e[tag=m_corpse,distance=0..]
kill @e[tag=hewer,distance=0..]
kill @e[tag=v_rockward,distance=0..]
kill @e[tag=jungleworn,distance=0..]

scoreboard players set mainstory Story 6
advancement grant @a[tag=mg.flw] only main_quest:fifth_dungeon
scoreboard players set $fla6 mg.fla 1

scoreboard players set Inventory Time 2
scoreboard players set Inventory DayNight 1

setblock -10197 55 405 air

#lord of forest
setblock -9773 244 416 minecraft:redstone_block
