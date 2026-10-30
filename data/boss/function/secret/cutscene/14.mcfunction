setblock -12472 184 -169 minecraft:chiseled_resin_bricks
setblock -12471 184 -171 minecraft:chiseled_resin_bricks
setblock -12472 184 -173 minecraft:chiseled_resin_bricks

particle effect{color:[0.000,1.000,1.000],power:0.5} -12472 184 -169 0.5 0.5 0.5 0.1 100
particle effect{color:[0.000,1.000,1.000],power:0.5} -12471 184 -171 0.5 0.5 0.5 0.1 100
particle effect{color:[0.000,1.000,1.000],power:0.5} -12472 184 -173 0.5 0.5 0.5 0.1 100

playsound minecraft:entity.glow_squid.ambient master @a[tag=mg.flw] -12471 184 -171 4 1
playsound minecraft:entity.glow_squid.squirt master @a[tag=mg.flw] -12471 184 -171 4 1

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/secret/cutscene/15 3s


#","color":"white"},{"text":"
