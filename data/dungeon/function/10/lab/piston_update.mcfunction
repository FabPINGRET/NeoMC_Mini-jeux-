fill -11709 215 305 -11709 215 309 air

execute if block -11713 217 306 lever[face=floor,facing=west,powered=true] if block -11713 217 307 lever[face=floor,facing=west,powered=true] run setblock -11709 215 305 minecraft:redstone_block
execute if block -11713 217 306 lever[face=floor,facing=west,powered=true] if block -11713 217 308 lever[face=floor,facing=west,powered=false] run setblock -11709 215 307 minecraft:redstone_block
execute if block -11713 217 306 lever[face=floor,facing=west,powered=false] if block -11713 217 308 lever[face=floor,facing=west,powered=true] run setblock -11709 215 307 minecraft:redstone_block
execute if block -11713 217 307 lever[face=floor,facing=west,powered=true] run setblock -11709 215 309 minecraft:redstone_block 
execute if block -11713 217 308 lever[face=floor,facing=west,powered=true] run setblock -11709 215 309 minecraft:redstone_block

execute unless score ta_lab_step Value matches 4 unless score ta_lab_step Value matches 7 run scoreboard players set ta_lab_step Value 0
execute if score ta_lab_step Value matches 4 if score ta_lab_safe_next_fluid Value matches 0 run scoreboard players set ta_lab_safe_next_fluid Value 3
