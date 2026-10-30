function boss:mini/custodian/time/blank_walls

fill -10453 84 427 -10429 119 451 minecraft:blue_stained_glass replace minecraft:black_stained_glass
fill -10453 84 427 -10429 119 451 minecraft:blue_stained_glass replace minecraft:orange_stained_glass
fill -10453 84 427 -10429 119 451 minecraft:blue_stained_glass replace minecraft:white_stained_glass
fill -10453 84 427 -10429 119 451 minecraft:blue_stained_glass replace minecraft:light_blue_stained_glass


fill -10453 90 427 -10429 119 451 minecraft:blue_concrete replace #wool
fill -10453 84 427 -10429 84 451 minecraft:yellow_concrete replace #wool
fill -10453 85 427 -10429 85 451 minecraft:orange_concrete replace #wool
fill -10453 86 427 -10429 86 451 minecraft:red_concrete replace #wool
fill -10453 87 427 -10429 89 451 minecraft:purple_concrete replace #wool


summon armor_stand -10441 83.1 429 {Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["custodian_sunset_moon","custodian_display"],attributes:[{id:"minecraft:scale",base:4}],Pose:{Head:[0f,0f,180f]},equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{"properties":[{"name":"textures","value":"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOTk1MTRiMGY2N2E4YTFhMGJmODNjMmY4ODE3NTViNjA1MWIyYmQ0MmVlMzMwMjM0NGM1MzE1YWI3ZWQzNjk2ZSJ9fX0="}]}}}}}




execute if score custodian_phase Value matches 1 run schedule function floaty:sched/boss/mini/custodian/attack/sunset_start_1 4s replace
execute if score custodian_phase Value matches 2 run schedule function floaty:sched/boss/mini/custodian/attack/sunset_start_2 4s replace
execute if score custodian_phase Value matches 3 run schedule function floaty:sched/boss/mini/custodian/attack/sunset_start_3 4s replace
