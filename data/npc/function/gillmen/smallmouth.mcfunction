execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Smallmouth","color":"yellow"},{"text":"> There's a ","color":"white"},{"text":"creature in my basement ","color":"blue"},{"text":"who keeps rambling on and on about ","color":"white"},{"text":"boots","color":"blue"},{"text":" for some reason. Don't worry, I don't think he bites.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
