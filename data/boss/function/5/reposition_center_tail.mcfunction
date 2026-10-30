function boss:5/clear
schedule function floaty:sched/boss/5/appear_random 2s replace
tag @e[tag=boss_skt_hole,distance=0..] remove boss_skt_hole_last
tag @e[tag=boss_skt_hole_1,distance=0..] add boss_skt_hole_last

execute if block -10196 55 411 stone run schedule function floaty:sched/boss/5/pick_attack 5s
