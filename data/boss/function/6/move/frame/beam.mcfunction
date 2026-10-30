function boss:6/clear

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] run clone -10516 63 -57 -10509 67 -53 ~-3 ~ ~-2
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] run clone -10515 63 -51 -10508 67 -47 ~-4 ~ ~-2
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] run clone -10518 63 -45 -10514 67 -38 ~-2 ~ ~-3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] run clone -10512 63 -44 -10508 67 -37 ~-2 ~ ~-4

execute as @n[tag=boss_sh_loc,distance=0..] at @s if score boss:sh_protected bool matches 0 run fill ~-4 ~ ~-4 ~4 ~5 ~4 air replace minecraft:mud_brick_slab
