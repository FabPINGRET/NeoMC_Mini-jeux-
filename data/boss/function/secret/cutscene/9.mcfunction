tp @n[tag=sc_boss_pos,distance=0..] -12476 184 -171
tp @n[tag=sc_boss_dest,distance=0..] -12476 184 -171

function boss:secret/display/target/nearest

particle minecraft:end_rod -12476 187 -171 1 1 1 0.3 200
particle minecraft:witch -12476 187 -171 1 1 1 1 200
playsound minecraft:block.trial_spawner.ominous_activate master @a[tag=mg.flw] -12476 187 -171 3 0.4
playsound minecraft:entity.enderman.teleport master @a[tag=mg.flw] -12476 187 -171 3 0.4

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/secret/cutscene/10 3s
