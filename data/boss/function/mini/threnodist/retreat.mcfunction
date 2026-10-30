kill @e[tag=threnodist_decoy,distance=0..]

tp @n[tag=threnodist_stand,distance=0..] @n[tag=threnodist_boss,distance=0..] 

execute as @n[tag=threnodist_boss,distance=0..] at @s run particle minecraft:portal ~ ~1.5 ~ 0 0 0 0.5 100
execute as @n[tag=threnodist_boss,distance=0..] at @s run playsound minecraft:entity.enderman.teleport hostile @a[tag=mg.flw] ~ ~ ~ 3 0.7

tp @n[tag=threnodist_boss,distance=0..] -11144 23 430
