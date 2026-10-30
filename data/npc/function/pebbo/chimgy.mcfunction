execute positioned 10121 180 1276 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10121 180 1276 run tellraw @a[distance=..10,tag=!vendor_arrow_6,tag=mg.flw] [{"text":"<"},{"text":"Chimgy Haggletop","color":"yellow"},{"text":"> Arrows are pretty easy to make. Just tie some fuzz and a grain of sand to a splinter!","color":"white"}]
execute positioned 10121 180 1276 run tellraw @a[distance=..10,tag=vendor_arrow_6,tag=mg.flw] [{"text":"<"},{"text":"Chimgy Haggletop","color":"yellow"},{"text":"> I'm fresh outta fuzz, gotta collect some more before I can give you more arrows.","color":"white"}]

execute positioned 10121 180 1276 run give @a[distance=..10,tag=!vendor_arrow_6,tag=mg.flw] arrow 24
execute positioned 10121 180 1276 run tag @a[distance=..10,tag=!vendor_arrow_6,tag=mg.flw] add vendor_arrow_6


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
