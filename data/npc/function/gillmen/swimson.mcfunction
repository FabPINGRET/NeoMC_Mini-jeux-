execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Swimson","color":"yellow"},{"text":"> Here at the water factory, we take immense pride in the quality of our product. If the salt content isn't exactly right, the water won't make it past this room and it'll be sent back for reprocessing. After all, we live surrounded by the stuff! It's gotta be perfect.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
