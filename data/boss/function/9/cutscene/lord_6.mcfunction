playsound minecraft:entity.drowned.ambient_water neutral @s -11223 -18 -109 5 2
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Water","color":"blue"},{"text":"> I wish I had time for a longer thank you, hero, but I must return to","color":"white"},{"text":" Valor Tower","color":"red"},{"text":" and investigate recent events.","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/lord_7 8s
