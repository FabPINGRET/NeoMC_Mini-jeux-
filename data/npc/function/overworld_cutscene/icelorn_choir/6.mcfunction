execute positioned -10081 129 164 at @e[sort=nearest,limit=1,tag=icelorn_organist,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.happy_ghast.death neutral @a[tag=mg.flw] ~ ~ ~ 3 2

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Icelorn Organist","color":"aqua"},{"text":"> ","color":"white"},{"text":"hhhhuuhhhhhu","color":"gray","italic":true},{"text":" Please, please listen...","color":"white","italic":false},{"text":" hhuuhuhuh ","color":"gray","italic":true},{"text":"If not to me, then to the ","color":"white","italic":false},{"text":"choir","color":"aqua"},{"text":"...","color":"white"},{"text":" hhhuhuuhuhhhhhuhh","color":"gray","italic":true}]

schedule function floaty:sched/npc/overworld_cutscene/icelorn_choir/7 8s replace

#","color":"white"},{"text":"
