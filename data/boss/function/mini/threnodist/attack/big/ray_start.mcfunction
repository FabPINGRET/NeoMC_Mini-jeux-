execute as @n[tag=threnodist_stand,distance=0..] at @s positioned ~ ~15 ~ rotated ~ 50 positioned ^ ^ ^3 run function boss:mini/threnodist/attack/big/ray
execute if score thren_big_dir bool matches 0 as @n[tag=threnodist_stand,distance=0..] at @s run tp @s ~ ~ ~ ~2 ~
execute if score thren_big_dir bool matches 1 as @n[tag=threnodist_stand,distance=0..] at @s run tp @s ~ ~ ~ ~-2 ~

execute as @n[tag=threnodist_stand,distance=0..] at @s run playsound minecraft:block.enchantment_table.use hostile @a[tag=mg.flw] ~ ~ ~ 3 0.6
