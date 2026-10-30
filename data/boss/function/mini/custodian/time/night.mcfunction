function boss:mini/custodian/time/blank_walls

fill -10453 84 427 -10429 119 451 minecraft:black_stained_glass replace minecraft:light_blue_stained_glass
fill -10453 84 427 -10429 119 451 minecraft:black_stained_glass replace minecraft:blue_stained_glass
fill -10453 84 427 -10429 119 451 minecraft:black_stained_glass replace minecraft:orange_stained_glass

fill -10453 84 427 -10429 119 451 minecraft:black_concrete replace #wool

setblock -10429 87 440 minecraft:white_concrete
setblock -10430 89 443 minecraft:white_concrete
setblock -10435 89 449 minecraft:white_concrete
setblock -10444 87 451 minecraft:white_concrete
setblock -10440 90 451 minecraft:white_concrete
setblock -10451 88 445 minecraft:white_concrete
setblock -10453 90 441 minecraft:white_concrete
setblock -10451 92 433 minecraft:white_concrete
setblock -10447 90 429 minecraft:white_concrete
setblock -10440 89 427 minecraft:white_concrete
setblock -10432 88 431 minecraft:white_concrete
setblock -10429 93 437 minecraft:white_concrete
setblock -10431 94 445 minecraft:white_concrete
setblock -10447 92 449 minecraft:white_concrete
setblock -10451 93 446 minecraft:white_concrete
setblock -10452 95 435 minecraft:white_concrete
setblock -10448 97 429 minecraft:white_concrete
setblock -10442 96 427 minecraft:white_concrete
setblock -10435 93 429 minecraft:white_concrete
setblock -10431 95 433 minecraft:white_concrete
setblock -10429 98 439 minecraft:white_concrete
setblock -10433 99 448 minecraft:white_concrete
setblock -10437 98 450 minecraft:white_concrete
setblock -10443 95 451 minecraft:white_concrete
setblock -10452 97 444 minecraft:white_concrete
setblock -10453 99 440 minecraft:white_concrete
setblock -10433 98 430 minecraft:white_concrete
setblock -10438 99 427 minecraft:white_concrete
setblock -10447 100 449 minecraft:white_concrete
setblock -10443 101 432 minecraft:white_stained_glass
setblock -10446 101 438 minecraft:white_stained_glass
setblock -10449 101 435 minecraft:white_stained_glass
setblock -10446 101 445 minecraft:white_stained_glass
setblock -10441 101 449 minecraft:white_stained_glass
setblock -10437 101 445 minecraft:white_stained_glass
setblock -10433 101 439 minecraft:white_stained_glass
setblock -10440 101 439 minecraft:white_stained_glass
setblock -10437 101 434 minecraft:white_stained_glass

summon armor_stand -10441 88.5 439 {Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["custodian_midnight_moon","custodian_display"],attributes:[{id:"minecraft:scale",base:4}],Pose:{Head:[0f,0f,180f]},equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{"properties":[{"name":"textures","value":"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOTk1MTRiMGY2N2E4YTFhMGJmODNjMmY4ODE3NTViNjA1MWIyYmQ0MmVlMzMwMjM0NGM1MzE1YWI3ZWQzNjk2ZSJ9fX0="}]}}}}}


setblock -10441 90 439 light[level=15]


execute if score custodian_phase Value matches 1 run schedule function floaty:sched/boss/mini/custodian/attack/moon_ray_start_3 4s replace
execute if score custodian_phase Value matches 2 run schedule function floaty:sched/boss/mini/custodian/attack/moon_ray_start_2 4s replace
execute if score custodian_phase Value matches 3 run schedule function floaty:sched/boss/mini/custodian/attack/moon_ray_start_1 4s replace
