function music:boss_fanfare
schedule function floaty:sched/music/virus 45t replace
bossbar set boss:final players @a[tag=mg.flw]
fill -12362 127 360 -12356 123 350 light[level=15]

schedule function floaty:sched/boss/final/virus/attack/do_spike 2s replace
scoreboard players set wv_lastattack Value 1

function boss:final/virus/model/heart

fill -12339 128 356 -12339 130 354 barrier

#","color":"white"},{"text":"

schedule function floaty:sched/boss/final/cutscene/lordsword_0 9s replace
