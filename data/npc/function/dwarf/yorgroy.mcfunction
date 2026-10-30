execute positioned -363 59 -113 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -363 59 -113 run tellraw @a[distance=..10,tag=!vendor_arrow_3,tag=mg.flw] [{"text":"<"},{"text":"Yorgroy","color":"dark_aqua"},{"text":"> Fresh baked arrows! Haha just messin around a little bit, just messin around.","color":"white"}]
execute positioned -363 59 -113 run tellraw @a[distance=..10,tag=vendor_arrow_3,tag=mg.flw] [{"text":"<"},{"text":"Yorgroy","color":"dark_aqua"},{"text":"> Sorry bub, you've got the look of someone I've already given arrows to today.","color":"white"}]

execute positioned -363 59 -113 run give @a[distance=..10,tag=!vendor_arrow_3,tag=mg.flw] arrow 12
execute positioned -363 59 -113 run tag @a[distance=..10,tag=!vendor_arrow_3,tag=mg.flw] add vendor_arrow_3


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
