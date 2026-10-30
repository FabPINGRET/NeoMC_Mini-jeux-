function boss:6/clear

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] if score boss:sh_ceiling bool matches 0 run clone -10516 63 -107 -10509 67 -103 ~-3 ~ ~-3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] if score boss:sh_ceiling bool matches 0 run clone -10516 63 -101 -10509 67 -97 ~-4 ~ ~-1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] if score boss:sh_ceiling bool matches 0 run clone -10522 63 -107 -10518 67 -100 ~-1 ~ ~-3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] if score boss:sh_ceiling bool matches 0 run clone -10528 63 -107 -10524 67 -100 ~-3 ~ ~-4

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] if score boss:sh_ceiling bool matches 1 run clone -10516 55 -106 -10509 61 -103 ~-3 73 ~-2
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] if score boss:sh_ceiling bool matches 1 run clone -10516 55 -101 -10509 61 -98 ~-4 73 ~-1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] if score boss:sh_ceiling bool matches 1 run clone -10522 55 -107 -10519 61 -99 ~-1 73 ~-3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] if score boss:sh_ceiling bool matches 1 run clone -10527 55 -107 -10524 61 -100 ~-2 73 ~-4

execute as @n[tag=boss_sh_loc,distance=0..] at @s if score boss:sh_protected bool matches 0 run fill ~-4 ~ ~-4 ~4 ~5 ~4 air replace minecraft:mud_brick_slab
