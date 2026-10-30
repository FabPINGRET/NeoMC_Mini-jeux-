playsound minecraft:entity.strider.death neutral @a[tag=mg.flw] -10072 116 -355 3 2
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"red"},{"color":"white","text":"> The "},{"text":"Dark Isles ","color":"dark_purple"},{"text":"have already been claimed by the ","color":"white"},{"text":"World Virus","color":"dark_aqua"},{"text":".","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/4/cutscene/3 7s
