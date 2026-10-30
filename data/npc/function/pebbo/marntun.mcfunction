execute positioned 10098 188 1309 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10098 188 1309 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Marntun the Shieldsplitter","color":"blue"},{"text":"> Don't even THINK about doing a murder in there. I'm dead serious, I will GET you if you do.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
