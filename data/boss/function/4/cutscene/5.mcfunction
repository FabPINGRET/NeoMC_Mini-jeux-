playsound minecraft:entity.strider.death neutral @a[tag=mg.flw] -10072 116 -355 3 2
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Dreadwarden of Flame","color":"red"},{"color":"white","text":"> There's no hope for you. We "},{"text":"Dreadwardens ","color":"light_purple"},{"text":"have captured all ","color":"white"},{"text":"Seven Lords ","color":"gold"},{"text":"of this world.","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/4/cutscene/6 8s
