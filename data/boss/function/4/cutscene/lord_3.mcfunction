playsound minecraft:entity.ravager.stunned neutral @a[tag=mg.flw] -10058 117 -355 3 1.4
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Flame","color":"red"},{"text":"> Thank you hero, I am in your debt.","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/4/cutscene/lord_4 5s
