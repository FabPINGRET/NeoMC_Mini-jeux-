execute positioned -8 53 1601 run playsound minecraft:entity.creaking.attack neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Knotfire","color":"green"},{"text":"> Come, by my grace I will make a husk of you, little sacrifice.","color":"white"},{"text":" ⇒","color":"light_purple"}]


schedule function floaty:sched/npc/overworld_cutscene/knotfire/2 7s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
