playsound minecraft:entity.camel.hurt neutral @a[tag=mg.flw] -10122 159 -189 3 0.7
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Dust Nexus","color":"gold"},{"color":"white","text":"> And, like my "},{"text":"Wyrm","color":"gold"},{"text":", he will swallow you whole...","color":"white"},{"text":" ⇒","color":"light_purple"}]
setblock -10083 134 -211 minecraft:redstone_block
setblock -10092 134 -188 minecraft:redstone_block

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/3/cutscene/15 5.2s
