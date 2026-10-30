playsound minecraft:entity.camel.hurt neutral @a[tag=mg.flw] -10122 159 -189 3 0.7
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"gold"},{"color":"white","text":"> It was decided that we first conquer a weaker dimension, one much closer to the Floaty Isles, to be our base of attack against the "},{"text":"Bell","color":"gold"},{"text":".","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/3/cutscene/6 9s
