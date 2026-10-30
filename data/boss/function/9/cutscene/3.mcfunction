summon armor_stand -11223 -20 -109 {NoGravity:1b,Silent:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,PersistenceRequired:1b,Tags:["boss_wm_cutscene"],DisabledSlots:4144959,Rotation:[-90F,0F],equipment:{feet:{id:"minecraft:leather_boots",count:1,components:{"minecraft:dyed_color":1908001,"minecraft:trim":{material:"minecraft:lapis",pattern:"minecraft:ward"}}},legs:{id:"minecraft:leather_leggings",count:1,components:{"minecraft:dyed_color":1481884}},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":16383998,"minecraft:trim":{material:"minecraft:copper",pattern:"minecraft:host"}}},head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMWMyODE4ZmIxNjNmZGFhMzE2MjM3MWU3OWQyMThmNDZiM2QxZThkYTYzMmRjYzk1MzJiYjVlY2E4OWRlNDMyIn19fQ=="}]}}},mainhand:{id:"minecraft:trident",count:1}}}
setblock -11243 -34 -132 minecraft:redstone_block

playsound minecraft:entity.enderman.teleport hostile @a[tag=mg.flw] -11223 -20 -109 3 1 1
playsound minecraft:block.conduit.attack.target hostile @a[tag=mg.flw] -11223 -20 -109 3 0.1 1
playsound minecraft:block.conduit.attack.target hostile @a[tag=mg.flw] -11223 -20 -109 3 1 1
playsound minecraft:block.conduit.attack.target hostile @a[tag=mg.flw] -11223 -20 -109 3 2 1

particle minecraft:dust_pillar{block_state:"water"} -11223 -20 -109 0.5 0.1 0.5 0 100 force
particle splash -11223 -20 -109 0.3 0.8 0.3 0 100 force

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/4 3s
