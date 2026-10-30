summon marker -10472 -18 -368 {NoGravity:1b,Silent:1b,Invulnerable:1b,Tags:["st_hand_dest_1","st_hand_dest"]}
summon marker -10474 -14 -371 {NoGravity:1b,Silent:1b,Invulnerable:1b,Tags:["st_hand_dest_2","st_hand_dest"]}
summon marker -10474 -14 -385 {NoGravity:1b,Silent:1b,Invulnerable:1b,Tags:["st_hand_dest_3","st_hand_dest"]}
summon marker -10472 -18 -388 {NoGravity:1b,Silent:1b,Invulnerable:1b,Tags:["st_hand_dest_4","st_hand_dest"]}

summon armor_stand -10472 -30 -368 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["st_hand_inter_1","st_hand_inter"],DisabledSlots:4144959}
summon armor_stand -10474 -30 -371 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["st_hand_inter_2","st_hand_inter"],DisabledSlots:4144959}
summon armor_stand -10474 -30 -385 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["st_hand_inter_3","st_hand_inter"],DisabledSlots:4144959}
summon armor_stand -10472 -30 -388 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["st_hand_inter_4","st_hand_inter"],DisabledSlots:4144959}

summon armor_stand -10472 -30 -368 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["st_hand_loc_1","st_hand_loc"],DisabledSlots:4144959,CustomName:'{"bold":true,"color":"gray","text":"Hollow Watcher"}'}
summon armor_stand -10474 -30 -371 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["st_hand_loc_2","st_hand_loc"],DisabledSlots:4144959,CustomName:'{"bold":true,"color":"gray","text":"Hollow Watcher"}'}
summon armor_stand -10474 -30 -385 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["st_hand_loc_3","st_hand_loc"],DisabledSlots:4144959,CustomName:'{"bold":true,"color":"gray","text":"Hollow Watcher"}'}
summon armor_stand -10472 -30 -388 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["st_hand_loc_4","st_hand_loc"],DisabledSlots:4144959,CustomName:'{"bold":true,"color":"gray","text":"Hollow Watcher"}'}

execute as @e[tag=st_hand_loc,distance=0..] run function boss:7/hand_frame/crystal

function boss:7/body_frame/0

summon armor_stand -10473 -20 -378 {NoGravity:1b,Silent:1b,Invulnerable:1b,ShowArms:0b,Small:1b,NoBasePlate:0b,PersistenceRequired:1b,Tags:["st_boss_statue","dominion_trigger"],DisabledSlots:4144959,Rotation:[-90F,0F],equipment:{feet:{id:"minecraft:netherite_boots",count:1,components:{"minecraft:trim":{material:"minecraft:iron",pattern:"minecraft:spire"}}},legs:{id:"minecraft:netherite_leggings",count:1,components:{"minecraft:trim":{material:"minecraft:iron",pattern:"minecraft:spire"}}},chest:{id:"minecraft:netherite_chestplate",count:1,components:{"minecraft:trim":{material:"minecraft:iron",pattern:"minecraft:spire"}}},head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{id:[I;1080111988,1100367586,-1845895429,-1077775666],properties:[{name:"textures",value:"ewogICJ0aW1lc3RhbXAiIDogMTczMjAzNjMwNzgyMywKICAicHJvZmlsZUlkIiA6ICJhODgyMzAzMDVkOWY0ODRiYjNjNjc2OTg1OTYxYjc2YSIsCiAgInByb2ZpbGVOYW1lIiA6ICJMb3JkRHJld3BpY3VzIiwKICAic2lnbmF0dXJlUmVxdWlyZWQiIDogdHJ1ZSwKICAidGV4dHVyZXMiIDogewogICAgIlNLSU4iIDogewogICAgICAidXJsIiA6ICJodHRwOi8vdGV4dHVyZXMubWluZWNyYWZ0Lm5ldC90ZXh0dXJlL2YwYTFmNmJjNTlhZmJlMTY1NDYzY2M2OWM2ZTc0YjNiZDQxMjkxN2ZhY2YxOGVmZWEzZGNlOTFhZmE3ZWM4YzAiCiAgICB9CiAgfQp9"}]}}}}}

summon armor_stand -10473 -24 -378 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["st_boss_center_pos"],DisabledSlots:4144959}
