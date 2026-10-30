execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_bread_0,tag=mg.flw] [{"text":"<"},{"text":"Thalpius","color":"aqua"},{"text":"> Here, take some of these! Fresh baked just this morning! Best bread you're gonna find!","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_bread_0,tag=mg.flw] [{"text":"<"},{"text":"Thalpius","color":"aqua"},{"text":"> You've gotta give the dough some time to rise! Come back tomorrow.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_bread_0,tag=mg.flw] bread 10
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_bread_0,tag=mg.flw] add vendor_bread_0


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
