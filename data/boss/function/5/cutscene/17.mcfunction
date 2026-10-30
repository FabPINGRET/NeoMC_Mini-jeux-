function boss:5/cutscene/skeleton
data modify entity @n[type=armor_stand,tag=boss_skt_cutscene,distance=0..] Pose set value {}
setblock -10213 56 411 air
scoreboard players set @a[gamemode=!spectator,tag=mg.flw] ScreenShake 0

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/5/cutscene/18 2s
