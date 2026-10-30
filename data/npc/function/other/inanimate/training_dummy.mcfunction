execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:item.armor.equip_leather neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute if score mr_nippy bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Training Dummy","color":"aqua"},{"text":"> ","color":"white"},{"text":"...\nAh, you're not hitting me. Thanks.","color":"gray","italic":true}]

execute if score mr_nippy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Training Dummy","color":"aqua"},{"text":"> ","color":"white"},{"text":"...\nA new club? And I'm invited? I'll head over now!","color":"gray","italic":true}]

execute if score mr_nippy bool matches 1 run setblock -99 53 205 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
