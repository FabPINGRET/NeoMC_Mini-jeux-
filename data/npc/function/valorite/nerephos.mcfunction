execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Nerephos","color":"#D47453"},{"text":"> We're your one-stop law shop for everything related to personal injury, family matters, and horse felonies. If you're ever harmed by negligence, planning to adopt, or are accused of selling an anemic horse with chewing disease, we're your guys!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
