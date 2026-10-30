function boss:mini/mime_in_charge/pose_init
data merge entity @n[tag=mime_stand,distance=0..] {Pose:{Head:[0f,0f,0f]}}
setblock -11665 150 -339 minecraft:redstone_block
item replace entity @n[tag=mime_stand,distance=0..] weapon.mainhand with minecraft:netherite_sword
item replace entity @n[tag=mime_stand,distance=0..] weapon.offhand with minecraft:netherite_sword
execute as @e[tag=mime_border,sort=random,limit=1,distance=0..] at @s run tp @n[tag=mime_stand,distance=0..] ~ 160 ~

schedule function floaty:sched/boss/mini/mime_in_charge/chase_run 5t
