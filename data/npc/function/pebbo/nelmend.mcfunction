execute positioned 127 193 -2056 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 127 193 -2056 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Nelmend of the Sunken Rite","color":"green"},{"text":"> One day, we will return to our home. When the stones send for us, we will return. There is still much to learn from the magic of the ","color":"white"},{"text":"Bell","color":"gold"},{"text":".","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
