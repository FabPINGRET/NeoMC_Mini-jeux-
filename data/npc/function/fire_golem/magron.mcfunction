execute if score golem_lycan bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.ravager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute if score golem_lycan bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.breeze.deflect neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score golem_lycan bool matches 0 if score moonlight_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Magron","color":"red"},{"text":"> We pray that one day, new ","color":"white"},{"text":"Fire Golems ","color":"red"},{"text":"will be begotten, not constructed. We pray that one day, ","color":"white"},{"text":"Fire Golems","color":"red"},{"text":" will be golems no more.","color":"white"}]
execute if score golem_lycan bool matches 0 if score moonlight_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Magron","color":"red"},{"text":"> Even though the Sun has turned its eye away from us, the Moon has heard our prayers. Through moonlight, we become alive!","color":"white"}]

execute if score golem_lycan bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Magronex","color":"red"},{"text":"> Under the Moon's cold light, our deepest desire has been fulfilled! Life is better than I could have ever hoped for.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
