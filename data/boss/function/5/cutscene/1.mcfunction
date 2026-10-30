playsound minecraft:entity.creaking.deactivate neutral @a[tag=mg.flw] -10222 93 427 3 2
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"green"},{"color":"white","text":"> Ohhh it’s the defender of the"},{"color":"gold","text":" Bell"},{"color":"white","text":"!"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/5/cutscene/2 5s
