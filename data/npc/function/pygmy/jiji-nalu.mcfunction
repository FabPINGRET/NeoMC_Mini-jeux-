execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_melon_0,tag=mg.flw] [{"text":"<"},{"text":"Jiji-Nalu","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Here's one entire melon! I cut it into 19 equal pieces for you. This way they're all the perfect thickness! You'll never cut a melon any other way after this, thank me later.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_melon_0,tag=mg.flw] [{"text":"<"},{"text":"Jiji-Nalu","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Hungry for more? I don't blame you. The other melons here are reserved for other customers for today, sorry.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_melon_0,tag=mg.flw] melon_slice 19
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_melon_0,tag=mg.flw] add vendor_melon_0

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
