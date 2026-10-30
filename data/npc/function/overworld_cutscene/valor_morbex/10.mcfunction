tp @n[tag=slime_man_valor_tower_1,distance=0..] 10020 94 -98 -45 0

execute positioned 10020 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10020 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"green"},{"text":"> I… oh, he’s already gone.","color":"white"}]
execute positioned 10020 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:item.chorus_fruit.teleport neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute positioned 10020 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run particle minecraft:sneeze ~ ~ ~ 0.1 0.1 0.1 0.05 100 force @a[tag=mg.flw]

execute as @a[tag=mg.flw] at @s run playsound minecraft:soundtrack.slime_man_fail record @s

schedule function floaty:sched/npc/overworld_cutscene/valor_morbex/10.5 4s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
