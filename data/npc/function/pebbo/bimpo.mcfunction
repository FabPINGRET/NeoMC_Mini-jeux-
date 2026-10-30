execute positioned 10101 187 1205 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10101 187 1205 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bimpo Withgrain","color":"dark_purple"},{"text":"> You'd think it would be hard to get wood here on the Isle of Silence, but that's not true. Long ago we managed to import one tree and that's lasted us for centuries.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
