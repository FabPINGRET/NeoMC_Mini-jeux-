execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:item.armor.equip_leather neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wax Model","color":"green"},{"text":"> ","color":"white"},{"text":"...\nIn a place this cold, my wax will never melt! I get plenty of hugs here too.","color":"gray","italic":true}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
