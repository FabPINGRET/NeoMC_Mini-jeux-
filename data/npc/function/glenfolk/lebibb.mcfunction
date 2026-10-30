execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"LeBibb","color":"aqua"},{"text":"> Food around ze","color":"white"},{"text":" Floaty Isles ","color":"yellow"},{"text":"can sometimes be hard to come by, so make sure you stock up, especially before attempting somezing dangerous! Most vendors will be happy to give you food","color":"white"},{"text":" once a day","color":"green"},{"text":". Zere is a ","color":"white"},{"text":"market ","color":"yellow"},{"text":"behind ze keep I suggest stopping at before leaving ze castle!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
