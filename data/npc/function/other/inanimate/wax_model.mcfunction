execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:item.armor.equip_leather neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute if score mr_nippy bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wax Model","color":"green"},{"text":"> ","color":"white"},{"text":"...\nThe sign says no touching. Sadly, people always interpret that to include no hugging. I am very alone.","color":"gray","italic":true}]

execute if score mr_nippy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wax Model","color":"green"},{"text":"> ","color":"white"},{"text":"...\nSomeone wants to spend time with me? I'm going right away.","color":"gray","italic":true}]
execute if score mr_nippy bool matches 1 run setblock 9940 52 -175 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
