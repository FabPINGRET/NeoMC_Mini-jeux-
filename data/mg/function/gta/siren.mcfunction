# @s est recherché : sirène (deux tons) et lumières
scoreboard players operation $gs mg.st = $gtt mg.st
scoreboard players set #40 mg.st 40
scoreboard players operation $gs mg.st %= #40 mg.st
execute if score $gs mg.st matches 0 run playsound minecraft:block.note_block.bell hostile @a ~ ~ ~ 1.2 1.4
execute if score $gs mg.st matches 20 run playsound minecraft:block.note_block.bell hostile @a ~ ~ ~ 1.2 1.0
execute if score @s mg.gwl matches 3.. run particle minecraft:dust{color:[0.1,0.3,1.0],scale:1.5} ~ ~2.4 ~ 0.3 0.1 0.3 0 3
execute if score @s mg.gwl matches 3.. run particle minecraft:dust{color:[1.0,0.1,0.1],scale:1.5} ~ ~2.4 ~ 0.3 0.1 0.3 0 3
