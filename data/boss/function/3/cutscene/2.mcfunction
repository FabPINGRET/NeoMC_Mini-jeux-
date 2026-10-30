playsound minecraft:entity.camel.hurt neutral @a[tag=mg.flw] -10122 159 -189 3 0.7
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"gold"},{"color":"white","text":"> While you've been busy shutting our operations down in this dimension, we've been working... growing in strength... preparing..."},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/3/cutscene/3 8s
