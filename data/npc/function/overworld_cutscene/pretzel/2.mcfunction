execute positioned 10520 43 -168 run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> I'm actually warming its lid with my little buns right now! It's called ","color":"white"},{"text":"The Inviolable Barrel of One Billion Crud","color":"red"},{"text":".","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/pretzel/3 10s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
