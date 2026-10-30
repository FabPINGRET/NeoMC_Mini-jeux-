execute as @a[tag=mg.flw] at @s run playsound minecraft:entity.frog.death neutral @s ~ ~ ~ 1 0.7
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Frogcrates","color":"#44BBFF"},{"text":"> I’m sorry Lord, a ","color":"white"},{"text":"Memory Contagion","color":"green"},{"text":" of the ","color":"white"},{"text":"Virus","color":"dark_aqua"},{"text":" forced a","color":"white"},{"text":" Dreadwarden ","color":"aqua"},{"text":"into my mind to imprison you, and then stole my memories from me for a time.","color":"white"},{"text":" ⇒","color":"light_purple"}]

data modify entity @n[tag=lord_of_water,distance=0..] Pose.Head set value [-45f,0f,0f]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/lord_4 10s
