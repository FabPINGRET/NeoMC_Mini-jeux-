scoreboard players set ios_humor bool 0
execute if block 9986 36 226 minecraft:yellow_wool if block 9986 36 225 minecraft:black_wool if block 9986 36 224 minecraft:blue_wool if block 9986 36 223 minecraft:yellow_wool if block 9986 36 222 minecraft:red_wool run scoreboard players set ios_humor bool 1

fill 9987 37 222 9987 37 226 minecraft:black_concrete

execute if block 9986 36 226 yellow_wool run setblock 9987 37 226 minecraft:red_concrete
execute if block 9986 36 226 black_wool run setblock 9987 37 226 minecraft:white_concrete
execute if block 9986 36 226 blue_wool run setblock 9987 37 226 minecraft:white_concrete
execute if block 9986 36 226 red_wool run setblock 9987 37 226 minecraft:white_concrete

execute if block 9986 36 225 yellow_wool run setblock 9987 37 225 minecraft:white_concrete
execute if block 9986 36 225 black_wool run setblock 9987 37 225 minecraft:red_concrete
execute if block 9986 36 225 blue_wool run setblock 9987 37 225 minecraft:white_concrete
execute if block 9986 36 225 red_wool run setblock 9987 37 225 minecraft:white_concrete

execute if block 9986 36 224 yellow_wool run setblock 9987 37 224 minecraft:white_concrete
execute if block 9986 36 224 black_wool run setblock 9987 37 224 minecraft:white_concrete
execute if block 9986 36 224 blue_wool run setblock 9987 37 224 minecraft:red_concrete
execute if block 9986 36 224 red_wool run setblock 9987 37 224 minecraft:white_concrete

execute if block 9986 36 223 yellow_wool run setblock 9987 37 223 minecraft:red_concrete
execute if block 9986 36 223 black_wool run setblock 9987 37 223 minecraft:white_concrete
execute if block 9986 36 223 blue_wool run setblock 9987 37 223 minecraft:white_concrete
execute if block 9986 36 223 red_wool run setblock 9987 37 223 minecraft:white_concrete

execute if block 9986 36 222 yellow_wool run setblock 9987 37 222 minecraft:white_concrete
execute if block 9986 36 222 black_wool run setblock 9987 37 222 minecraft:white_concrete
execute if block 9986 36 222 blue_wool run setblock 9987 37 222 minecraft:white_concrete
execute if block 9986 36 222 red_wool run setblock 9987 37 222 minecraft:red_concrete

playsound minecraft:entity.evoker.prepare_summon master @a[tag=mg.flw] 9992 35 215 1 2

execute if score ios_humor bool matches 0 run particle minecraft:large_smoke 9992 37 215 0.2 0.5 0.2 0.1 200
execute if score ios_humor bool matches 0 positioned 9992 36 215 run function summon:dyscrasian_homuncule

execute if score ios_humor bool matches 1 run particle cloud 9992 37 215 0.2 0.5 0.2 0.1 200
execute if score ios_humor bool matches 1 positioned 9992 36 215 run function summon:eucrasian_homuncule

execute if score ios_humor bool matches 1 run scoreboard players set ios_humor_created bool 1
