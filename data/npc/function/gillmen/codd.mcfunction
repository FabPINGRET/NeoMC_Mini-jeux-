execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_bread_4,tag=mg.flw] [{"text":"<"},{"text":"Codd","color":"yellow"},{"text":"> Arrows still work underwater! Sorta. I'll throw in some rations for you as well.","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_bread_4,tag=mg.flw] [{"text":"<"},{"text":"Codd","color":"yellow"},{"text":"> We need to ration everything, come back tomorrow for more.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_bread_4,tag=mg.flw] bread 24
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_bread_4,tag=mg.flw] arrow 24
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_bread_4,tag=mg.flw] add vendor_bread_4


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
