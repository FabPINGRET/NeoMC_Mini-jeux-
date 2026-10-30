execute positioned -12298 233 -279 run tag @p[tag=mg.flw] add sc_snake_captain_3
tag @a[tag=mg.flw] remove sc_snake_respawn_2
execute if block -12341 212 -240 ice run tag @a[tag=mg.flw] add sc_snake_respawn_3
setblock -12300 232 -279 minecraft:purple_wool strict
summon armor_stand -12300 232 -279 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_3","1"],DisabledSlots:4144959}
summon armor_stand -12300 232 -279 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_3","2"],DisabledSlots:4144959}
summon armor_stand -12300 232 -279 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_3","3"],DisabledSlots:4144959}
summon armor_stand -12300 232 -279 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_3","4"],DisabledSlots:4144959}
summon armor_stand -12300 232 -279 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_3","5"],DisabledSlots:4144959}
summon armor_stand -12300 232 -279 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_3","6"],DisabledSlots:4144959}
summon armor_stand -12300 232 -279 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_3","7"],DisabledSlots:4144959}
scoreboard players set sc_ride_free_3 Countdown 0
schedule function floaty:sched/dungeon/extra/snake/3_advance 5t replace
