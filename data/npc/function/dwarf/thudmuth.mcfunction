execute positioned -274 49 -140 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -274 49 -140 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Thudmuth","color":"dark_aqua"},{"text":"> We spent so much time and energy putting up defenses around the city but the","color":"white"},{"text":" bone contagion","color":"gray"},{"text":" forced itself in anyway. The might of the Dwarves is great, but I fear it may be waning.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
