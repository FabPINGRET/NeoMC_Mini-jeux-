playsound minecraft:entity.skeleton.hurt neutral @a[tag=mg.flw] -10146 153 -31 3 0.7
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"gray"},{"text":"> It's been sooooo boring waiting for you to finally show up.","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/2/cutscene/2 6s
