#----------- CLEAR FRAME -----------

execute as @e[tag=boss_ed_fella,distance=0..] at @s positioned ^ ^ ^4 if block ~ ~-1 ~ waxed_oxidized_copper_grate at @s run fill ~-3 116 ~-3 ~3 130 ~3 air replace minecraft:red_glazed_terracotta
execute as @e[tag=boss_ed_fella,distance=0..] at @s positioned ^ ^ ^4 if block ~ ~-1 ~ waxed_oxidized_copper_grate at @s run fill ~-3 116 ~-3 ~3 130 ~3 air replace minecraft:light
execute as @e[tag=boss_ed_fella,distance=0..] at @s positioned ^ ^ ^4 if block ~ ~-1 ~ waxed_oxidized_copper_grate at @s run fill ~-3 116 ~-3 ~3 130 ~3 air replace minecraft:target
execute as @e[tag=boss_ed_fella,distance=0..] at @s positioned ^ ^ ^4 if block ~ ~-1 ~ waxed_oxidized_copper_grate at @s run fill ~-3 116 ~-3 ~3 130 ~3 air replace minecraft:command_block

#----------- KILL IF END -----------

execute as @e[tag=boss_ed_fella,distance=0..] at @s positioned ^ ^ ^4 unless block ~ ~-1 ~ waxed_oxidized_copper_grate at @s run function boss:4/melt
execute as @e[tag=boss_ed_fella,distance=0..] at @s positioned ^ ^ ^4 unless block ~ ~-1 ~ waxed_oxidized_copper_grate at @s run kill @s

#----------- LAVA TRAIL -----------

execute as @e[tag=boss_ed_fella,distance=0..] at @s positioned ^ ^ ^4 if block ~ ~-1 ~ waxed_oxidized_copper_grate at @s run fill ~-2 ~ ~-2 ~2 ~ ~2 lava[level=6]
execute as @e[tag=boss_ed_fella,distance=0..] at @s positioned ^ ^ ^4 if block ~ ~-1 ~ waxed_oxidized_copper_grate at @s run fill ~-3 ~ ~-2 ~3 ~ ~2 lava[level=6]
execute as @e[tag=boss_ed_fella,distance=0..] at @s positioned ^ ^ ^4 if block ~ ~-1 ~ waxed_oxidized_copper_grate at @s run fill ~-2 ~ ~-3 ~2 ~ ~3 lava[level=6]

#----------- MOVE MARKER -----------

execute as @e[tag=boss_ed_fella,distance=0..] at @s positioned ^ ^ ^4 if block ~ ~-1 ~ waxed_oxidized_copper_grate at @s run playsound minecraft:entity.magma_cube.squish hostile @a[tag=mg.flw] ~ ~ ~ 2 0.1
execute as @e[tag=boss_ed_fella,distance=0..] at @s positioned ^ ^ ^4 if block ~ ~-1 ~ waxed_oxidized_copper_grate at @s run tp @e[type=arrow,distance=..4] ^ ^ ^4
execute as @e[tag=boss_ed_fella,distance=0..] at @s positioned ^ ^ ^4 if block ~ ~-1 ~ waxed_oxidized_copper_grate at @s run tp @s ^ ^ ^4


#----------- DRAW FRAME -----------

execute as @e[tag=boss_ed_fella,tag=fella_north,distance=0..] at @s run clone -10075 113 -302 -10069 120 -296 ~-3 ~ ~-3
execute as @e[tag=boss_ed_fella,tag=fella_south,distance=0..] at @s run clone -10075 113 -318 -10069 120 -312 ~-3 ~ ~-3
execute as @e[tag=boss_ed_fella,tag=fella_east,distance=0..] at @s run clone -10075 113 -326 -10069 120 -320 ~-3 ~ ~-3
execute as @e[tag=boss_ed_fella,tag=fella_west,distance=0..] at @s run clone -10075 113 -310 -10069 120 -304 ~-3 ~ ~-3

#----------- SECOND TRAIL -----------

execute as @e[tag=boss_ed_fella,tag=fella_north,distance=0..] at @s run fill ~3 ~ ~2 ~3 ~ ~5 lava[level=6] replace air
execute as @e[tag=boss_ed_fella,tag=fella_north,distance=0..] at @s run fill ~-3 ~ ~2 ~-3 ~ ~5 lava[level=6] replace air
execute as @e[tag=boss_ed_fella,tag=fella_north,distance=0..] at @s run fill ~2 ~ ~3 ~2 ~ ~4 lava[level=6] replace air
execute as @e[tag=boss_ed_fella,tag=fella_north,distance=0..] at @s run fill ~-2 ~ ~3 ~-2 ~ ~4 lava[level=6] replace air

execute as @e[tag=boss_ed_fella,tag=fella_south,distance=0..] at @s run fill ~3 ~ ~-2 ~3 ~ ~-5 lava[level=6] replace air
execute as @e[tag=boss_ed_fella,tag=fella_south,distance=0..] at @s run fill ~-3 ~ ~-2 ~-3 ~ ~-5 lava[level=6] replace air
execute as @e[tag=boss_ed_fella,tag=fella_south,distance=0..] at @s run fill ~2 ~ ~-3 ~2 ~ ~-4 lava[level=6] replace air
execute as @e[tag=boss_ed_fella,tag=fella_south,distance=0..] at @s run fill ~-2 ~ ~-3 ~-2 ~ ~-4 lava[level=6] replace air

execute as @e[tag=boss_ed_fella,tag=fella_east,distance=0..] at @s run fill ~-2 ~ ~3 ~-5 ~ ~3 lava[level=6] replace air
execute as @e[tag=boss_ed_fella,tag=fella_east,distance=0..] at @s run fill ~-2 ~ ~-3 ~-5 ~ ~-3 lava[level=6] replace air
execute as @e[tag=boss_ed_fella,tag=fella_east,distance=0..] at @s run fill ~-3 ~ ~2 ~-4 ~ ~2 lava[level=6] replace air
execute as @e[tag=boss_ed_fella,tag=fella_east,distance=0..] at @s run fill ~-3 ~ ~-2 ~-4 ~ ~-2 lava[level=6] replace air

execute as @e[tag=boss_ed_fella,tag=fella_west,distance=0..] at @s run fill ~2 ~ ~3 ~5 ~ ~3 lava[level=6] replace air
execute as @e[tag=boss_ed_fella,tag=fella_west,distance=0..] at @s run fill ~2 ~ ~-3 ~5 ~ ~-3 lava[level=6] replace air
execute as @e[tag=boss_ed_fella,tag=fella_west,distance=0..] at @s run fill ~3 ~ ~2 ~4 ~ ~2 lava[level=6] replace air
execute as @e[tag=boss_ed_fella,tag=fella_west,distance=0..] at @s run fill ~3 ~ ~-2 ~4 ~ ~-2 lava[level=6] replace air

#----------- ADVANCE FRAME -----------

execute if entity @e[tag=boss_ed_fella,distance=0..] run setblock -10071 95 -378 minecraft:redstone_block

#----------- DAMAGE PLAYERS -----------

execute as @e[tag=boss_ed_fella,distance=0..] at @s as @a[distance=..3.5,tag=mg.flw] run damage @s 16 minecraft:mob_attack by @e[tag=boss_ed_name,limit=1,distance=0..]
