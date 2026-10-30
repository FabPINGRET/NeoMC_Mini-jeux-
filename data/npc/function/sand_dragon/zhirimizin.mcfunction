execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.panda.cant_breed neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Zhirimizin the Recluse","color":"gold"},{"text":"> Why did meteors only land in our desert? Most Sand Dragons think it's some sort of punishment from the gods, but me? I think they're an inside job. The government is hiding giant space magnets under the sand, wake up sheeple.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
