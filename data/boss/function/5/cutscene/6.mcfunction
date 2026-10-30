function boss:5/cutscene/tongue_flick
data modify entity @n[type=armor_stand,tag=boss_skt_cutscene,distance=0..] Pose set value {}

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/5/cutscene/7 2s
