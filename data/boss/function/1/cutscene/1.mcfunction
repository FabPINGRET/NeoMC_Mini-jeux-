playsound minecraft:entity.armadillo.hurt neutral @a[tag=mg.flw] -9934 178 148 3 0.7
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"light_purple"},{"color":"white","text":"> So, you're the hero of the Floaty Isles. They warned me about you..."},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/1/cutscene/2 6s
