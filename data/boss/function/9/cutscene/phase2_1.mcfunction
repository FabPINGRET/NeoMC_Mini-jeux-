scoreboard players set @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] ScreenShake 1
kill @e[tag=wm_drone_pos,distance=0..]
kill @e[tag=wm_drone_dest,distance=0..]
kill @e[tag=wm_drone_pivot,distance=0..]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/phase2_2 4s
