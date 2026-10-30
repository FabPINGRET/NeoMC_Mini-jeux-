kill @e[tag=vesperal_spike,distance=0..]
kill @e[tag=vesperal_spike_pos,distance=0..]
fill -10591 3 194 -10555 24 230 air replace barrier
kill @e[tag=mooneye,distance=0..]

spreadplayers -10573 212 7 11 false @e[tag=vesperal_spike_loc,distance=0..]
execute as @e[tag=vesperal_spike_loc,distance=0..] at @s align xz run tp @s ~0.5 ~ ~0.5
execute positioned -10573 77 212 run tag @e[tag=vesperal_spike_loc,distance=..5] add too_close

function boss:mini/vesperal_paladin/summon_spike_5
schedule function floaty:sched/boss/mini/vesperal_paladin/summon_spike_4 10t
schedule function floaty:sched/boss/mini/vesperal_paladin/summon_spike_3 20t
schedule function floaty:sched/boss/mini/vesperal_paladin/summon_spike_2 30t
schedule function floaty:sched/boss/mini/vesperal_paladin/summon_spike_1 40t
