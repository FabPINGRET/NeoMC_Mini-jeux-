playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] -12476 184 -171 3 0.5
playsound minecraft:entity.happy_ghast.ambient neutral @a[tag=mg.flw] -12476 184 -171 3 0.7

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"God of Keys","color":"dark_purple","bold":true},{"color":"white","text":"> Haven’t you noticed you’re much more powerful than any other being you encounter? That’s not a coincidence!","color":"white","bold":false},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/secret/cutscene/12 9s

#","color":"white"},{"text":"
