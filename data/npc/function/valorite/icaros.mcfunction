execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Icaros","color":"#D47453"},{"text":"> Hey, only Valorites are allowed to place bets! Rules are rules. And don't be a snitch, the authorities don't need to know about our sport down here, got it?","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
