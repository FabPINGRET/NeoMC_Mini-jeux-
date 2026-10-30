function boss:6/clear

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] if score boss:sh_ceiling bool matches 0 run clone -10516 63 -65 -10508 68 -63 ~-2 ~ ~-1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] if score boss:sh_ceiling bool matches 0 run clone -10516 63 -61 -10508 68 -59 ~-6 ~ ~-1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] if score boss:sh_ceiling bool matches 0 run clone -10520 63 -65 -10518 68 -57 ~-1 ~ ~-2
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] if score boss:sh_ceiling bool matches 0 run clone -10524 63 -65 -10522 68 -57 ~-1 ~ ~-6

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] if score boss:sh_ceiling bool matches 1 run clone -10516 55 -65 -10509 61 -63 ~-2 73 ~-1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] if score boss:sh_ceiling bool matches 1 run clone -10515 55 -61 -10508 61 -59 ~-5 73 ~-1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] if score boss:sh_ceiling bool matches 1 run clone -10520 55 -65 -10518 61 -58 ~-1 73 ~-2
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] if score boss:sh_ceiling bool matches 1 run clone -10524 55 -64 -10522 61 -57 ~-1 73 ~-5

execute as @n[tag=boss_sh_loc,distance=0..] at @s if score boss:sh_protected bool matches 0 run fill ~-4 ~ ~-4 ~4 ~5 ~4 air replace minecraft:mud_brick_slab
