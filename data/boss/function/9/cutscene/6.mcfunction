playsound minecraft:entity.glow_squid.hurt hostile @a[tag=mg.flw] -11223 -20 -109 3 1.4 1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Dreadwarden of Water","color":"blue"},{"color":"white","text":"> It is with this assurance of victory that I face you now.","color":"white"},{"text":" ⇒","color":"light_purple"}]

playsound minecraft:entity.lightning_bolt.thunder hostile @a[tag=mg.flw] -11223 -20 -109 3 0.8 1

#Start Rising to the Ceiling
setblock -11241 -34 -132 minecraft:redstone_block

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/7 7s
