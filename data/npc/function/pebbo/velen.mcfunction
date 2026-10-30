execute positioned 31 193 -2092 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 31 193 -2092 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Velen of the Hushed Thrum","color":"green"},{"text":"> As a Cobblemancy side-project, I made a weapon from the ","color":"white"},{"text":"hardest stone imaginable","color":"aqua"},{"text":". It's up the ladder, you may need it.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
