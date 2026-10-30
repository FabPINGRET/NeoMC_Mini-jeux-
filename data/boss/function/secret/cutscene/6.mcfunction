playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] -12471 184 -171 3 0.5
playsound minecraft:entity.happy_ghast.ambient neutral @a[tag=mg.flw] -12471 184 -171 3 0.7

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"God of Keys","color":"dark_purple","bold":true},{"text":"> Bring everything you have against me, hold nothing back!","color":"white"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/secret/cutscene/7 5s

#","color":"white"},{"text":"
