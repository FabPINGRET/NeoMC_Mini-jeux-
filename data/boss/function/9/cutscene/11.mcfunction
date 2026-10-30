function game:screenshake_end
function music:boss_fanfare
bossbar set boss:wm players @a[tag=mg.flw]
setblock -11219 -35 -131 stone
schedule function floaty:sched/boss/9/pick_attack 3s replace
schedule function floaty:sched/music/dark_boss 45t replace
