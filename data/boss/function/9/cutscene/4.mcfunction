playsound minecraft:entity.glow_squid.hurt hostile @a[tag=mg.flw] -11223 -20 -109 3 1.4 1
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Dreadwarden of Water","color":"blue"},{"color":"white","text":"> Even if I fail to destroy you, you cannot hope to challenge the "},{"text":"Virus","color":"dark_aqua"},{"text":" without the power of seven Lords. You need","color":"white"},{"text":" all seven","color":"gold"},{"text":".","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/5 9s
