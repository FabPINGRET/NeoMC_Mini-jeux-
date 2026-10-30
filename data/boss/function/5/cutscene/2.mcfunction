summon armor_stand -10222 93 427 {NoGravity:1b,Silent:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,PersistenceRequired:1b,Tags:["boss_skt_cutscene"],DisabledSlots:4144959,Rotation:[180F,0F],equipment:{feet:{id:"minecraft:leather_boots",count:1,components:{"minecraft:dyed_color":4862235,"minecraft:trim":{material:"minecraft:emerald",pattern:"minecraft:flow"}}},legs:{id:"minecraft:leather_leggings",count:1,components:{"minecraft:dyed_color":4862235,"minecraft:trim":{material:"minecraft:emerald",pattern:"minecraft:flow"}}},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":4862235,"minecraft:trim":{material:"minecraft:emerald",pattern:"minecraft:flow"}}},head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{id:[I;-417552618,-1843115745,-1484175063,-2140311761],properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMmNjYmI4NmNiMzgyNDAzYjYwNDY5ZjlkNWFmMjkxMGYyYTk5ZGIyZGU0YmIwMzA5MGYxOWUzZWViZDQ1OTgifX19"}]}}}}}
particle minecraft:totem_of_undying -10222 94 427 0.2 0.2 0.2 0.5 100 force
playsound minecraft:item.chorus_fruit.teleport master @a[tag=mg.flw] -10222 94 427 4 1
setblock -10197 55 407 minecraft:redstone_block

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/5/cutscene/3 3s
