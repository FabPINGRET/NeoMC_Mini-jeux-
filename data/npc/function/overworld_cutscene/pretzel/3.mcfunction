execute positioned 10520 43 -168 run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> I found it in my baby mama's backyard. Dug it out myself when she was at work. I haven't opened it yet, but, now that you're here, wanna open it together?","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/pretzel/4 11s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
