execute positioned 10396 170 -12 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> Have you come to beg for mercy? Have you come to swear fealty like the ","color":"white","bold":false},{"text":"Lord of Smoke","color":"yellow"},{"text":"? He and his Contagions proved inadequate to serve, failures every one...","color":"white","bold":false},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/machine/2 11s replace

#","color":"white"},{"text":"
