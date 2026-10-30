data modify entity @e[limit=1,tag=lod_boss_cutscene,distance=0..] Pose set value {RightArm:[360f,80f,85f]}
item replace entity @e[tag=lod_boss_cutscene,distance=0..] weapon.mainhand with iron_sword
execute as @e[tag=lod_boss_cutscene,distance=0..] at @s run particle dust{color:[0.9,0.8,0.5],scale:2} ~ ~ ~ 0.5 1 0.5 0 20 force @a[tag=mg.flw]
setblock -10090 134 -188 minecraft:redstone_block
execute as @e[tag=lod_boss_cutscene,distance=0..] at @s run playsound minecraft:block.respawn_anchor.deplete master @a[tag=mg.flw] ~ ~ ~ 3 2
execute as @e[tag=lod_boss_cutscene,distance=0..] at @s run playsound minecraft:entity.vex.death master @a[tag=mg.flw] ~ ~ ~ 3 0.1
execute as @e[tag=lod_boss_cutscene,distance=0..] at @s run playsound minecraft:entity.lightning_bolt.thunder master @a[tag=mg.flw] ~ ~ ~ 3 0.1

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/3/cutscene/10 1.2s
