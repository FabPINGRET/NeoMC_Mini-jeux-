execute if score golem_lycan bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.ravager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute if score golem_lycan bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.breeze.deflect neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score golem_lycan bool matches 0 if score moonlight_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Krokub","color":"red"},{"text":"> We used to all live in houses, but we tore them down for the materials to build the Supplicants you see around the","color":"white"},{"text":" Magma Kingdom","color":"red"},{"text":". They ensure that no matter where the Sun is on its journey across the sky, it is being rightfully honored.","color":"white"}]
execute if score golem_lycan bool matches 0 if score moonlight_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Krokub","color":"red"},{"text":"> We used to all live in houses, but we tore them down for the materials to build the Supplicants you see around the ","color":"white"},{"text":"Magma Kingdom","color":"red"},{"text":". They ensure that no matter where the Moon is on its journey across the sky, it is being rightfully honored.","color":"white"}]

execute if score golem_lycan bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Krokubax","color":"red"},{"text":"> I've re-dedicated each of the Supplicant statues from the Sun to the Moon.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
