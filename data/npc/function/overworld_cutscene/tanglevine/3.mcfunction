tp @n[tag=slime_man_tanglevine,distance=0..] 10468 59 119 0 0
tp @n[tag=puppet_tanglevine,distance=0..] 10469.5 58.66 119.5

execute positioned 10468 60 119 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:item.chorus_fruit.teleport neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute positioned 10468 60 119 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run particle minecraft:sneeze ~ ~ ~ 0.1 0.1 0.1 0.05 100 force @a[tag=mg.flw]



schedule function floaty:sched/npc/overworld_cutscene/tanglevine/4 3s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
