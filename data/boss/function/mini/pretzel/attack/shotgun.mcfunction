tp @n[tag=pretzel_shotgun_man,distance=0..] -10340 90 446
tp @n[tag=pretzel_shotgun_gun,distance=0..] -10340 89.6 446
tag @r[gamemode=!spectator,tag=mg.flw] add targeted
setblock -10355 61 455 minecraft:redstone_block
particle minecraft:dust_plume -10340 91 446 0.3 1 0.3 0 100
playsound minecraft:entity.villager.celebrate hostile @a[tag=mg.flw] -10340 89 446 2 0.9
scoreboard players set pretzel_shotgun_tracking bool 1
