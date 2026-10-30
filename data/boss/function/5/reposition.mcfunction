function boss:5/clear
schedule function floaty:sched/boss/5/appear_random 2s replace
setblock -10204 55 418 minecraft:blue_wool

execute if block -10196 55 411 stone run schedule function floaty:sched/boss/5/pick_attack 5s
