execute positioned 134 193 -2065 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 134 193 -2065 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Solor of the Worm's Song","color":"green"},{"text":"> When all 6 of these statues are turned so that they ","color":"white"},{"text":"directly face the Shrunken Temple's hiding place","color":"green"},{"text":", the seal will open and you will be able to retrieve it.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
