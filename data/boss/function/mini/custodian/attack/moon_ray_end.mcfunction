setblock -10456 67 433 air
fill -10451 67 433 -10453 67 435 glass replace stone

kill @e[tag=custodian_moon_ray_1,distance=0..]
kill @e[tag=custodian_moon_ray_2,distance=0..]
kill @e[tag=custodian_moon_ray_3,distance=0..]

schedule function floaty:sched/boss/mini/custodian/time/sunrise 3s replace
