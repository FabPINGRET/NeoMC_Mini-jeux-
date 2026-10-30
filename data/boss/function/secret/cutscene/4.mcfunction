playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] -12471 184 -171 3 0.5
playsound minecraft:entity.happy_ghast.ambient neutral @a[tag=mg.flw] -12471 184 -171 3 0.7

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"God of Keys","color":"dark_purple","bold":true},{"color":"white","text":"> Yes, yes, you are the incarnate power of the"},{"text":" Bell","color":"gold"},{"text":", I can smell the truth on you plain as anything.","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/secret/cutscene/5 9s

#","color":"white"},{"text":"
