execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Professor Whoosh","color":"#D47453"},{"text":"> My Dirigable is working! This marvel of technology I've created will usher in a new age of prosperity for ","color":"white"},{"text":"Valorforge","color":"red"},{"text":". The ultimate goal is to figure out a way to scale it down for personal use at birthday parties and baby showers and the like.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
