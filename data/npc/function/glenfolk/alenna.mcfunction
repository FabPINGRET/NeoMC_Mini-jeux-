execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_carrot_0,tag=mg.flw] [{"text":"<"},{"text":"Alenna","color":"aqua"},{"text":"> ","color":"white"},{"text":"*mmmunch* *crunch* *crunch*","color":"gray","italic":true},{"text":" Hi!","color":"white","italic":false},{"text":" *gulp*","color":"gray","italic":true},{"text":" I'm just in here eating some ingredients! Here, have some!","color":"white","italic":false},{"text":" *crunch* *munch*","color":"gray","italic":true}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_carrot_0,tag=mg.flw] [{"text":"<"},{"text":"Alenna","color":"aqua"},{"text":"> *munch* *smack*","color":"gray","italic":true},{"text":" Hey!","color":"white","italic":false},{"text":" *gulp*","color":"gray","italic":true},{"text":" Didn't I already give you some of these today? If we take toooooooo much, someone will notice!","color":"white","italic":false},{"text":" *cronch* *munch* *munch*","color":"gray","italic":true}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_carrot_0,tag=mg.flw] carrot 10
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_carrot_0,tag=mg.flw] add vendor_carrot_0

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
