execute positioned 10396 170 -12 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> Today, that needle punched a sucking wound in the fabric of space, and the trickle of power has become a torrent. A direct tunnel between the ","color":"white","bold":false},{"text":"Floaty Isles","color":"yellow"},{"text":" and my ","color":"white"},{"text":"homeworld","color":"aqua"},{"text":" has been opened.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/machine/11 12s replace

#","color":"white"},{"text":"
