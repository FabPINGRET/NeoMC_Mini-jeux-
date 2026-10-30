execute positioned -10081 129 164 at @e[sort=nearest,limit=1,tag=icelorn_organist,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.happy_ghast.death neutral @a[tag=mg.flw] ~ ~ ~ 3 2

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Icelorn Organist","color":"aqua"},{"text":"> ","color":"white"},{"text":"hhuuhhhuh","color":"gray","italic":true},{"text":" You...","color":"white","italic":false},{"text":" hhhhuuhhhhhh ","color":"gray","italic":true},{"text":"You aren't listening...","color":"white","italic":false},{"text":" hhuuhuuhhhuhuuhhuhuhuh","color":"gray","italic":true},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/icelorn_choir/6 7s replace

function boss:mini/icelorn_choir/speed/2
function boss:mini/icelorn_choir/song/all_inst

#","color":"white"},{"text":"
