playsound minecraft:entity.glow_squid.hurt hostile @a[tag=mg.flw] -11223 -20 -109 3 1.4 1
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"blue"},{"color":"white","text":"> I expected that you would find me here."},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/2 6s
