execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Araxion","color":"#D47453"},{"text":"> Whenever I can't figure out what I need to do next, I talk to the Lords. They are usually able to point me in the right direction! Wink wink, nudge nudge, gamer advice right there.\n\nOh, were you interested in renting a fire?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
