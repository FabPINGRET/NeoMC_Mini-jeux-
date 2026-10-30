execute positioned -10341 89 445 run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> Ok, I get it, I got a little carried away.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/pretzel/8 6s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
