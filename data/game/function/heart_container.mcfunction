summon armor_stand ~ ~ ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["heart_container"],DisabledSlots:4144959,equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzQ2ZDg3NzY4MGM5ODQ3MTc2Mzc3YTFhMTQ1YmYwZGMyM2RhM2Q0MGRiNzQ0YmIyMmRlNDljNzUyMzQwZWU4MSJ9fX0="}]}}}}}
fill -9761 280 417 -9767 280 417 minecraft:redstone_block
setblock -9776 280 416 minecraft:redstone_block
execute as @e[tag=heart_container,distance=0..] at @s run particle minecraft:end_rod ~ ~2 ~ 0 0 0 0.3 100 force
tag @a[gamemode=!spectator,tag=mg.flw] remove bossroom
