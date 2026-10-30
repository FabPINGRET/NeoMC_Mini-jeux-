playsound minecraft:block.trial_spawner.spawn_item hostile @a[tag=mg.flw] ~ ~ ~ 3 1
particle dust_color_transition{from_color:[0.000,0.000,0.000],scale:2,to_color:[1.000,1.000,0.000]} ~ ~ ~ 0.1 0.1 0.1 0 1

# summon the temporary entity
summon marker ^ ^ ^3 {Tags:["direction"]}

# get the coordinates of the boss and the entity
execute store result score #playerX Value run data get entity @s Pos[0] 1000
execute store result score #playerY Value run data get entity @s Pos[1] 1000
execute store result score #playerZ Value run data get entity @s Pos[2] 1000
execute store result score #targetX Value as @e[type=marker,tag=direction,limit=1,distance=0..] run data get entity @s Pos[0] 1000
execute store result score #targetY Value as @e[type=marker,tag=direction,limit=1,distance=0..] run data get entity @s Pos[1] 1000
execute store result score #targetZ Value as @e[type=marker,tag=direction,limit=1,distance=0..] run data get entity @s Pos[2] 1000

# do the math
scoreboard players operation #targetX Value -= #playerX Value
scoreboard players operation #targetY Value -= #playerY Value
scoreboard players operation #targetZ Value -= #playerZ Value

# summon the projectile entity
summon arrow ~ ~ ~ {NoGravity:1b,SoundEvent:"particle.soul_escape",damage:4d,pickup:2b,shake:1b,Tags:["projectile","wailing_arrow"]}
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[0] float 1 run data get entity @s Rotation[0] 1
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[1] float 1 run data get entity @s Rotation[1] 1
data modify entity @e[limit=1,tag=projectile,distance=0..] Owner set from entity @n[tag=ta_boss_name,distance=0..] UUID

# apply motion to projectile
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[0] double 0.001 run scoreboard players get #targetX Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[1] double 0.001 run scoreboard players get #targetY Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[2] double 0.001 run scoreboard players get #targetZ Value

# clean up
tag @e[tag=projectile,distance=0..] remove projectile
kill @e[tag=direction,distance=0..]
