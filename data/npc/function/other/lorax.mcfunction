execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.8

execute if score lorax bool matches 1 run setblock -99 54 -228 redstone_block

execute if block -99 54 -228 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"The Lorax","color":"#fc8403"},{"text":"> I am the Lorax who speaks for the trees, which they seem to be chopping as fast as they please! All I want is to live on a ","color":"white"},{"text":"nice, comfortable stump ","color":"green"},{"text":"somewhere trees are respected and allowed to grow. Somewhere ","color":"white"},{"text":"far away from Bugboy Forest","color":"green"},{"text":". If you can tell me about such a place, it would make me a ","color":"white"},{"text":"very, very happy","color":"red"},{"text":" Lorax.","color":"white"}]

execute unless block -99 54 -228 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"The Lorax","color":"#fc8403"},{"text":"> You found a ","color":"white"},{"text":"nice, comfortable stump ","color":"green"},{"text":"for me? Somewhere ","color":"white"},{"text":"far away from Bugboy Forest","color":"green"},{"text":"? Incredible! I'll head there right away. You've made me a ","color":"white"},{"text":"very, very happy","color":"red"},{"text":" Lorax.","color":"white"}]
execute unless block -99 54 -228 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.2 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
