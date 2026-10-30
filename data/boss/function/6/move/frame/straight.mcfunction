function boss:6/clear

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] if score boss:sh_ceiling bool matches 0 run clone -10516 63 -83 -10508 67 -81 ~-3 ~ ~-1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] if score boss:sh_ceiling bool matches 0 run clone -10516 63 -79 -10508 67 -77 ~-5 ~ ~-1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] if score boss:sh_ceiling bool matches 0 run clone -10514 63 -75 -10512 67 -67 ~-1 ~ ~-3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] if score boss:sh_ceiling bool matches 0 run clone -10510 63 -75 -10508 67 -67 ~-1 ~ ~-5

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] if score boss:sh_ceiling bool matches 1 run clone -10516 55 -83 -10509 61 -81 ~-3 73 ~-1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] if score boss:sh_ceiling bool matches 1 run clone -10515 55 -79 -10508 61 -77 ~-4 73 ~-1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] if score boss:sh_ceiling bool matches 1 run clone -10514 55 -75 -10512 61 -68 ~-1 73 ~-3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] if score boss:sh_ceiling bool matches 1 run clone -10510 55 -74 -10508 61 -67 ~-1 73 ~-4

execute as @n[tag=boss_sh_loc,distance=0..] at @s if score boss:sh_protected bool matches 0 run fill ~-4 ~ ~-4 ~4 ~5 ~4 air replace minecraft:mud_brick_slab
