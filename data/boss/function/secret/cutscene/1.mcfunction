execute positioned -12471 183 -171 run function boss:secret/setup

setblock -12453 162 -153 redstone_block
function boss:secret/display/target/nearest

particle minecraft:end_rod -12471 187 -171 1 1 1 0.3 200
particle minecraft:witch -12471 187 -171 1 1 1 1 200
playsound minecraft:block.trial_spawner.ominous_activate master @a[tag=mg.flw] -12471 187 -171 3 0.4
playsound minecraft:entity.enderman.teleport master @a[tag=mg.flw] -12471 187 -171 3 0.4

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/secret/cutscene/2 3s
