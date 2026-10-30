execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Polypthas","color":"#D47453"},{"text":"> Many of our neighbors and friends, good and honest people, became","color":"white"},{"text":" Germ Eaters ","color":"dark_aqua"},{"text":"and started doing violence in the name of the usurper! With all my actuarial experience, you'd think I'd be able to see it coming, but no.","color":"white"}]
execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Polypthas","color":"#D47453"},{"text":"> Many of our neighbors and friends, good and honest people, became","color":"white"},{"text":" Comedy Eaters ","color":"#D47453"},{"text":"and started making improv their entire personality! With all my actuarial experience, you'd think I'd be able to see it coming, but no.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
