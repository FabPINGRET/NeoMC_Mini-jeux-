execute positioned 214 43 112 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned 214 43 112 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute positioned 214 43 112 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Pupu-Nini","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"But I'm not a puppet! I'm a person!","color":"white","italic":false},{"text":" *tuk-nuk*","color":"gray","italic":true},{"text":" ⇒","color":"light_purple"}]

execute positioned 214 43 112 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

schedule function floaty:sched/npc/overworld_cutscene/zalvorn_intro/2 6s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
