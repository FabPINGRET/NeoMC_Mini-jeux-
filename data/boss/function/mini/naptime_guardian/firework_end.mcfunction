setblock -11543 190 -326 air
setblock -11540 189 -332 air
tp @n[tag=naptime_stand,distance=0..] -11545.5 200 -335.5 0 0
schedule function floaty:sched/boss/mini/naptime_guardian/bat_thorn 2s replace
