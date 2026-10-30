execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7
execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mythania","color":"#D47453"},{"text":"> If you're here to file a Property Burgled by a Cultist claim, we'll be with you in a moment. I should also inform you that our life insurance policies no longer cover death by exploding.","color":"white"}]
execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mythania","color":"#D47453"},{"text":"> If you're here to file a Property Burgled by a Comedian claim, we'll be with you in a moment. I should also inform you that our life insurance policies no longer cover death by exploding.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
