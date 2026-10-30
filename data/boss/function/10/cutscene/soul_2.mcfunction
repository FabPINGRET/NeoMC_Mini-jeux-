tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Penitent Soul","color":"white"},{"color":"white","text":"> ... Though my master was guilty of betraying the world, I am guilty of betraying my master..."},{"text":" ⇒","color":"light_purple"}]

playsound minecraft:entity.allay.ambient_without_item neutral @a[tag=mg.flw] -11830 217 330 5 0.5 

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/10/cutscene/soul_3 10s
