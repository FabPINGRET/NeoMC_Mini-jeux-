playsound minecraft:entity.vex.ambient neutral @a[tag=mg.flw] -11830 216 330 3 0.7
playsound minecraft:entity.vex.charge neutral @a[tag=mg.flw] -11830 216 330 3 0.1
playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] -11830 216 330 3 0.1
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"yellow"},{"text":"> All that stands in his way now is the","color":"white"},{"text":" Bell of Life","color":"gold"},{"text":". And you."},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/10/cutscene/5 7.5s

#","color":"white"},{"text":"
