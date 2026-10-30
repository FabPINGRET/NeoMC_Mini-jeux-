execute positioned -289 60 -49 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -289 60 -49 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Borgogu","color":"dark_aqua"},{"text":"> It's nearly impossible to weed out all the bone monsters disguised as dwarves. I don't believe you're one of them hero, but I know there are still at least a few within the city. Talk to","color":"white"},{"text":" The Tective","color":"dark_aqua"},{"text":" if you want to help, he's in his office and he thinks he's close to deducing who the last imposters are.","color":"white"}]
execute positioned -289 60 -49 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Borgogu","color":"dark_aqua"},{"text":"> Thank you for saving our city once again hero. Now if you'll excuse me, I have to sentence these two lovebirds to go on a date already.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
