playsound minecraft:entity.skeleton.hurt neutral @a[tag=mg.flw] -10146 153 -31 3 0.7
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Bone Nexus","color":"gray"},{"text":"> I am the Nexus of the one-of-a-kind \"Bone Contagion,\" and I'm a bit nastier than my ","color":"white"},{"text":"rose-headed brother","color":"gray"},{"text":".","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/2/cutscene/6 8s
