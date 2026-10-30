summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}
summon arrow ~ ~ ~ {pickup:2b,damage:10d,Tags:["boss_sh_arrowspit"],SoundEvent:"block.mud.step"}

execute as @e[tag=boss_sh_arrowspit,nbt={inGround:0b},distance=0..] run data modify entity @s Owner set from entity @n[tag=boss_sh_loc,distance=0..] UUID

execute as @e[tag=boss_sh_arrowspit,nbt={inGround:0b},distance=0..] store result entity @s Motion[0] double 0.001 run function boss:6/arrow_spit/direction_x
execute as @e[tag=boss_sh_arrowspit,nbt={inGround:0b},distance=0..] store result entity @s Motion[1] double 0.001 run random value -100..500
execute as @e[tag=boss_sh_arrowspit,nbt={inGround:0b},distance=0..] store result entity @s Motion[2] double 0.001 run function boss:6/arrow_spit/direction_z
