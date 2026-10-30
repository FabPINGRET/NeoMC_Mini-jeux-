data modify entity @n[tag=mime_stand,distance=0..] Pose set value {RightArm:[180,-1,-20],LeftArm:[180,1,20]}
tp @n[tag=mime_stand,distance=0..] -11648 166 -350 0 0
setblock -11665 150 -337 minecraft:redstone_block
execute as @n[tag=mime_stand,distance=0..] at @s run particle minecraft:squid_ink ~ ~1 ~ 0.6 0.6 0.6 0.15 10
execute as @n[tag=mime_stand,distance=0..] at @s run playsound minecraft:entity.enderman.teleport hostile @a[tag=mg.flw] ~ ~ ~ 1 1
