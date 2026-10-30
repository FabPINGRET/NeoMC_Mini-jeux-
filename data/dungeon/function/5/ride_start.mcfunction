execute positioned -10280 113 299 run tag @p[tag=mg.flw] add skt_snake_captain
setblock -10282 112 299 minecraft:moss_block
summon armor_stand -10282 112 299 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["skt_snake_ride","1"],DisabledSlots:4144959}
summon armor_stand -10282 112 299 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["skt_snake_ride","2"],DisabledSlots:4144959}
summon armor_stand -10282 112 299 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["skt_snake_ride","3"],DisabledSlots:4144959}
summon armor_stand -10282 112 299 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["skt_snake_ride","4"],DisabledSlots:4144959}
summon armor_stand -10282 112 299 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["skt_snake_ride","5"],DisabledSlots:4144959}
summon armor_stand -10282 112 299 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["skt_snake_ride","6"],DisabledSlots:4144959}
summon armor_stand -10282 112 299 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["skt_snake_ride","7"],DisabledSlots:4144959}
scoreboard players set skt_ride_free Countdown 0
schedule function floaty:sched/dungeon/5/ride_advance 5t replace
