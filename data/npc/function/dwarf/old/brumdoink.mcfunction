execute positioned -211 58 -93 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -211 58 -93 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brumdoink","color":"dark_aqua"},{"text":"> Each tree is special, each has its own magical charm! I love trees, from the old giants in","color":"white"},{"text":" Bugboy Forest","color":"green"},{"text":" to the weird, purple, gossamer ones all over the ","color":"white"},{"text":"Warped Lands","color":"light_purple"},{"text":".","color":"white"}]

setblock -9762 76 426 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
