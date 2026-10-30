execute positioned -238 39 -182 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -238 39 -182 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dussok","color":"dark_aqua"},{"text":"> It's a bad idea for outsiders to be wandering around here. We don't even let","color":"white"},{"text":" fire golems","color":"red"},{"text":" in for stones' sake, and we usually love those guys!","color":"white"}]
execute positioned -238 39 -182 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dussok","color":"dark_aqua"},{"text":"> It's good to feel less isolated from the rest of the Isles again. I hope our","color":"white"},{"text":" fire golems","color":"red"},{"text":" neighbors can forgive our self-absorption. I'm sure they would have loved to come to our aid in defeating the","color":"white"},{"text":" bone contagion","color":"gray"},{"text":", but we were too stubborn and suspicious to let them.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
