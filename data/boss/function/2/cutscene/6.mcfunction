execute as @n[tag=cob_boss_cutscene,distance=0..] at @s run playsound minecraft:entity.skeleton.hurt neutral @a[tag=mg.flw] ~ ~ ~ 3 0.7
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Bone Nexus","color":"gray"},{"text":"> I bet you noticed my pet ","color":"white"},{"text":"Kraken ","color":"gray"},{"text":"when you came in; she's a little dead and dried out at the moment.","color":"white"},{"text":" ⇒","color":"light_purple"}]
setblock -10115 138 -63 minecraft:redstone_block

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/2/cutscene/7 6s
