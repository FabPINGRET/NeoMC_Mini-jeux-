playsound minecraft:entity.creaking.deactivate neutral @a[tag=mg.flw] -10222 93 427 3 2
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Dreadwarden of Forest","color":"green"},{"color":"white","text":"> Wait, wait, don’t go anywhere, I really want to show you this..."},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/5/cutscene/4 6s
