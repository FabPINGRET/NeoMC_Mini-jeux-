function boss:6/clear

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] if score boss:sh_ceiling bool matches 0 run clone -10516 63 -89 -10509 67 -85 ~-3 ~ ~-1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] if score boss:sh_ceiling bool matches 0 run clone -10516 63 -95 -10509 67 -91 ~-4 ~ ~-3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] if score boss:sh_ceiling bool matches 0 run clone -10528 63 -92 -10524 67 -85 ~-3 ~ ~-3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] if score boss:sh_ceiling bool matches 0 run clone -10522 63 -92 -10518 67 -85 ~-1 ~ ~-4

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] if score boss:sh_ceiling bool matches 1 run clone -10516 55 -89 -10509 61 -86 ~-3 73 ~-1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] if score boss:sh_ceiling bool matches 1 run clone -10516 55 -94 -10509 61 -91 ~-4 73 ~-2
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] if score boss:sh_ceiling bool matches 1 run clone -10527 55 -92 -10524 61 -85 ~-2 73 ~-3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] if score boss:sh_ceiling bool matches 1 run clone -10522 55 -92 -10519 61 -85 ~-1 73 ~-4

execute as @n[tag=boss_sh_loc,distance=0..] at @s if score boss:sh_protected bool matches 0 run fill ~-4 ~ ~-4 ~4 ~5 ~4 air replace minecraft:mud_brick_slab
