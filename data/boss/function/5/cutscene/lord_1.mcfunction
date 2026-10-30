playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] -10222 95 434 3 2
playsound minecraft:entity.creaking.unfreeze neutral @a[tag=mg.flw] -10222 95 434 3 1

tellraw @a[tag=mg.flw] [{"color":"white","text":"<"},{"color":"green","text":"Lord of Forest"},{"color":"white","text":"> You freed me hero, thank you."},{"text":" ⇒","color":"light_purple"}]


# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/5/cutscene/lord_2 5s
