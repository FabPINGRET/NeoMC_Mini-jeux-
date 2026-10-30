execute positioned -12361 223 -302 run tag @p[tag=mg.flw] add sc_snake_captain_2
execute if block -12341 212 -240 ice run tag @a[tag=mg.flw] add sc_snake_respawn_2
setblock -12361 222 -300 minecraft:purple_wool strict
summon armor_stand -12361 222 -300 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_2","1"],DisabledSlots:4144959}
summon armor_stand -12361 222 -300 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_2","2"],DisabledSlots:4144959}
summon armor_stand -12361 222 -300 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_2","3"],DisabledSlots:4144959}
summon armor_stand -12361 222 -300 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_2","4"],DisabledSlots:4144959}
summon armor_stand -12361 222 -300 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_2","5"],DisabledSlots:4144959}
summon armor_stand -12361 222 -300 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_2","6"],DisabledSlots:4144959}
summon armor_stand -12361 222 -300 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_2","7"],DisabledSlots:4144959}
scoreboard players set sc_ride_free_2 Countdown 0
schedule function floaty:sched/dungeon/extra/snake/2_advance 5t replace
