playsound minecraft:entity.armadillo.hurt neutral @a[tag=mg.flw] -9934 178 148 3 0.7
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Bloom Nexus","color":"light_purple"},{"color":"white","text":"> You die here, hero. The "},{"text":"Monarch Rose","color":"light_purple"},{"text":" is almost completely under my control now.","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/1/cutscene/7 6s
