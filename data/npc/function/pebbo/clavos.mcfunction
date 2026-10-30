execute positioned 10124 174 1330 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10124 174 1330 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Clavos the Faithful","color":"red"},{"text":"> His majesty often comes here to blow off steam with some rough-and-tumble fun. Some spirited, boisterous play. Yes, that's just what the King needs sometimes! Some capers and shenanigans. Some harmless roughhousing and buffoonery, yes that's what he needs!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
