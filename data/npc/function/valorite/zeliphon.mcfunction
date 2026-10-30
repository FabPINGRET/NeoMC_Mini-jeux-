execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Zeliphon","color":"#D47453"},{"text":"> Before the ","color":"white"},{"text":"Germ Eaters","color":"dark_aqua"},{"text":" locked me up, I didn't even know that part of the prison building existed! I didn't realize prison was more than just merchandise and souvenirs. The world is full of crazy twists like that. There's a dark side to this whole prison gig you don't even see.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
