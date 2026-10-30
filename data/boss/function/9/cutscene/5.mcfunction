playsound minecraft:entity.glow_squid.hurt hostile @a[tag=mg.flw] -11223 -20 -109 3 1.4 1
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Dreadwarden of Water","color":"blue"},{"color":"white","text":"> Even if you free the"},{"color":"blue","text":" Lord of Water "},{"color":"white","text":"today, the "},{"color":"yellow","text":"Lord of Smoke"},{"color":"white","text":" is ours forever.","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/6 7.5s
