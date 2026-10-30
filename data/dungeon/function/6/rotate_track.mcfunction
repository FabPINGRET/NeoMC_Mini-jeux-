playsound minecraft:block.grindstone.use master @a[tag=mg.flw] ~ ~ ~ 4 0.8
clone ~ ~ ~ ~ ~ ~ ~ ~-1 ~
fill ~ ~1 ~ ~2 ~3 ~2 air

execute if block ~ ~-1 ~ white_wool run clone -10399 8 -188 -10397 11 -186 ~ ~ ~
execute if block ~ ~-1 ~ light_gray_wool run clone -10403 8 -188 -10401 11 -186 ~ ~ ~

execute if block ~ ~-1 ~ brown_wool run clone -10399 8 -192 -10397 11 -190 ~ ~ ~
execute if block ~ ~-1 ~ red_wool run clone -10403 8 -192 -10401 11 -190 ~ ~ ~

execute if block ~ ~-1 ~ gray_wool run clone -10395 8 -192 -10393 11 -190 ~ ~ ~
execute if block ~ ~-1 ~ orange_wool run clone -10391 8 -192 -10389 11 -190 ~ ~ ~
execute if block ~ ~-1 ~ yellow_wool run clone -10391 8 -188 -10389 11 -186 ~ ~ ~
execute if block ~ ~-1 ~ black_wool run clone -10395 8 -188 -10393 11 -186 ~ ~ ~

execute if block ~ ~-1 ~ cyan_wool run clone -10395 8 -200 -10393 11 -198 ~ ~ ~
execute if block ~ ~-1 ~ magenta_wool run clone -10391 8 -200 -10389 11 -198 ~ ~ ~
execute if block ~ ~-1 ~ pink_wool run clone -10391 8 -196 -10389 11 -194 ~ ~ ~
execute if block ~ ~-1 ~ light_blue_wool run clone -10395 8 -196 -10393 11 -194 ~ ~ ~

execute if block ~ ~-1 ~ lime_wool run clone -10403 8 -200 -10401 11 -198 ~ ~ ~
execute if block ~ ~-1 ~ lime_wool run setblock ~1 ~3 ~ rail[shape=north_south]
execute if block ~ ~-1 ~ blue_wool run clone -10399 8 -200 -10397 11 -198 ~ ~ ~
execute if block ~ ~-1 ~ blue_wool run setblock ~2 ~3 ~1 rail[shape=east_west]
execute if block ~ ~-1 ~ purple_wool run clone -10399 8 -196 -10397 11 -194 ~ ~ ~
execute if block ~ ~-1 ~ purple_wool run setblock ~1 ~3 ~2 rail[shape=north_south]
execute if block ~ ~-1 ~ green_wool run clone -10403 8 -196 -10401 11 -194 ~ ~ ~
execute if block ~ ~-1 ~ green_wool run setblock ~ ~3 ~1 rail[shape=east_west]

kill @n[type=item,nbt={Item:{id:"minecraft:rail"}},distance=0..]
schedule function floaty:sched/dungeon/6/kill_track 1t replace
