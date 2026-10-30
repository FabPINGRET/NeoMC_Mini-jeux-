execute positioned 10102 187 1218 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10102 187 1218 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Plimble Meltwick","color":"dark_purple"},{"text":"> Every candle here in the Petrified Kingdom was made right here in my workshop! They've really caught on. I'm very prolific.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
