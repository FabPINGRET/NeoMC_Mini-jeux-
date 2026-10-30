playsound minecraft:block.amethyst_block.fall neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

tag @s add mlc_tag

tellraw @a[tag=mlc_tag,tag=mg.flw] [{"text":"<"},{"text":"Moonlight Nexus","color":"aqua"},{"text":"> Ok, I'll follow you, but you had better stay on ","color":"white"},{"text":"Waxwane Brick","color":"aqua"},{"text":"!","color":"white"}]

summon armor_stand ~ ~ ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["mlc_tracker","mlc_moon"]}
summon armor_stand ~ ~ ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["mlc_main","mlc_moon"],DisabledSlots:4144959,equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{id:[I;-1531356392,10633216,-2053431415,1006290370],properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNjJkNWQ5ZDQxZDE5MTdmODZkODIyZDEzZDI2YWEwN2VlNmRlZmVjY2RhMWM5ODg1MDVhYjg2NGFmZTk4YTYwNSJ9fX0="}]}}}}}

setblock -9766 273 431 minecraft:redstone_block

kill @e[tag=mlc_display,distance=0..]

fill 9959 58 12 9959 58 13 air
setblock 9960 58 14 air
