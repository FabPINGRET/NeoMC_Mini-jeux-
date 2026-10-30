execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.panda.cant_breed neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Zirinaj","color":"gold"},{"text":"> The world feels weirder than it once did. It's hard to believe there are other Isles out there.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
