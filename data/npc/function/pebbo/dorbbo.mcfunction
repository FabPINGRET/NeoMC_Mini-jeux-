execute positioned 10123 180 1282 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10123 180 1282 run tellraw @a[distance=..10,tag=!vendor_pumpkin_pie_0,tag=mg.flw] [{"text":"<"},{"text":"Dorbbo Cointuck","color":"yellow"},{"text":"> I tried to start a business growing these pies with the magic circle and then reselling them at a ludicrous price, but the King put a stop to it.","color":"white"}]
execute positioned 10123 180 1282 run tellraw @a[distance=..10,tag=vendor_pumpkin_pie_0,tag=mg.flw] [{"text":"<"},{"text":"Dorbbo Cointuck","color":"yellow"},{"text":"> Come back tomorrow when I've had time to bake more pies!","color":"white"}]

execute positioned 10123 180 1282 run give @a[distance=..10,tag=!vendor_pumpkin_pie_0,tag=mg.flw] pumpkin_pie 10
execute positioned 10123 180 1282 run tag @a[distance=..10,tag=!vendor_pumpkin_pie_0,tag=mg.flw] add vendor_pumpkin_pie_0


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
