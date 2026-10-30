execute positioned 10468 60 119 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10468 60 119 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> I, Slime Man, have once again saved the day! Tales of my heroism will be told in","color":"white"},{"text":" Tanglevine","color":"green"},{"text":" for decades to come!","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/tanglevine/5 7s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
