playsound minecraft:entity.creaking.deactivate neutral @a[tag=mg.flw] -10222 93 427 3 2
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Dreadwarden of Forest","color":"green"},{"color":"white","text":"> Isn’t he great? I spent ages in this tomb, piecing his bones together and slowly bringing him back to life."},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/5/cutscene/9 2s
