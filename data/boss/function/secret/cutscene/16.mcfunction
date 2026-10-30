playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] -12476 184 -171 3 0.5
playsound minecraft:entity.happy_ghast.ambient neutral @a[tag=mg.flw] -12476 184 -171 3 0.7

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"God of Keys","color":"dark_purple","bold":true},{"text":"> They are for you to seek out if you desire, a final treasure hunt, hidden well. Worry not, they ","color":"white","bold":false},{"text":"do not count towards achieving 100%","color":"aqua"},{"text":"!","color":"white","bold":false}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/secret/cutscene/17 10s

function boss:secret/display/target/nearest

#","color":"white"},{"text":"
