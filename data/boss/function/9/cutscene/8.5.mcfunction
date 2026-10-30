playsound minecraft:entity.glow_squid.hurt hostile @a[tag=mg.flw] -11223 -20 -109 3 1.4 1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Dreadwarden of Water","color":"blue"},{"color":"white","text":"> You have no help, no escape, and no"},{"text":" hope","color":"white","italic":true},{"text":".","color":"white","italic":false}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/9 3.5s
