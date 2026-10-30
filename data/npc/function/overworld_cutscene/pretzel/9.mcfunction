spawnpoint @a[tag=mg.flw] 10525 42 -168 90 0
scoreboard players set $flsp mg.st 34

execute positioned 10520 43 -168 run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> I'm going to set up shop ","color":"white"},{"text":"somewhere else","color":"dark_aqua"},{"text":". I'll pre-admire all the crud in the barrel, and if you ever want any just let me know.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/pretzel/10 13s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
