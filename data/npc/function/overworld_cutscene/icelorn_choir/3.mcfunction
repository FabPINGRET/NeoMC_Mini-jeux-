execute positioned -10081 129 164 at @e[sort=nearest,limit=1,tag=icelorn_organist,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.happy_ghast.death neutral @a[tag=mg.flw] ~ ~ ~ 3 2

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Icelorn Organist","color":"aqua"},{"text":"> ","color":"white"},{"text":"hhhuhhhuhhuhh","color":"gray","italic":true},{"text":" Please, listen...","color":"white","italic":false},{"text":" hhhhuhhhhuhuh","color":"gray","italic":true}]

schedule function floaty:sched/npc/overworld_cutscene/icelorn_choir/4 4s replace

execute as @n[tag=icelorn_organist,distance=0..] at @s run tp @s ~ ~ ~ 135 0

#","color":"white"},{"text":"
