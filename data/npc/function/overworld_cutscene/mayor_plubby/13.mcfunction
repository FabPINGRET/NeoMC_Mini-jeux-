setblock 10385 55 -221 air

execute positioned 10386 59 -219 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2

execute positioned 10386 59 -219 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:item.chorus_fruit.teleport neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute positioned 10386 59 -219 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run particle minecraft:sneeze ~ ~ ~ 0.1 0.1 0.1 0.05 100 force @a[tag=mg.flw]

execute positioned 10386 59 -219 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> Leaving a slick trail of justice,","color":"white"},{"text":" Slime Man ","color":"green"},{"text":"out!","color":"white"},{"text":" ⇒","color":"light_purple"}]

tp @n[tag=slime_man_mayor_plubby,distance=0..] 10386 54 -219 135 0
execute as @n[tag=mayor_plubby,distance=0..] at @s run tp @s ~ ~ ~ 0 0


schedule function floaty:sched/npc/overworld_cutscene/mayor_plubby/14 5s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
