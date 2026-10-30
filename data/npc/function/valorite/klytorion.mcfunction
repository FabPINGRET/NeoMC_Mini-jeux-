execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Klytorion","color":"#D47453"},{"text":"> I'm these Simpletoids's trainer. Teaching them to race is more stick than carrot most days, but Simpletoids don't respond well to positive reinforcement. It's entertaining watching the little guys wheeling around, so that makes it okay.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
