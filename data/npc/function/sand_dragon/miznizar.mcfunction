execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.panda.cant_breed neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Miznizar","color":"gold"},{"text":"> Our little oasis is all the water we'll ever need. Those ","color":"white"},{"text":"Gillmen ","color":"yellow"},{"text":"must be greedy to want so much water to themselves! I want to raise my son to be grateful for everything he has.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
