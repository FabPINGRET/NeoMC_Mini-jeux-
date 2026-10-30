playsound minecraft:entity.camel.hurt neutral @a[tag=mg.flw] -10122 159 -189 3 0.7
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Dust Nexus","color":"gold"},{"color":"white","text":"> I am the Nexus of the Dust Contagion, the strongest of the three sent to crack open the Floaty Isles."},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/3/cutscene/9 7s
