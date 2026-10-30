execute positioned 10051 187 1242 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10051 187 1242 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Guldrok the Hammerjaw","color":"blue"},{"text":"> There are more Pebbos in the ","color":"white"},{"text":"Dark Isles","color":"dark_purple"},{"text":" than any other type of creature. Did you know that?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
