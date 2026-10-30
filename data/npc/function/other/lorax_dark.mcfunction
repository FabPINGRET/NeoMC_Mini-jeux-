execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.8

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"The Lorax","color":"#fc8403"},{"text":"> I am the Lorax who speaks for the trees, and here they grow happy and tall as they please! You've made me a ","color":"white"},{"text":"very, very happy","color":"red"},{"text":" Lorax by telling me about this place.","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.2 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
