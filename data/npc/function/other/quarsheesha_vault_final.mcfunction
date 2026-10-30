execute positioned 100 47 33 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 100 47 33 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Quarsheesha","color":"aqua"},{"text":"> All of the vault doors are open! Wow! Though... I would stay far away from that last one. Horrible chills ran through my body as soon as it opened.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
