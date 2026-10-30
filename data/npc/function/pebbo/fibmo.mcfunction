execute positioned 10120 187 1194 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10120 187 1194 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Fibmo Laa","color":"dark_purple"},{"text":"> This music? These songs? They are my life's work. I dare you to not weep at their deep, cutting beauty.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
