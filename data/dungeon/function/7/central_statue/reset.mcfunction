# Clone Fists
clone -10244 78 -400 -10238 84 -397 -10248 121 -401
clone -10244 78 -395 -10238 84 -392 -10248 121 -358
clone -10244 78 -390 -10238 84 -387 -10290 121 -358
clone -10244 78 -385 -10238 84 -382 -10290 121 -401

# Clear Cages
fill -10243 95 -401 -10289 95 -355 air replace minecraft:tuff_brick_wall
fill -10243 96 -358 -10247 101 -356 air
fill -10244 96 -359 -10246 101 -355 air
fill -10243 96 -400 -10247 101 -398 air
fill -10244 96 -401 -10246 101 -397 air
fill -10285 96 -400 -10289 101 -398 air
fill -10286 96 -401 -10288 101 -397 air
fill -10285 96 -358 -10289 101 -356 air
fill -10286 96 -359 -10288 101 -355 air
fill -10245 96 -357 -10287 105 -399 air replace minecraft:iron_chain

# Clone Cages
clone -10244 78 -406 -10240 84 -402 -10247 105 -401
clone -10244 78 -406 -10240 84 -402 -10247 105 -359
clone -10244 78 -406 -10240 84 -402 -10289 105 -359
clone -10244 78 -406 -10240 84 -402 -10289 105 -401

fill -10287 112 -399 -10287 174 -399 iron_chain
fill -10287 112 -357 -10287 174 -357 iron_chain
fill -10245 112 -357 -10245 174 -357 iron_chain
fill -10245 112 -399 -10245 174 -399 iron_chain

#Return Armor Stands
execute as @n[tag=st_mirror,tag=st_central_a,distance=0..] run tp @s -10287 107 -399
execute as @n[tag=st_mirror,tag=st_central_b,distance=0..] run tp @s -10287 107 -357
execute as @n[tag=st_mirror,tag=st_central_c,distance=0..] run tp @s -10245 107 -357
execute as @n[tag=st_mirror,tag=st_central_d,distance=0..] run tp @s -10245 107 -399

data modify entity @n[tag=st_mirror,tag=st_central_a,distance=0..] NoGravity set value 0
data modify entity @n[tag=st_mirror,tag=st_central_b,distance=0..] NoGravity set value 0
data modify entity @n[tag=st_mirror,tag=st_central_c,distance=0..] NoGravity set value 0
data modify entity @n[tag=st_mirror,tag=st_central_d,distance=0..] NoGravity set value 0

#Reset landed checks
setblock -10289 91 -398 air
setblock -10290 91 -356 air
setblock -10247 91 -356 air
setblock -10247 91 -398 air

fill -10248 96 -377 -10252 96 -379 minecraft:lime_stained_glass
