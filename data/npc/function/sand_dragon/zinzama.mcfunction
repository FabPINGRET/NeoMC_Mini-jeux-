execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.panda.cant_breed neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Tomb Guard Zinzama","color":"gold"},{"text":"> This noble tomb was struck by a firey meteor, which we thought would surely wake the dead within. As it turns out, the last dynasty of kings buried here couldn't have cared less about their slumber being disturbed, so the","color":"white"},{"text":" Viceroy","color":"gold"},{"text":" turned their final resting place into his throne room. We Sand Dragons do not respect the dead who do not respect themselves.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
