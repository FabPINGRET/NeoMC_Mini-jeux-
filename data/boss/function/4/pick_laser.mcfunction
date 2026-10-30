tag @a[gamemode=!spectator,tag=bossroom,limit=1,sort=random,tag=mg.flw] add laser_picker

execute as @a[tag=laser_picker,tag=mg.flw] at @s as @e[tag=boss_ed_edge,limit=1,sort=nearest,distance=0..] if entity @s[tag=1-1] run tag @e[tag=boss_ed_edge,tag=5-1,distance=0..] add boss_ed_laser
execute as @a[tag=laser_picker,tag=mg.flw] at @s as @e[tag=boss_ed_edge,limit=1,sort=nearest,distance=0..] if entity @s[tag=1-2] run tag @e[tag=boss_ed_edge,tag=5-2,distance=0..] add boss_ed_laser
execute as @a[tag=laser_picker,tag=mg.flw] at @s as @e[tag=boss_ed_edge,limit=1,sort=nearest,distance=0..] if entity @s[tag=1-3] run tag @e[tag=boss_ed_edge,tag=5-3,distance=0..] add boss_ed_laser
execute as @a[tag=laser_picker,tag=mg.flw] at @s as @e[tag=boss_ed_edge,limit=1,sort=nearest,distance=0..] if entity @s[tag=1-4] run tag @e[tag=boss_ed_edge,tag=5-4,distance=0..] add boss_ed_laser
execute as @a[tag=laser_picker,tag=mg.flw] at @s as @e[tag=boss_ed_edge,limit=1,sort=nearest,distance=0..] if entity @s[tag=1-5] run tag @e[tag=boss_ed_edge,tag=5-5,distance=0..] add boss_ed_laser

execute as @a[tag=laser_picker,tag=mg.flw] at @s as @e[tag=boss_ed_edge,limit=1,sort=nearest,distance=0..] if entity @s[tag=5-1] run tag @e[tag=boss_ed_edge,tag=1-1,distance=0..] add boss_ed_laser
execute as @a[tag=laser_picker,tag=mg.flw] at @s as @e[tag=boss_ed_edge,limit=1,sort=nearest,distance=0..] if entity @s[tag=5-2] run tag @e[tag=boss_ed_edge,tag=1-2,distance=0..] add boss_ed_laser
execute as @a[tag=laser_picker,tag=mg.flw] at @s as @e[tag=boss_ed_edge,limit=1,sort=nearest,distance=0..] if entity @s[tag=5-3] run tag @e[tag=boss_ed_edge,tag=1-3,distance=0..] add boss_ed_laser
execute as @a[tag=laser_picker,tag=mg.flw] at @s as @e[tag=boss_ed_edge,limit=1,sort=nearest,distance=0..] if entity @s[tag=5-4] run tag @e[tag=boss_ed_edge,tag=1-4,distance=0..] add boss_ed_laser
execute as @a[tag=laser_picker,tag=mg.flw] at @s as @e[tag=boss_ed_edge,limit=1,sort=nearest,distance=0..] if entity @s[tag=5-5] run tag @e[tag=boss_ed_edge,tag=1-5,distance=0..] add boss_ed_laser

execute as @a[tag=laser_picker,tag=mg.flw] at @s as @e[tag=boss_ed_edge,limit=1,sort=nearest,distance=0..] if entity @s[tag=2-1] run tag @e[tag=boss_ed_edge,tag=2-5,distance=0..] add boss_ed_laser
execute as @a[tag=laser_picker,tag=mg.flw] at @s as @e[tag=boss_ed_edge,limit=1,sort=nearest,distance=0..] if entity @s[tag=3-1] run tag @e[tag=boss_ed_edge,tag=3-5,distance=0..] add boss_ed_laser
execute as @a[tag=laser_picker,tag=mg.flw] at @s as @e[tag=boss_ed_edge,limit=1,sort=nearest,distance=0..] if entity @s[tag=4-1] run tag @e[tag=boss_ed_edge,tag=4-5,distance=0..] add boss_ed_laser

execute as @a[tag=laser_picker,tag=mg.flw] at @s as @e[tag=boss_ed_edge,limit=1,sort=nearest,distance=0..] if entity @s[tag=2-5] run tag @e[tag=boss_ed_edge,tag=2-1,distance=0..] add boss_ed_laser
execute as @a[tag=laser_picker,tag=mg.flw] at @s as @e[tag=boss_ed_edge,limit=1,sort=nearest,distance=0..] if entity @s[tag=3-5] run tag @e[tag=boss_ed_edge,tag=3-1,distance=0..] add boss_ed_laser
execute as @a[tag=laser_picker,tag=mg.flw] at @s as @e[tag=boss_ed_edge,limit=1,sort=nearest,distance=0..] if entity @s[tag=4-5] run tag @e[tag=boss_ed_edge,tag=4-1,distance=0..] add boss_ed_laser

execute if entity @e[tag=boss_ed_laser,tag=1-1,distance=0..] run setblock -10069 95 -385 minecraft:redstone_block
execute if entity @e[tag=boss_ed_laser,tag=1-2,distance=0..] run setblock -10069 95 -385 minecraft:redstone_block
execute if entity @e[tag=boss_ed_laser,tag=1-3,distance=0..] run setblock -10069 95 -385 minecraft:redstone_block
execute if entity @e[tag=boss_ed_laser,tag=1-4,distance=0..] run setblock -10069 95 -385 minecraft:redstone_block
execute if entity @e[tag=boss_ed_laser,tag=1-5,distance=0..] run setblock -10069 95 -385 minecraft:redstone_block

execute if entity @e[tag=boss_ed_laser,tag=5-1,distance=0..] run setblock -10067 95 -385 minecraft:redstone_block
execute if entity @e[tag=boss_ed_laser,tag=5-2,distance=0..] run setblock -10067 95 -385 minecraft:redstone_block
execute if entity @e[tag=boss_ed_laser,tag=5-3,distance=0..] run setblock -10067 95 -385 minecraft:redstone_block
execute if entity @e[tag=boss_ed_laser,tag=5-4,distance=0..] run setblock -10067 95 -385 minecraft:redstone_block
execute if entity @e[tag=boss_ed_laser,tag=5-5,distance=0..] run setblock -10067 95 -385 minecraft:redstone_block

execute if entity @e[tag=boss_ed_laser,tag=2-1,distance=0..] run setblock -10063 95 -385 minecraft:redstone_block
execute if entity @e[tag=boss_ed_laser,tag=3-1,distance=0..] run setblock -10063 95 -385 minecraft:redstone_block
execute if entity @e[tag=boss_ed_laser,tag=4-1,distance=0..] run setblock -10063 95 -385 minecraft:redstone_block

execute if entity @e[tag=boss_ed_laser,tag=2-5,distance=0..] run setblock -10065 95 -385 minecraft:redstone_block
execute if entity @e[tag=boss_ed_laser,tag=3-5,distance=0..] run setblock -10065 95 -385 minecraft:redstone_block
execute if entity @e[tag=boss_ed_laser,tag=4-5,distance=0..] run setblock -10065 95 -385 minecraft:redstone_block

tag @a[tag=mg.flw] remove laser_picker
