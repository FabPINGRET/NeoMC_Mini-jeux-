execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Calyrios","color":"#D47453"},{"text":"> This is the ","color":"white"},{"text":"Germ Eaters'","color":"dark_aqua"},{"text":" storeroom. If only there was a way inside, I'd storm in and give 'em a piece of my mind! Oh well, I can't see any possible way to get in, can you?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
