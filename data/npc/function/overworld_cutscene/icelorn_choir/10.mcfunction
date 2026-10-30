execute positioned -10081 129 164 at @e[sort=nearest,limit=1,tag=icelorn_organist,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.happy_ghast.death neutral @a[tag=mg.flw] ~ ~ ~ 3 2

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Icelorn Organist","color":"aqua"},{"text":"> ","color":"white"},{"text":"hhhuhhhuhhhh","color":"gray","italic":true},{"text":"... ","color":"white","italic":false}]

schedule function floaty:sched/npc/overworld_cutscene/icelorn_choir/11 4s replace

#","color":"white"},{"text":"
