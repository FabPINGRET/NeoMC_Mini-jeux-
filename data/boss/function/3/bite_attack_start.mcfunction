tag @r[tag=bossroom,gamemode=!spectator,tag=mg.flw] add lod_boss_ptarget

execute as @a[tag=bossroom,gamemode=!spectator,tag=lod_boss_ptarget,tag=mg.flw] at @s if block ~ 130 ~ minecraft:blue_wool if block -10083 158 -184 sand run summon armor_stand ~ 159 ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,Tags:["lod_boss_target","temp_target"],DisabledSlots:4144959}

execute as @a[tag=bossroom,gamemode=!spectator,tag=lod_boss_ptarget,tag=mg.flw] at @s if block ~ 130 ~ minecraft:blue_wool if block -10083 158 -184 air run summon armor_stand ~ 146 ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,Tags:["lod_boss_target","temp_target"],DisabledSlots:4144959}

execute as @e[tag=temp_target,distance=0..] at @s align xz run tp @s ~0.5 ~ ~0.5

execute as @a[tag=bossroom,gamemode=!spectator,tag=lod_boss_ptarget,tag=mg.flw] at @s unless block ~ 130 ~ minecraft:blue_wool run tag @e[sort=nearest,limit=1,tag=lod_boss_border,distance=0..] add lod_boss_target

execute if entity @e[tag=lod_boss_target,distance=0..] run setblock -10083 134 -211 minecraft:redstone_block
execute if entity @e[tag=lod_boss_target,distance=0..] run setblock -10083 134 -209 minecraft:redstone_block

execute unless entity @e[tag=lod_boss_target,distance=0..] run setblock -10083 134 -201 minecraft:redstone_block

tag @a[tag=mg.flw] remove lod_boss_ptarget
