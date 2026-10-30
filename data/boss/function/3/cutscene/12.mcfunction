playsound minecraft:entity.camel.hurt neutral @a[tag=mg.flw] -10122 159 -189 3 0.7
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Dust Nexus","color":"gold"},{"color":"white","text":"> The "},{"text":"Seven Lords ","color":"gold"},{"text":"of the ","color":"white"},{"text":"Dark Isles ","color":"dark_purple"},{"text":"have been subdued. Their world now belongs to us.","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/3/cutscene/13 8s
