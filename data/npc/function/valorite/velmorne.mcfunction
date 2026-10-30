execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Velmorne","color":"#D47453"},{"text":"> Ah, a visitor! I am the hug facilitator here at Lullaby Meadow, though I have experience in smile coaching as well. As you can see, our ","color":"white"},{"text":"sole resident ","color":"blue"},{"text":"is in dire need of some good old-fashioned wellness, so please don't bother him. Stop by anytime to use our spa, it's the brown puddle by the wall there.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
