execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score BetterEconomy bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Plini-Oko","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Trade has been slow in the jungle. If I had meat to offer, you'd know by the smell.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]
execute if score BetterEconomy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_rabbit_0,tag=mg.flw] [{"text":"<"},{"text":"Plini-Oko","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Fresh, spit-roasted meat for you! It's hard to chew this stuff with our woody teeth. Hopefully you have an easier time with it.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]
execute if score BetterEconomy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_rabbit_0,tag=mg.flw] [{"text":"<"},{"text":"Plini-Oko","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Hey, spit-roasting takes a while, ok? First you have to soak the meat in a bucket of spit, then you roast it! Come back tomorrow, I have a lot of spitting left to do today and my mouth is already dry.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute if score BetterEconomy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_rabbit_0,tag=mg.flw] cooked_rabbit 12
execute if score BetterEconomy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_rabbit_0,tag=mg.flw] add vendor_rabbit_0

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
