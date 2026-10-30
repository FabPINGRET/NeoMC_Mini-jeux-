tag @e[tag=simpletoid,distance=0..] remove running

tp @n[tag=simpletoid,tag=1,distance=0..] 9959 40 -52 180 0
tp @n[tag=simpletoid,tag=2,distance=0..] 9958 40 -52 180 0
tp @n[tag=simpletoid,tag=3,distance=0..] 9957 40 -52 180 0

#bool (mode)
execute as @e[tag=simpletoid,distance=0..] run scoreboard players set @s bool 0
#Value (speed)
execute as @e[tag=simpletoid,distance=0..] run scoreboard players set @s Value 0

execute as @e[tag=simpletoid_pivot_a,distance=0..] at @s run tp @s ~ ~ ~ -90 0
execute as @e[tag=simpletoid_pivot_b,distance=0..] at @s run tp @s ~ ~ ~ 90 0

setblock 9955 36 -52 minecraft:air
execute as @e[tag=simpletoid,distance=0..] run data modify entity @s Pose set value {}

tag @e[tag=simpletoid,distance=0..] remove winner
tag @e[tag=simpletoid,distance=0..] remove loser

scoreboard players set simpletoid_bet Value 0
#scoreboard players set simpletoid_force_winner Value 0
scoreboard players set simpletoid_winner Value 0
