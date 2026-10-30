execute positioned -11655 183 -186 run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned -11655 183 -186 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Papa Gnöb","color":"red"},{"text":"> How's it goin, buh'? Hey, listen, could you take the key from the chest there on your way out? Long story, don't want to explain it, but I don't like having it here. Thanks, cutie. ","color":"white"},{"text":"*smooch*","color":"gray","italic":true}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
