execute as @n[tag=threnodist_stand,distance=0..] at @s run particle minecraft:portal ~ ~1.5 ~ 0 0 0 0.5 200
execute as @n[tag=threnodist_stand,distance=0..] at @s run playsound minecraft:entity.enderman.teleport hostile @a[tag=mg.flw] ~ ~ ~ 2 0.7

execute as @e[tag=thren_stand_decoy,distance=0..] at @s run particle minecraft:portal ~ ~1.5 ~ 0 0 0 0.5 200
execute as @e[tag=thren_stand_decoy,distance=0..] at @s run playsound minecraft:entity.enderman.teleport hostile @a[tag=mg.flw] ~ ~ ~ 2 0.7

spreadplayers -11144 430 7 18 false @e[tag=thren_rand,distance=0..]
execute as @e[tag=thren_rand,distance=0..] at @s if block ~ 124 ~ glass run tag @s add viable
tag @e[tag=thren_rand,tag=viable,sort=random,limit=1,distance=0..] add loc_1
execute as @e[tag=thren_rand,tag=loc_1,distance=0..] at @s run tp @n[tag=threnodist_stand,distance=0..] ~ 58 ~
tag @e[tag=thren_rand,tag=loc_1,distance=0..] remove viable
tag @e[tag=thren_rand,tag=loc_1,distance=0..] remove loc_1

tag @e[tag=thren_stand_decoy,sort=random,limit=1,distance=0..] add chosen_1

tag @e[tag=thren_rand,tag=viable,sort=random,limit=1,distance=0..] add loc_2
execute as @e[tag=thren_rand,tag=loc_2,distance=0..] at @s run tp @n[tag=thren_stand_decoy,tag=chosen_1,distance=0..] ~ 58 ~
tag @e[tag=thren_rand,tag=loc_2,distance=0..] remove viable
tag @e[tag=thren_rand,tag=loc_2,distance=0..] remove loc_2

tag @e[tag=thren_stand_decoy,tag=!chosen_1,sort=random,limit=1,distance=0..] add chosen_2

tag @e[tag=thren_rand,tag=viable,sort=random,limit=1,distance=0..] add loc_3
execute as @e[tag=thren_rand,tag=loc_3,distance=0..] at @s run tp @n[tag=thren_stand_decoy,tag=chosen_2,distance=0..] ~ 58 ~
tag @e[tag=thren_rand,tag=loc_3,distance=0..] remove viable
tag @e[tag=thren_rand,tag=loc_3,distance=0..] remove loc_3
tag @e[tag=thren_rand,tag=viable,sort=random,limit=1,distance=0..] add loc_4

tag @e[tag=thren_stand_decoy,tag=!chosen_1,tag=!chosen_2,sort=random,limit=1,distance=0..] add chosen_3

execute as @e[tag=thren_rand,tag=loc_4,distance=0..] at @s run tp @n[tag=thren_stand_decoy,tag=chosen_3,distance=0..] ~ 58 ~
tag @e[tag=thren_rand,tag=loc_4,distance=0..] remove viable
tag @e[tag=thren_rand,tag=loc_4,distance=0..] remove loc_4


tag @e[tag=thren_rand,distance=0..] remove viable
tag @e[tag=thren_stand_decoy,distance=0..] remove chosen_1
tag @e[tag=thren_stand_decoy,distance=0..] remove chosen_2
tag @e[tag=thren_stand_decoy,distance=0..] remove chosen_3
