execute positioned 72 193 -2069 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 72 193 -2069 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Groor of the Silent Truth","color":"green"},{"text":"> The stones foretold your coming here, as they have foretold a great many things. We know more about recent events in the Isles than you may expect, Hero.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
