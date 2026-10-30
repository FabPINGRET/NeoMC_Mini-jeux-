playsound minecraft:entity.warden.sonic_boom master @a[tag=mg.flw] -11830 219 330 3 0.4

summon armor_stand -11830 217 330 {Silent:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,PersistenceRequired:1b,Tags:["boss_ta_cutscene_stand"],attributes:[{id:"minecraft:scale",base:3}],DisabledSlots:4144959,Rotation:[-90F,0F],equipment:{feet:{id:"minecraft:leather_boots",count:1,components:{"minecraft:dyed_color":0,"minecraft:trim":{material:"minecraft:gold",pattern:"minecraft:flow"}}},legs:{id:"minecraft:leather_leggings",count:1,components:{"minecraft:dyed_color":0,"minecraft:trim":{material:"minecraft:gold",pattern:"minecraft:silence"}}},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":0,"minecraft:trim":{material:"minecraft:gold",pattern:"minecraft:flow"}}},head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{"properties":[{"name":"textures","value":"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzViNWRiM2ZkNWMyY2IzMjViOGI3MzAyNjZkZWE1MzgzNzBiMzQ4NGM0YWFkZjM4MDhkZDYxNDBmOWM3NDYwMiJ9fX0"}]}}},mainhand:{id:"minecraft:golden_sword",count:1},offhand:{id:"minecraft:golden_sword",count:1}},CustomName:{"color":"yellow","text":"Lord of Smoke"}}

setblock -11798 203 360 minecraft:redstone_block

particle sculk_soul -11830 219 330 1 2 1 0.2 300
particle minecraft:large_smoke -11830 219 330 1 2 1 0.1 300

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/10/cutscene/7 4s

#","color":"white"},{"text":"
