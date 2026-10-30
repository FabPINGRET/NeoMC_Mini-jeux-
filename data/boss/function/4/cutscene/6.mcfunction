playsound minecraft:entity.strider.death neutral @a[tag=mg.flw] -10072 116 -355 3 2
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Dreadwarden of Flame","color":"red"},{"color":"white","text":"> Now, you're locked in this room with me! If I could overpower the "},{"text":"Lord of Flame","color":"red"},{"text":", I can certainly overpower you...","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/4/cutscene/7 4.4s
