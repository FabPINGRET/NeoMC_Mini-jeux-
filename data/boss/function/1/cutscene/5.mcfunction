playsound minecraft:entity.armadillo.hurt neutral @a[tag=mg.flw] -9934 178 148 3 0.7
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Bloom Nexus","color":"light_purple"},{"color":"white","text":"> Something greater than myself or my "},{"text":"two brothers","color":"light_purple"},{"text":" is on its way. We herald its arrival with destruction!","color":"white"},{"text":" ⇒","color":"light_purple"}]
setblock -9945 167 169 minecraft:redstone_block
function music:boss_intro

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/1/cutscene/6 9s
