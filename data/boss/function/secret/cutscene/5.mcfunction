playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] -12471 184 -171 3 0.5
playsound minecraft:entity.happy_ghast.ambient neutral @a[tag=mg.flw] -12471 184 -171 3 0.7

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"God of Keys","color":"dark_purple","bold":true},{"text":"> Hush, I want to give you a ","color":"white"},{"text":"gift","color":"aqua"},{"text":", old friend. But first show me what you’ve learned over these past few thousand years!","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/secret/cutscene/6 11s

schedule function floaty:sched/music/boss_intro 5s

#","color":"white"},{"text":"
