playsound minecraft:entity.camel.hurt neutral @a[tag=mg.flw] -10122 159 -189 3 0.7
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Dust Nexus","color":"gold"},{"color":"white","text":"> Everything is in place now. Today, the "},{"text":"World Virus ","color":"dark_aqua"},{"text":"will tear into your dimension from our new stronghold, the ","color":"white"},{"text":"Dark Isles","color":"dark_purple"},{"text":".","color":"white"},{"text":" ⇒","color":"light_purple"}]
function music:boss_intro

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/3/cutscene/14 7s
