execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if block 10466 53 120 minecraft:red_wool positioned 10468 59 121 if entity @a[gamemode=!spectator,distance=8..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Pupu-Nini","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Please ","color":"white"},{"text":"gather everyone","color":"green"},{"text":" here, I would like to thank you all myself...","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute if block 10466 53 120 minecraft:blue_wool if score Inventory TomeOfTongues matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Pupu-Nini","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Good luck in there! I'm afraid rescuing the ","color":"white"},{"text":"Lord of Forest ","color":"green"},{"text":"won't be as easy as it was to rescue me...","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute if block 10466 53 120 minecraft:blue_wool if score Inventory TomeOfTongues matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Pupu-Nini","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"You're amazing! Talking to you is quite the pygmy-up. Hah! Pygmy pun.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute if block 10466 53 120 minecraft:red_wool positioned 10468 59 121 if entity @a[gamemode=!spectator,distance=..8,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=8..,tag=mg.flw] run function npc:overworld_cutscene/tanglevine/0

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

execute positioned 10466 62 121 run kill @n[tag=quest_marker,distance=..3]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
