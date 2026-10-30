execute positioned -10081 129 164 at @e[sort=nearest,limit=1,tag=icelorn_organist,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.happy_ghast.death neutral @a[tag=mg.flw] ~ ~ ~ 3 2

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Icelorn Organist","color":"aqua"},{"text":"> ","color":"white"},{"text":"huhhhuuuuhhh","color":"gray","italic":true},{"text":" I want...","color":"white","italic":false},{"text":" hhhuhuhhuhhhhu ","color":"gray","italic":true},{"text":"I want to play this for you...","color":"white","italic":false},{"text":" hhuuuuuhhhuhuhhhh","color":"gray","italic":true},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/icelorn_choir/3 7s replace

spawnpoint @a[tag=mg.flw] -10066 123 179 135 -20
scoreboard players set $flsp mg.st 29

#","color":"white"},{"text":"
