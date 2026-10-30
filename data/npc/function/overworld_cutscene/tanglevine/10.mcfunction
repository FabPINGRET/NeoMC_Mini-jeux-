setblock 10470 54 120 air

execute positioned 10468 60 119 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10468 60 119 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> Leaving a slick trail of justice, Slime Man out!","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute positioned 10468 60 119 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:item.chorus_fruit.teleport neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute positioned 10468 60 119 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run particle minecraft:sneeze ~ ~ ~ 0.1 0.1 0.1 0.05 100 force @a[tag=mg.flw]

tp @n[tag=slime_man_tanglevine,distance=0..] 10468 53 119 0 0
tp @n[tag=puppet_tanglevine,distance=0..] 10469.5 52.66 119.5

stopsound @a[tag=mg.flw] record

schedule function floaty:sched/npc/overworld_cutscene/tanglevine/11 5s




#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
