summon arrow ~ ~ ~ {pickup:2b,damage:1d,Tags:["boss_sh_honeybomb_arrow"],SoundEvent:"block.honey_block.step"}

execute as @e[tag=boss_sh_honeybomb_arrow,distance=0..] store result entity @s Motion[0] double 0.001 run function boss:6/honeybomb/direction_x
execute as @e[tag=boss_sh_honeybomb_arrow,distance=0..] store result entity @s Motion[1] double 0.001 run random value 0..10
execute as @e[tag=boss_sh_honeybomb_arrow,distance=0..] store result entity @s Motion[2] double 0.001 run function boss:6/honeybomb/direction_z
