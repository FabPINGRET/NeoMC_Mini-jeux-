fill -12414 122 385 -12354 122 325 diamond_block replace minecraft:sculk
clone -12414 122 325 -12354 122 385 -12414 37 325
fill -12354 37 325 -12414 37 385 minecraft:redstone_block replace minecraft:diamond_block
execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] at @s if block ~ ~-0.1 ~ minecraft:diamond_block run damage @s 38 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]
execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] at @s if block ~ ~-0.6 ~ minecraft:diamond_block run damage @s 38 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]
execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] at @s if block ~ ~-1.1 ~ minecraft:diamond_block run damage @s 38 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]

execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] at @s if block ~-0.5 ~-0.1 ~-0.5 minecraft:diamond_block run damage @s 38 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]
execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] at @s if block ~-0.5 ~-0.6 ~-0.5 minecraft:diamond_block run damage @s 38 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]
execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] at @s if block ~-0.5 ~-1.1 ~-0.5 minecraft:diamond_block run damage @s 38 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]

execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] at @s if block ~0.5 ~-0.1 ~-0.5 minecraft:diamond_block run damage @s 38 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]
execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] at @s if block ~0.5 ~-0.6 ~-0.5 minecraft:diamond_block run damage @s 38 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]
execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] at @s if block ~0.5 ~-1.1 ~-0.5 minecraft:diamond_block run damage @s 38 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]

execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] at @s if block ~-0.5 ~-0.1 ~0.5 minecraft:diamond_block run damage @s 38 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]
execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] at @s if block ~-0.5 ~-0.6 ~0.5 minecraft:diamond_block run damage @s 38 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]
execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] at @s if block ~-0.5 ~-1.1 ~0.5 minecraft:diamond_block run damage @s 38 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]

execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] at @s if block ~0.5 ~-0.1 ~0.5 minecraft:diamond_block run damage @s 38 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]
execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] at @s if block ~0.5 ~-0.6 ~0.5 minecraft:diamond_block run damage @s 38 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]
execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] at @s if block ~0.5 ~-1.1 ~0.5 minecraft:diamond_block run damage @s 38 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]

execute as @n[tag=lord_morbex_stand,distance=0..] at @s run playsound minecraft:entity.wither.hurt hostile @a[tag=mg.flw] ~ 123 ~ 5 0.1
execute as @n[tag=lord_morbex_stand,distance=0..] at @s run playsound minecraft:item.mace.smash_ground_heavy hostile @a[tag=mg.flw] ~ 123 ~ 5 2
