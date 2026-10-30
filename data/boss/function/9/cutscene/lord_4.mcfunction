execute as @a[tag=mg.flw] at @s run playsound minecraft:entity.frog.death neutral @s ~ ~ ~ 1 0.7
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Frogcrates","color":"#44BBFF"},{"text":"> You would have been trapped here forever if it weren’t for the hero standing before you.","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/lord_5 7s
