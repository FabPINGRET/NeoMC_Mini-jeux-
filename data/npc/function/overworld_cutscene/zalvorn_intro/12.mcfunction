execute positioned -10195 67 131 at @n[tag=pupufight,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned -10195 67 131 at @n[tag=pupufight,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pupu-Nini","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Haha! I got him! All the puppets were taken to this awful place and I was brought here with them.","color":"white","italic":false},{"text":" *tuk-nuk*","color":"gray","italic":true},{"text":" ⇒","color":"light_purple"}]

execute positioned -10195 67 131 at @n[tag=pupufight,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

schedule function floaty:sched/npc/overworld_cutscene/zalvorn_intro/13 9s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
