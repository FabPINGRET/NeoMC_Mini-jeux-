execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_arrow_2,tag=mg.flw] [{"text":"<"},{"text":"Carper","color":"yellow"},{"text":"> I keep finding these pointy things floating around. I get the sense that they're probably more useful in the open air than underwater, so I'll give them to you!","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_arrow_2,tag=mg.flw] [{"text":"<"},{"text":"Carper","color":"yellow"},{"text":"> If I find any more of these, you can have them.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_arrow_2,tag=mg.flw] arrow 24
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_arrow_2,tag=mg.flw] add vendor_arrow_2


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
