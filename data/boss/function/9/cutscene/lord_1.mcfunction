playsound minecraft:entity.drowned.ambient_water neutral @s -11223 -18 -109 5 2
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"blue"},{"text":">","color":"white"},{"text":" I... I can feel droplets of fresh water forming around me again...","color":"white","italic":true},{"text":" ⇒","color":"light_purple"}]


# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/lord_2 7.4s
