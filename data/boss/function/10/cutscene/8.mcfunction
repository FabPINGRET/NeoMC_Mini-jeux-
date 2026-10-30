playsound minecraft:entity.vex.ambient neutral @a[tag=mg.flw] -11830 216 330 3 0.7
playsound minecraft:entity.vex.charge neutral @a[tag=mg.flw] -11830 216 330 3 0.1
playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] -11830 216 330 3 0.1
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Smoke","color":"yellow"},{"text":"> Why be one of seven when I could be the ","color":"white"},{"text":"One Lord","color":"yellow"},{"text":"? That is the offer ","color":"white"},{"text":"Morbex","color":"dark_aqua"},{"text":" came to me with."},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/10/cutscene/9 10s

#","color":"white"},{"text":"
