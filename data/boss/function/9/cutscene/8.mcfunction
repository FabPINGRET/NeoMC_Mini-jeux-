scoreboard players set @a[gamemode=!spectator,tag=mg.flw] ScreenShake 1
function music:boss_intro

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/8.5 4s
