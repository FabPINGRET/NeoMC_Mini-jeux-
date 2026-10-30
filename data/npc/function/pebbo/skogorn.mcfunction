execute positioned 10069 187 1222 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10069 187 1222 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Skogorn the Broadwall","color":"blue"},{"text":"> Waking up with your squad is the best way to start the day. Starting the morning with a sleepy smile and a warm hug from each and every soldier in your unit is one of life's most special pleasures.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
