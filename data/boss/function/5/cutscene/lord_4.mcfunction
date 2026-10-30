playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] -10222 95 434 3 2
playsound minecraft:entity.creaking.unfreeze neutral @a[tag=mg.flw] -10222 95 434 3 1

tellraw @a[tag=mg.flw] [{"color":"white","text":"<"},{"color":"green","text":"Lord of Forest"},{"color":"white","text":"> The trees leave you with this gift. Farewell."}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/5/cutscene/lord_5 6s
