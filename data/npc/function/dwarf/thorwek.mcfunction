execute positioned -288 58 -179 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -288 58 -179 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Thorwek","color":"dark_aqua"},{"text":"> ","color":"white"},{"text":"Two of the other members","color":"dark_aqua"},{"text":" of the parks and rec department are out surveying the petrified trees around the city! We're trying to decide if any of the trees are good enough to designate as their own national park. I believe they're both investigating ","color":"white"},{"text":"trees near city gates","color":"dark_aqua"},{"text":".","color":"white"}]

setblock -9762 76 418 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
