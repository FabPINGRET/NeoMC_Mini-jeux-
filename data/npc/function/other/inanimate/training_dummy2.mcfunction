execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:item.armor.equip_leather neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Training Dummy","color":"aqua"},{"text":"> ","color":"white"},{"text":"...\nNobody here has tried to stab me or whack me with a blade! Is this normal? Maybe my standards were too low.","color":"gray","italic":true}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
