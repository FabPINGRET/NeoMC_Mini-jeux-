tag @e[tag=thren_stand_decoy,sort=random,limit=1,distance=0..] add 1
tag @e[tag=thren_stand_decoy,sort=random,limit=1,tag=!1,distance=0..] add 2
tag @e[tag=thren_stand_decoy,sort=random,limit=1,tag=!1,tag=!2,distance=0..] add 3

execute positioned -11144 21 430 as @n[tag=threnodist_decoy,distance=0..] run tp @s @n[tag=thren_stand_decoy,tag=1,distance=0..]
execute positioned -11144 21 430 as @n[tag=threnodist_decoy,distance=0..] run tp @s @n[tag=thren_stand_decoy,tag=2,distance=0..]
execute positioned -11144 21 430 as @n[tag=threnodist_decoy,distance=0..] run tp @s @n[tag=thren_stand_decoy,tag=3,distance=0..]
tp @n[tag=threnodist_boss,distance=0..] @n[tag=threnodist_stand,distance=0..]

execute as @n[tag=threnodist_stand,distance=0..] at @s run particle minecraft:portal ~ ~1.5 ~ 0 0 0 0.5 100
execute as @n[tag=threnodist_stand,distance=0..] at @s run playsound minecraft:entity.enderman.teleport hostile @a[tag=mg.flw] ~ ~ ~ 3 0.7
execute as @n[tag=thren_stand_decoy,distance=0..] at @s run particle minecraft:portal ~ ~1.5 ~ 0 0 0 0.5 100
execute as @n[tag=thren_stand_decoy,distance=0..] at @s run playsound minecraft:entity.enderman.teleport hostile @a[tag=mg.flw] ~ ~ ~ 3 0.7
execute as @e[tag=threnodist_stand,distance=0..] at @s run particle minecraft:dust_color_transition{from_color:[0.000,0.000,0.000],to_color:[0.529,0.000,0.529],scale:3} ~ ~1.5 ~ 0.4 0.4 0.4 1 100
execute as @e[tag=thren_stand_decoy,distance=0..] at @s run particle minecraft:dust_color_transition{from_color:[0.000,0.000,0.000],to_color:[0.529,0.000,0.529],scale:3} ~ ~1.5 ~ 0.4 0.4 0.4 1 100


tp @e[tag=threnodist_stand,distance=0..] -11144 23 430
tp @e[tag=thren_stand_decoy,distance=0..] -11144 23 430
