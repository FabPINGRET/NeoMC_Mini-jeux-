playsound minecraft:entity.ravager.stunned neutral @a[tag=mg.flw] -10058 117 -355 3 1.4
tellraw @a[tag=mg.flw] [{"text":"<","italic":true},{"text":"?","color":"red"},{"text":"> I...      I am........","color":"white"},{"text":" ⇒","color":"light_purple"}]
kill @e[type=minecraft:magma_cube,distance=0..]
# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/4/cutscene/lord_2 4s
