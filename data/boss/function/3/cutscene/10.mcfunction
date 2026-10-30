data modify entity @e[limit=1,tag=lod_boss_cutscene,distance=0..] Pose set value {}

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/3/cutscene/12 0.8s
