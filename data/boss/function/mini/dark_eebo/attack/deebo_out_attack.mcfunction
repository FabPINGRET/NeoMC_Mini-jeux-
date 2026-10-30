execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s run tp @n[tag=deebo_stand,distance=0..] ~ ~-0.5 ~

execute at @n[tag=deebo_marker,tag=active,distance=0..] run particle dust_color_transition{from_color:[0.098,0.604,0.820],to_color:[0.110,0.808,0.859],scale:3} ~ ~0.5 ~ 0.3 0.3 0.3 0 50 normal
execute at @n[tag=deebo_marker,tag=active,distance=0..] run playsound minecraft:entity.enderman.teleport hostile @a[tag=mg.flw] ~ 186 ~ 1 1
execute at @n[tag=deebo_marker,tag=active,distance=0..] run playsound minecraft:entity.witch.ambient hostile @a[tag=mg.flw] ~ 186 ~ 1 1.7

function boss:mini/dark_eebo/painting/clear
tag @e[tag=deebo,distance=0..] remove active
tag @e[tag=deebo_marker,distance=0..] remove active

#start lasers
setblock -11549 173 -173 stone
setblock -11552 173 -175 minecraft:redstone_block

execute if score boss:deebo BossHealth matches 6 if block -11547 173 -171 lime_wool run function boss:mini/dark_eebo/cutscene_1


execute if score boss:deebo BossHealth matches 6 if block -11547 173 -171 lime_wool run setblock -11547 173 -171 pink_wool
execute if score boss:deebo BossHealth matches 6 if block -11547 173 -171 orange_wool run setblock -11547 173 -171 lime_wool
execute if score boss:deebo BossHealth matches 6 if block -11547 173 -171 purple_wool run setblock -11547 173 -171 orange_wool
execute if score boss:deebo BossHealth matches 6 if block -11547 173 -171 white_wool run setblock -11547 173 -171 purple_wool
execute if score boss:deebo BossHealth matches 6 if block -11547 173 -171 red_wool run setblock -11547 173 -171 white_wool
execute if score boss:deebo BossHealth matches 6 if block -11547 173 -171 green_wool run setblock -11547 173 -171 red_wool
execute if score boss:deebo BossHealth matches 6 if block -11547 173 -171 blue_wool run setblock -11547 173 -171 green_wool
execute if score boss:deebo BossHealth matches 6 if block -11547 173 -171 black_wool run setblock -11547 173 -171 blue_wool
