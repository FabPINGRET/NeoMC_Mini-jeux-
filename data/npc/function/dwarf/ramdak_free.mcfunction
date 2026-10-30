execute positioned -257 52 -164 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -257 52 -164 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Ramdak","color":"dark_aqua"},{"text":"> There were so many bugs in that jail, I was losing my little mind. Thank you for finding the real bone monsters so I could walk free.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
