execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Cavier","color":"yellow"},{"text":"> Everyone here works to support the Gill Guild in one form or another. We at the Ishbowl Offices oversee the operation of the","color":"white"},{"text":" Water Factory","color":"blue"},{"text":", as well as keep the peace around the city. That way, ","color":"white"},{"text":"Papa Seamonster","color":"yellow"},{"text":" can focus on important things like investigating how to reclaim","color":"white"},{"text":" Bubble Lake ","color":"blue"},{"text":"from the monsters!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
