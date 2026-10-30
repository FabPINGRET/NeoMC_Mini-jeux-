playsound minecraft:entity.creaking.deactivate neutral @a[tag=mg.flw] -10222 93 427 3 2
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Dreadwarden of Forest","color":"green"},{"color":"white","text":"> The whole time I was working on him, I would imagine him murdering you and it brought a smile to my face."},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/5/cutscene/12 2s
