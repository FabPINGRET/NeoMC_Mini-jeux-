execute as @n[tag=threnodist_stand,distance=0..] at @s run playsound minecraft:entity.shulker.shoot hostile @a[tag=mg.flw] ~ ~ ~ 3 1
execute as @n[tag=threnodist_stand,distance=0..] at @s positioned ~ ~2.7 ~ facing -11144 58 430 run function boss:mini/threnodist/attack/gravity_center/ray
