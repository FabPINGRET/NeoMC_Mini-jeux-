execute positioned 10520 43 -168 run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> Whoa, haha! I, too, am a collector of Items! A peddler of powerful oddments, that's me! I've recently come into the possession of a ","color":"white"},{"text":"relic","color":"red"},{"text":" more prized than any in my entire Miscellany-topia.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/pretzel/2 13s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
