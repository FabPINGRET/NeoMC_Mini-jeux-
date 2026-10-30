execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.panda.cant_breed neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Ravazatzi","color":"gold"},{"text":"> It turns out that these ","color":"white"},{"text":"meteors","color":"gold"},{"text":" which have crashed into our desert are a phenomenal source of ","color":"white"},{"text":"high-quality iron","color":"gold"},{"text":". When it melts, the slag and impurities float to the top. All we have to do then is pour off the top layer so the iron can be as pure as possible.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
