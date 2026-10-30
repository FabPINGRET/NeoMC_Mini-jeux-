playsound minecraft:entity.armadillo.hurt neutral @a[tag=mg.flw] -9934 178 148 3 0.7
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Bloom Nexus","color":"light_purple"},{"color":"white","text":"> Goodbye."}]
function music:boss_fanfare
bossbar set boss:sop players @a[tag=mg.flw]
schedule function floaty:sched/music/floaty_boss 45t replace

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/1/cutscene/9 2.5s
