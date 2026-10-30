execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Pyrron","color":"#D47453"},{"text":"> I'm 3.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
