playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] -12471 184 -171 3 0.5
playsound minecraft:entity.happy_ghast.ambient neutral @a[tag=mg.flw] -12471 184 -171 3 0.7

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"God of Keys","color":"dark_purple","bold":true},{"color":"white","text":"> You are the"},{"text":" Bell","color":"gold"},{"text":", are you not? Hmmm, but you have its scent! Surely, I am not mistaken.","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/secret/cutscene/4 8s

#","color":"white"},{"text":"
