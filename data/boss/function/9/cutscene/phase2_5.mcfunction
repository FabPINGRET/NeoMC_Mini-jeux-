function game:screenshake_end

setblock -11219 -35 -131 stone
schedule function floaty:sched/boss/9/pick_attack 3s replace
