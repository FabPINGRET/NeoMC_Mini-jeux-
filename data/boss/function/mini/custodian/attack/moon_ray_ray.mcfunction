particle enchanted_hit ~ ~ ~ 0 0 0 0 1

execute positioned ~ ~ ~ as @a[gamemode=!spectator,distance=..0.75,tag=mg.flw] run damage @s 12 minecraft:dragon_breath by @n[tag=custodian_boss,distance=0..]

execute positioned ^ ^ ^0.1 if block ^ ^ ^ air run function boss:mini/custodian/attack/moon_ray_ray
execute positioned ^ ^ ^0.1 if block ^ ^ ^ light run function boss:mini/custodian/attack/moon_ray_ray
