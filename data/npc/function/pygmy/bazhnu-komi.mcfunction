execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score zalvorn Story matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bazhnu-Komi","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"We're hard at work coming up with a magical dance!","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute if score zalvorn Story matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bazhnu-Komi","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Our dance is ready! Dancers, let's reach deep into our spirits and discover where Pupu-Nini went! And-a-one, and-a-two...","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]
execute if score zalvorn Story matches 1 run setblock 10410 31 167 air
execute if score zalvorn Story matches 1 run schedule function floaty:sched/main_quest/pygmy_dance_start 6s

execute if score zalvorn Story matches 2 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bazhnu-Komi","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"The","color":"white"},{"text":" first Pygmy you saw ","color":"green"},{"text":"when you came to the jungle knows something about where Pupu-Nini went! Go now, Pupu-Nini must be rescued!","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute if score zalvorn Story matches 3.. at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bazhnu-Komi","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"We are glad our dance was able to aid you!","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]


execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose
execute as @e[tag=pygmy,tag=dancer,tag=!leader,distance=0..] run data modify entity @s Pose set from entity @n[tag=dancer,tag=pygmy,tag=leader,distance=0..] Pose

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
