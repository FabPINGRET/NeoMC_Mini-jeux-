playsound minecraft:entity.firework_rocket.twinkle master @a[tag=mg.flw] ~ ~ ~ 1 2
playsound minecraft:entity.generic.explode master @a[tag=mg.flw] ~ ~ ~ 1 1.5

clear @s arrow 1

#-------------------------------------------------- 1

# summon the temporary entity
summon marker ^ ^ ^2.5 {Tags:["direction"]}

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
summon arrow ~ ~1.5 ~ {pickup:2b,damage:2d,crit:1b,Tags:["projectile"],SoundEvent:"block.chain.hit"}
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[0] float 1 run data get entity @s Rotation[0] 1
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[1] float 1 run data get entity @s Rotation[1] 1
data modify entity @e[limit=1,tag=projectile,distance=0..] Owner set from entity @s UUID

# apply motion to projectile
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[0] double 0.001 run scoreboard players get #targetX Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[1] double 0.001 run scoreboard players get #targetY Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[2] double 0.001 run scoreboard players get #targetZ Value

# clean up
tag @e[tag=projectile,distance=0..] remove projectile
kill @e[tag=direction,distance=0..]

#-------------------------------------------------- 2

# summon the temporary entity
summon marker ^ ^0.18 ^2.5 {Tags:["direction"]}

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
summon arrow ~ ~1.5 ~ {pickup:2b,damage:2d,crit:1b,Tags:["projectile"],SoundEvent:"block.chain.hit"}
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[0] float 1 run data get entity @s Rotation[0] 1
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[1] float 1 run data get entity @s Rotation[1] 1
data modify entity @e[limit=1,tag=projectile,distance=0..] Owner set from entity @s UUID

# apply motion to projectile
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[0] double 0.001 run scoreboard players get #targetX Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[1] double 0.001 run scoreboard players get #targetY Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[2] double 0.001 run scoreboard players get #targetZ Value

# clean up
tag @e[tag=projectile,distance=0..] remove projectile
kill @e[tag=direction,distance=0..]

#-------------------------------------------------- 3

# summon the temporary entity
summon marker ^ ^-0.18 ^2.5 {Tags:["direction"]}

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
summon arrow ~ ~1.5 ~ {pickup:2b,damage:2d,crit:1b,Tags:["projectile"],SoundEvent:"block.chain.hit"}
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[0] float 1 run data get entity @s Rotation[0] 1
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[1] float 1 run data get entity @s Rotation[1] 1
data modify entity @e[limit=1,tag=projectile,distance=0..] Owner set from entity @s UUID

# apply motion to projectile
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[0] double 0.001 run scoreboard players get #targetX Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[1] double 0.001 run scoreboard players get #targetY Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[2] double 0.001 run scoreboard players get #targetZ Value

# clean up
tag @e[tag=projectile,distance=0..] remove projectile
kill @e[tag=direction,distance=0..]

#-------------------------------------------------- 4

# summon the temporary entity
summon marker ^0.18 ^ ^2.5 {Tags:["direction"]}

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
summon arrow ~ ~1.5 ~ {pickup:2b,damage:2d,crit:1b,Tags:["projectile"],SoundEvent:"block.chain.hit"}
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[0] float 1 run data get entity @s Rotation[0] 1
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[1] float 1 run data get entity @s Rotation[1] 1
data modify entity @e[limit=1,tag=projectile,distance=0..] Owner set from entity @s UUID

# apply motion to projectile
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[0] double 0.001 run scoreboard players get #targetX Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[1] double 0.001 run scoreboard players get #targetY Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[2] double 0.001 run scoreboard players get #targetZ Value

# clean up
tag @e[tag=projectile,distance=0..] remove projectile
kill @e[tag=direction,distance=0..]

#-------------------------------------------------- 5

# summon the temporary entity
summon marker ^0.15 ^0.15 ^2.5 {Tags:["direction"]}

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
summon arrow ~ ~1.5 ~ {pickup:2b,damage:2d,crit:1b,Tags:["projectile"],SoundEvent:"block.chain.hit"}
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[0] float 1 run data get entity @s Rotation[0] 1
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[1] float 1 run data get entity @s Rotation[1] 1
data modify entity @e[limit=1,tag=projectile,distance=0..] Owner set from entity @s UUID

# apply motion to projectile
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[0] double 0.001 run scoreboard players get #targetX Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[1] double 0.001 run scoreboard players get #targetY Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[2] double 0.001 run scoreboard players get #targetZ Value

# clean up
tag @e[tag=projectile,distance=0..] remove projectile
kill @e[tag=direction,distance=0..]

#-------------------------------------------------- 6

# summon the temporary entity
summon marker ^0.15 ^-0.15 ^2.5 {Tags:["direction"]}

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
summon arrow ~ ~1.5 ~ {pickup:2b,damage:2d,crit:1b,Tags:["projectile"],SoundEvent:"block.chain.hit"}
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[0] float 1 run data get entity @s Rotation[0] 1
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[1] float 1 run data get entity @s Rotation[1] 1
data modify entity @e[limit=1,tag=projectile,distance=0..] Owner set from entity @s UUID

# apply motion to projectile
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[0] double 0.001 run scoreboard players get #targetX Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[1] double 0.001 run scoreboard players get #targetY Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[2] double 0.001 run scoreboard players get #targetZ Value

# clean up
tag @e[tag=projectile,distance=0..] remove projectile
kill @e[tag=direction,distance=0..]

#-------------------------------------------------- 7

# summon the temporary entity
summon marker ^-0.18 ^ ^2.5 {Tags:["direction"]}

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
summon arrow ~ ~1.5 ~ {pickup:2b,damage:2d,crit:1b,Tags:["projectile"],SoundEvent:"block.chain.hit"}
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[0] float 1 run data get entity @s Rotation[0] 1
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[1] float 1 run data get entity @s Rotation[1] 1
data modify entity @e[limit=1,tag=projectile,distance=0..] Owner set from entity @s UUID

# apply motion to projectile
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[0] double 0.001 run scoreboard players get #targetX Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[1] double 0.001 run scoreboard players get #targetY Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[2] double 0.001 run scoreboard players get #targetZ Value

# clean up
tag @e[tag=projectile,distance=0..] remove projectile
kill @e[tag=direction,distance=0..]

#-------------------------------------------------- 8

# summon the temporary entity
summon marker ^-0.15 ^0.15 ^2.5 {Tags:["direction"]}

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
summon arrow ~ ~1.5 ~ {pickup:2b,damage:2d,crit:1b,Tags:["projectile"],SoundEvent:"block.chain.hit"}
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[0] float 1 run data get entity @s Rotation[0] 1
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[1] float 1 run data get entity @s Rotation[1] 1
data modify entity @e[limit=1,tag=projectile,distance=0..] Owner set from entity @s UUID

# apply motion to projectile
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[0] double 0.001 run scoreboard players get #targetX Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[1] double 0.001 run scoreboard players get #targetY Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[2] double 0.001 run scoreboard players get #targetZ Value

# clean up
tag @e[tag=projectile,distance=0..] remove projectile
kill @e[tag=direction,distance=0..]

#-------------------------------------------------- 9

# summon the temporary entity
summon marker ^-0.15 ^-0.15 ^2.5 {Tags:["direction"]}

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
summon arrow ~ ~1.5 ~ {pickup:2b,damage:2d,crit:1b,Tags:["projectile"],SoundEvent:"block.chain.hit"}
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[0] float 1 run data get entity @s Rotation[0] 1
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Rotation[1] float 1 run data get entity @s Rotation[1] 1
data modify entity @e[limit=1,tag=projectile,distance=0..] Owner set from entity @s UUID

# apply motion to projectile
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[0] double 0.001 run scoreboard players get #targetX Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[1] double 0.001 run scoreboard players get #targetY Value
execute store result entity @n[type=arrow,tag=projectile,distance=0..] Motion[2] double 0.001 run scoreboard players get #targetZ Value

# clean up
tag @e[tag=projectile,distance=0..] remove projectile
kill @e[tag=direction,distance=0..]

