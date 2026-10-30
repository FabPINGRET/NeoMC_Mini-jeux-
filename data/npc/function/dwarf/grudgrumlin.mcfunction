execute positioned -286 41 -55 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute unless block -289 41 -57 air positioned -286 41 -55 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grudgrumlin","color":"dark_aqua"},{"text":"> This is terrible! I asked my ","color":"white"},{"text":"homunculus","color":"aqua"},{"text":" to get something from the pantry for me, and next thing I know there was a loud crash! Now the door is blocked by something heavy and won't open. There's ","color":"white"},{"text":"another way into the pantry","color":"aqua"},{"text":" we use to smuggle in rare ingredients from outside the city. If you could find it and make sure my homunculus is safe, I would be ","color":"white"},{"text":"very, very grateful","color":"red"},{"text":". This is all my fault...","color":"white"}]
execute if block -289 41 -57 air positioned -286 41 -55 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grudgrumlin","color":"dark_aqua"},{"text":"> You unblocked the door, and my homunculus is okay! Thank the stones for you, hero. You've made me ","color":"white"},{"text":"very, very happy","color":"red"},{"text":". Now I'm gonna go ask my homunculus why it smells like smoke in there...","color":"white"}]
execute if block -289 41 -57 air positioned -286 41 -55 run particle minecraft:heart ~ ~0.75 ~ 0.3 0.3 0.3 0 10 force
execute if block -289 41 -57 air run setblock -285 36 -59 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
