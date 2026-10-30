playsound minecraft:entity.vex.ambient neutral @a[tag=mg.flw] -11830 216 330 3 0.7
playsound minecraft:entity.vex.charge neutral @a[tag=mg.flw] -11830 216 330 3 0.1
playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] -11830 216 330 3 0.1
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"yellow"},{"color":"white","text":"> Welcome to the halls of the dead, \"hero.\""},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/10/cutscene/2 6s


kill @e[tag=ta_soul_display,tag=rictus,distance=0..]
kill @e[tag=ta_soul_display,tag=wailing,distance=0..]
kill @e[tag=ta_soul_display,tag=scornful,distance=0..]
kill @e[tag=ta_soul_display,tag=cackling,distance=0..]
