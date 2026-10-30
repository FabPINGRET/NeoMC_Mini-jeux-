execute positioned -363 59 -101 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -363 59 -101 run tellraw @a[distance=..10,tag=!vendor_bread_2,tag=mg.flw] [{"text":"<"},{"text":"Boroguerm","color":"dark_aqua"},{"text":"> Bread for you, pal! Baked fresh on hot rocks every day!","color":"white"}]
execute positioned -363 59 -101 run tellraw @a[distance=..10,tag=vendor_bread_2,tag=mg.flw] [{"text":"<"},{"text":"Boroguerm","color":"dark_aqua"},{"text":"> Here's some more bread! Take it, it's... oh, oops, I dropped it. That's ok, I'll start making more.","color":"white"}]

execute positioned -363 59 -101 run give @a[distance=..10,tag=!vendor_bread_2,tag=mg.flw] bread 10
execute positioned -363 59 -101 run tag @a[distance=..10,tag=!vendor_bread_2,tag=mg.flw] add vendor_bread_2


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
