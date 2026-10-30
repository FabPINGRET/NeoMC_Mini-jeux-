particle minecraft:block{block_state:"red_wool"} -9934 191 148 1 1 1 1 200 force
kill @e[tag=boss_sop_cutscene,distance=0..]
playsound minecraft:entity.ender_dragon.hurt hostile @a[tag=mg.flw] -9934 191 148 1 0.1 1

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/1/cutscene/8 1.6s
