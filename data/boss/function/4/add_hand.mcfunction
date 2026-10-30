execute if block -10041 95 -338 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","1","exclude"]}
execute if block -10041 95 -340 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","2","exclude"]}
execute if block -10041 95 -342 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","3","exclude"]}
execute if block -10041 95 -344 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","4","exclude"]}
execute if block -10041 95 -346 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","5","exclude"]}
execute if block -10041 95 -348 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","6","exclude"]}
execute if block -10041 95 -350 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","7","exclude"]}
execute if block -10041 95 -352 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","8","exclude"]}
execute if block -10041 95 -354 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","9","exclude"]}
execute if block -10041 95 -356 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","10","exclude"]}
execute if block -10041 95 -358 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","11","exclude"]}
execute if block -10041 95 -360 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","12","exclude"]}
execute if block -10041 95 -362 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","13","exclude"]}
execute if block -10041 95 -364 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","14","exclude"]}
execute if block -10041 95 -366 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","15","exclude"]}
execute if block -10041 95 -368 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","16","exclude"]}
execute if block -10041 95 -370 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","17","exclude"]}
execute if block -10041 95 -372 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","18","exclude"]}
execute if block -10041 95 -374 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","19","exclude"]}
execute if block -10041 95 -376 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","20","exclude"]}
execute if block -10041 95 -378 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","21","exclude"]}
execute if block -10041 95 -380 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","22","exclude"]}
execute if block -10041 95 -382 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","23","exclude"]}
execute if block -10041 95 -384 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","24","exclude"]}
execute if block -10041 95 -386 air run summon area_effect_cloud ~ ~ ~ {Tags:["hand_temp","25","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=hand_temp,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=hand_temp,tag=exclude,distance=0..]

execute if entity @e[tag=hand_temp,tag=1,distance=0..] run setblock -10041 95 -338 redstone_block
execute if entity @e[tag=hand_temp,tag=2,distance=0..] run setblock -10041 95 -340 redstone_block
execute if entity @e[tag=hand_temp,tag=3,distance=0..] run setblock -10041 95 -342 redstone_block
execute if entity @e[tag=hand_temp,tag=4,distance=0..] run setblock -10041 95 -344 redstone_block
execute if entity @e[tag=hand_temp,tag=5,distance=0..] run setblock -10041 95 -346 redstone_block
execute if entity @e[tag=hand_temp,tag=6,distance=0..] run setblock -10041 95 -348 redstone_block
execute if entity @e[tag=hand_temp,tag=7,distance=0..] run setblock -10041 95 -350 redstone_block
execute if entity @e[tag=hand_temp,tag=8,distance=0..] run setblock -10041 95 -352 redstone_block
execute if entity @e[tag=hand_temp,tag=9,distance=0..] run setblock -10041 95 -354 redstone_block
execute if entity @e[tag=hand_temp,tag=10,distance=0..] run setblock -10041 95 -356 redstone_block
execute if entity @e[tag=hand_temp,tag=11,distance=0..] run setblock -10041 95 -358 redstone_block
execute if entity @e[tag=hand_temp,tag=12,distance=0..] run setblock -10041 95 -360 redstone_block
execute if entity @e[tag=hand_temp,tag=13,distance=0..] run setblock -10041 95 -362 redstone_block
execute if entity @e[tag=hand_temp,tag=14,distance=0..] run setblock -10041 95 -364 redstone_block
execute if entity @e[tag=hand_temp,tag=15,distance=0..] run setblock -10041 95 -366 redstone_block
execute if entity @e[tag=hand_temp,tag=16,distance=0..] run setblock -10041 95 -368 redstone_block
execute if entity @e[tag=hand_temp,tag=17,distance=0..] run setblock -10041 95 -370 redstone_block
execute if entity @e[tag=hand_temp,tag=18,distance=0..] run setblock -10041 95 -372 redstone_block
execute if entity @e[tag=hand_temp,tag=19,distance=0..] run setblock -10041 95 -374 redstone_block
execute if entity @e[tag=hand_temp,tag=20,distance=0..] run setblock -10041 95 -376 redstone_block
execute if entity @e[tag=hand_temp,tag=21,distance=0..] run setblock -10041 95 -378 redstone_block
execute if entity @e[tag=hand_temp,tag=22,distance=0..] run setblock -10041 95 -380 redstone_block
execute if entity @e[tag=hand_temp,tag=23,distance=0..] run setblock -10041 95 -382 redstone_block
execute if entity @e[tag=hand_temp,tag=24,distance=0..] run setblock -10041 95 -384 redstone_block
execute if entity @e[tag=hand_temp,tag=25,distance=0..] run setblock -10041 95 -386 redstone_block

kill @e[type=minecraft:area_effect_cloud,tag=hand_temp,distance=0..]
