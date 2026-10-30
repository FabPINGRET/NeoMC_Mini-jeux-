playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] -12476 184 -171 3 0.5
playsound minecraft:entity.happy_ghast.ambient neutral @a[tag=mg.flw] -12476 184 -171 3 0.7

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"God of Keys","color":"dark_purple","bold":true},{"text":"> The ","color":"white","bold":false},{"text":"Bell of Life","color":"gold"},{"text":" is the strongest artifact in any possible world. Its power is your power. Its life is your life. Friend, ","color":"white"},{"text":"the Bell is","color":"gold"},{"text":" you","color":"gold","italic":true},{"text":".","color":"white","italic":false},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/secret/cutscene/13 11s

#","color":"white"},{"text":"
