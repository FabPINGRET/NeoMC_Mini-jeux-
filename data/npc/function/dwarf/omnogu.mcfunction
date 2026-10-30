execute positioned -333 60 -130 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -333 60 -130 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Omnogu","color":"dark_aqua"},{"text":"> We at the Bureau could spend all day weighing and measuring each other, teehee!","color":"white"}]

setblock -9768 80 420 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
