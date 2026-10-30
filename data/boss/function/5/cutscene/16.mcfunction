setblock -10197 55 407 air
setblock -10197 55 409 minecraft:redstone_block
data merge entity @n[type=armor_stand,tag=boss_skt_cutscene,distance=0..] {Pose:{LeftArm:[240f,340f,0f],RightArm:[240f,20f,0f]}}
setblock -10213 56 411 minecraft:redstone_block
scoreboard players set @a[gamemode=!spectator,tag=mg.flw] ScreenShake 1

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/5/cutscene/17 2s
