tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Penitent Soul","color":"white"},{"color":"white","text":"> I must do penance, hero. Please, take this and leave our halls..."}]

playsound minecraft:entity.allay.ambient_without_item neutral @a[tag=mg.flw] -11830 217 330 5 0.5 

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/10/cutscene/soul_4 7s
