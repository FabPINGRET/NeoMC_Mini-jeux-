#execute positioned -223 34 246 at @e[sort=nearest,limit=1,tag=npc] positioned ~ ~1 ~ run playsound minecraft:entity.happy_ghast.death neutral @a ~ ~ ~ 1 2

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Icelorn Tenor","color":"aqua"},{"text":"> ","color":"white"},{"text":"hhhhuuuhhuh","color":"gray","italic":true},{"text":" Come...","color":"white","italic":false},{"text":" huuhhuhhhuuhuh ","color":"gray","italic":true},{"text":"Our organist wants to show you a song...","color":"white","italic":false},{"text":" hhhuuuhuhuhuhhhhuuuuuhhh","color":"gray","italic":true},{"text":" ⇒","color":"light_purple"}]

execute positioned -223 35 246 run kill @e[type=snowball,tag=boss_marker,distance=..3]

schedule function floaty:sched/npc/overworld_cutscene/icelorn_choir/1 9s replace

fill -222 34 245 -222 34 246 air

tag @a[tag=mg.flw] add no_warp
function music:end
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1

#","color":"white"},{"text":"
