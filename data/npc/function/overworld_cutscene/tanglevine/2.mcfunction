execute positioned 10468 60 119 run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10468 60 119 run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"green"},{"text":"> I've done it! I've rescued the missing Pygmy!","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/tanglevine/3 3s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
