execute positioned -10195 67 131 at @n[tag=pupufight,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned -10195 67 131 at @n[tag=pupufight,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute positioned -10195 67 131 at @n[tag=pupufight,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pupu-Nini","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Let's get out of here. I'm not sticking around, I'm going back to the","color":"white"},{"text":" jungle","color":"green"},{"text":" as fast as I can. Meet me there in front of the ","color":"white"},{"text":"Serpent King's Tomb","color":"green"},{"text":"!","color":"white","italic":false},{"text":" *tuk-nuk*","color":"gray","italic":true}]

execute positioned -10195 67 131 at @n[tag=pupufight,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

schedule function floaty:sched/npc/overworld_cutscene/zalvorn_intro/14 9s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
