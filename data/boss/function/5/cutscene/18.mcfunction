setblock -10197 55 407 minecraft:redstone_block
setblock -10197 55 409 minecraft:air

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/5/cutscene/19 4s
