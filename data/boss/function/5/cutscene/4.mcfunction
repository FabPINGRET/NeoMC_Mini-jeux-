setblock -10197 55 407 air
setblock -10197 55 409 minecraft:redstone_block
playsound minecraft:entity.creaking.deactivate neutral @a[tag=mg.flw] -10222 93 427 3 2
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Dreadwarden of Forest","color":"green"},{"color":"white","text":"> Behold, the"},{"color":"green","text":" Serpent King"},{"color":"white","text":"!"},{"text":" ⇒","color":"light_purple"}]
data merge entity @n[type=armor_stand,tag=boss_skt_cutscene,distance=0..] {Pose:{LeftArm:[240f,340f,0f],RightArm:[240f,20f,0f]}}

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/5/cutscene/5 2s
