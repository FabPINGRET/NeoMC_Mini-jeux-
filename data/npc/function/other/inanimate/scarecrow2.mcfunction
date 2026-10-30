execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:item.armor.equip_leather neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Scarecrow","color":"gold"},{"text":"> ","color":"white"},{"text":"...\nMy fate is still to be a scarecrow. But that doesn't mean I can't also be an attractfriend.","color":"gray","italic":true}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
