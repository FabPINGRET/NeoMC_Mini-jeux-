execute positioned -12341 213 -244 run tag @p[tag=mg.flw] add sc_snake_captain_1
setblock -12341 212 -246 minecraft:purple_wool strict
summon armor_stand -12341 212 -246 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_1","1"],DisabledSlots:4144959}
summon armor_stand -12341 212 -246 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_1","2"],DisabledSlots:4144959}
summon armor_stand -12341 212 -246 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_1","3"],DisabledSlots:4144959}
summon armor_stand -12341 212 -246 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_1","4"],DisabledSlots:4144959}
summon armor_stand -12341 212 -246 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_1","5"],DisabledSlots:4144959}
summon armor_stand -12341 212 -246 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_1","6"],DisabledSlots:4144959}
summon armor_stand -12341 212 -246 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_snake_ride_1","7"],DisabledSlots:4144959}
scoreboard players set sc_ride_free_1 Countdown 0
schedule function floaty:sched/dungeon/extra/snake/1_advance 5t replace
