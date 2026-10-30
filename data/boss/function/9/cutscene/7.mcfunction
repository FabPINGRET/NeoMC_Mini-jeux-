playsound minecraft:entity.glow_squid.hurt hostile @a[tag=mg.flw] -11223 -20 -109 3 1.4 1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Dreadwarden of Water","color":"blue"},{"color":"white","text":"> You and I are still new to this mental realm, but"},{"text":" Aquamentra","color":"blue"},{"text":", the great","color":"white"},{"text":" Mind-Barnacle","color":"#44BBFF"},{"text":", has grown in power here for decades.","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/8 5s
