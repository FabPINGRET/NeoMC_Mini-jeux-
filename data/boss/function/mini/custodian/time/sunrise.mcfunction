function boss:mini/custodian/time/blank_walls

fill -10453 84 427 -10429 119 451 minecraft:orange_stained_glass replace minecraft:black_stained_glass
fill -10453 84 427 -10429 119 451 minecraft:orange_stained_glass replace minecraft:blue_stained_glass
fill -10453 84 427 -10429 119 451 minecraft:orange_stained_glass replace minecraft:white_stained_glass
fill -10453 84 427 -10429 119 451 minecraft:orange_stained_glass replace minecraft:light_blue_stained_glass


fill -10453 87 427 -10429 119 451 minecraft:orange_concrete replace #wool
fill -10453 84 427 -10429 84 451 minecraft:white_concrete replace #wool
fill -10453 85 427 -10429 86 451 minecraft:yellow_concrete replace #wool

summon armor_stand -10441 83.1 429 {Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["custodian_sunrise_sun","custodian_display"],attributes:[{id:"minecraft:scale",base:4}],Pose:{Head:[0f,0f,180f]},equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{"properties":[{"name":"textures","value":"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZDlkZTI1ZTk2M2E1ODk5ZTViMGQ0YzRjMmEzZTI3MjViOTI4Y2QyNDEzNmZmNmU3MWY3NDc4NzRhZTJiMTQ4YyJ9fX0="}]}}}}}

summon marker -10441 80 439 {NoGravity:1b,Silent:1b,Rotation:[180F,0F],Tags:["custodian_sunrise_pivot","custodian_display"]}



schedule function floaty:sched/boss/mini/custodian/attack/sunrise_start 3s replace
