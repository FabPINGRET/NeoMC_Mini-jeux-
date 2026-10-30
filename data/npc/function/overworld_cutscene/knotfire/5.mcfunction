execute positioned -10697 71 89 run playsound minecraft:entity.creaking.attack neutral @a[tag=mg.flw] ~ ~ ~ 2 0.1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Knotfire","color":"green"},{"text":"> Thank you for your sacrifice...","color":"white"}]

schedule function floaty:sched/npc/overworld_cutscene/knotfire/6 7s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
