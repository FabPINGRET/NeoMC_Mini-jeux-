playsound minecraft:entity.strider.death neutral @a[tag=mg.flw] -10072 116 -355 3 2
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"red"},{"color":"white","text":"> Soon, we'll have the "},{"text":"Floaty Isles ","color":"green"},{"text":"too...","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/4/cutscene/4 5s
