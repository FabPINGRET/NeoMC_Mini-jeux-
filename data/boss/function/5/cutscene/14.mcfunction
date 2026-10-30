playsound minecraft:entity.creaking.deactivate neutral @a[tag=mg.flw] -10222 93 427 3 2
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Dreadwarden of Forest","color":"green"},{"color":"white","text":"> But, now that we’re here... Well... I think I preferred him when he was dead."},{"text":" ⇒","color":"light_purple"}]


# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/5/cutscene/15 2s
