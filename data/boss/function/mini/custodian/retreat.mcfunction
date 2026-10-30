execute at @n[tag=custodian_boss,distance=0..] run particle minecraft:enchanted_hit ~ 85 ~ 0.3 0.5 0.3 0 60
execute as @n[tag=custodian_boss,distance=0..] at @s run playsound minecraft:entity.allay.ambient_with_item hostile @a[tag=mg.flw] ~ ~ ~ 2 0.5
tp @n[tag=custodian_boss,distance=0..] -10441 58 439
