execute positioned 10396 170 -12 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> Defender, surely you understand where we’re situated. Below this spot in the","color":"white","bold":false},{"text":" Floaty Isles","color":"yellow"},{"text":" is the","color":"white"},{"text":" Bell of Life","color":"gold"},{"text":".","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/machine/9 9s replace

#","color":"white"},{"text":"
