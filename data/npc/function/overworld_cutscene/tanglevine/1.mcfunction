execute positioned 10466 60 121 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned 10466 60 121 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute positioned 10466 60 121 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pupu-Nini","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"That’s the last time I go to your world. Lesson learned the hard way! Now, you want to enter the tomb? Let me say the chant of unsealing...","color":"white","italic":false},{"text":" *tuk-nuk*","color":"gray","italic":true},{"text":" ⇒","color":"light_purple"}]

execute positioned 10466 60 121 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

schedule function floaty:sched/npc/overworld_cutscene/tanglevine/2 12s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
