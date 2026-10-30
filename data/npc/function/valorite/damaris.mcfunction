execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7
execute if block 9981 49 -160 minecraft:ancient_debris at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Damaris","color":"#D47453"},{"text":"> We're trying to dig a tunnel into the prison to free our friends who were arrested by the ","color":"white"},{"text":"Germ Eaters","color":"dark_aqua"},{"text":". We could keep digging from the prison into the basement of ","color":"white"},{"text":"Valor Tower","color":"red"},{"text":", but one thing at a time.","color":"white"}]
execute if block 9981 49 -160 minecraft:air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Damaris","color":"#D47453"},{"text":"> The tunnel to the prison is complete!","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
