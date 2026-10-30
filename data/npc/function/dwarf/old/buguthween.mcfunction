execute positioned -302 57 -45 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -302 57 -45 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Buguthween","color":"dark_aqua"},{"text":"> I'm assessing the health of this chree. Hm, what's that? Haha no, I'm pretty sure it's \"chree,\" I'm pretty sure it is. Listen to yourself talk before you embarrass yourself next time haha.","color":"white"}]

setblock -9762 76 428 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
