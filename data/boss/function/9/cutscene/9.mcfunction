#stop facing player
setblock -11243 -34 -132 air

#start boss tick
setblock -11245 -34 -132 minecraft:redstone_block

playsound minecraft:block.sniffer_egg.plop hostile @a[tag=mg.flw] -11223 22 -109 5 0.1 1

summon marker -11223 25 -109 {NoGravity:1b,Silent:1b,Tags:["wm_drone_pos","1"]}
summon marker -11223 25 -109 {NoGravity:1b,Silent:1b,Tags:["wm_drone_dest","1"]}
summon marker -11223 -7 -109 {NoGravity:1b,Silent:1b,Tags:["wm_drone_pivot","1"]}

function boss:9/setup/drone_1
execute as @n[tag=wm_drone_pos,tag=1,distance=0..] at @s run function boss:9/move/loc_mode/ring
function boss:9/move/speed/medium_all
execute as @n[tag=wm_drone_pivot,tag=1,distance=0..] run function boss:9/move/rotate/random_yaw
execute as @n[tag=wm_drone_pivot,tag=1,distance=0..] run data modify entity @s Rotation[1] set value 90
execute as @n[tag=wm_drone_pivot,tag=1,distance=0..] run function boss:9/move/rotate/random_dir
#start raising pivot for 1
setblock -11248 -35 -129 minecraft:redstone_block

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/10 1.5s
