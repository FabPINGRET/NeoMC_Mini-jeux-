playsound minecraft:entity.drowned.ambient_water neutral @s -11223 -18 -109 5 2
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Water","color":"blue"},{"text":"> I leave you with this simple gift. Goodbye.","color":"white"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/lord_8 6s
