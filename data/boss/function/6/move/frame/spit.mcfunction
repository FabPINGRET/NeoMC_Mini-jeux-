function boss:6/clear

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] if score boss:sh_ceiling bool matches 0 run clone -10526 63 -83 -10519 67 -81 ~-3 ~ ~-1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] if score boss:sh_ceiling bool matches 0 run clone -10525 63 -79 -10518 67 -77 ~-4 ~ ~-1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] if score boss:sh_ceiling bool matches 0 run clone -10524 63 -75 -10522 67 -68 ~-1 ~ ~-3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] if score boss:sh_ceiling bool matches 0 run clone -10520 63 -74 -10518 67 -67 ~-1 ~ ~-4

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] if score boss:sh_ceiling bool matches 1 run clone -10526 56 -83 -10519 61 -81 ~-3 74 ~-1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] if score boss:sh_ceiling bool matches 1 run clone -10525 56 -79 -10518 61 -77 ~-4 74 ~-1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] if score boss:sh_ceiling bool matches 1 run clone -10524 56 -75 -10522 61 -68 ~-1 74 ~-3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] if score boss:sh_ceiling bool matches 1 run clone -10520 56 -74 -10518 61 -67 ~-1 74 ~-4

execute as @n[tag=boss_sh_loc,distance=0..] at @s if score boss:sh_protected bool matches 0 run fill ~-4 ~ ~-4 ~4 ~5 ~4 air replace minecraft:mud_brick_slab
