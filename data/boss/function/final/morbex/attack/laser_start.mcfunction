execute as @n[tag=lord_morbex_stand,distance=0..] at @s run playsound minecraft:entity.elder_guardian.hurt hostile @a[tag=mg.flw] ~ ~ ~ 4 2
execute as @n[tag=lord_morbex_stand,distance=0..] at @s run playsound minecraft:entity.drowned.shoot hostile @a[tag=mg.flw] ~ ~ ~ 4 0.1
execute as @n[tag=lord_morbex_stand,distance=0..] at @s positioned ~ ~4 ~ run function boss:final/morbex/attack/laser_ray
