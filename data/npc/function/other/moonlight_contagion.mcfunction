execute positioned 9960 59 14 run playsound minecraft:block.amethyst_block.fall neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute positioned 9960 59 14 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Moonlight Nexus","color":"aqua"},{"text":"> Ugh, the Botsicles. What a dreadful assignment. Every night, my","color":"white"},{"text":" life-giving curse","color":"aqua"},{"text":" is wasted on a bunch of walking tin cans who complain about flippers and tusks. I need ","color":"white"},{"text":"hosts who yearn to be transformed","color":"red"},{"text":". If you know such a people, I will follow you, but listen closely: once we're moving, you must ","color":"white"},{"text":"walk only on Waxwane Brick","color":"aqua"},{"text":". Step on anything else, and I'll slither straight back to this miserable tower. Understood? ","color":"white"},{"text":"Walk over to me","color":"aqua"},{"text":" when you want me to follow you.","color":"white"}]

setblock 9960 58 14 minecraft:polished_blackstone_pressure_plate

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
