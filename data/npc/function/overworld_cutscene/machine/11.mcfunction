execute positioned 10396 170 -12 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> The ","color":"white","bold":false},{"text":"World Virus","color":"dark_aqua"},{"text":" has full access to the ","color":"white"},{"text":"Bell","color":"gold"},{"text":" now. My work here is done.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/machine/12 7s replace

#","color":"white"},{"text":"
