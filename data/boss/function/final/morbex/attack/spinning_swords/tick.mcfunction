execute as @e[tag=morbex_spinning_sword,distance=0..] at @s run tp @s ~ ~ ~ ~35 ~
execute as @e[tag=morbex_spinning_sword_pivot,distance=0..] at @s run tp @s ~ ~ ~ ~3 ~

execute as @n[tag=morbex_spinning_sword_pivot,distance=0..] at @s rotated ~ ~ positioned ^ ^ ^28 positioned ~ 123 ~ run tp @n[tag=morbex_spinning_sword,tag=1,distance=0..] ~ ~ ~
execute as @n[tag=morbex_spinning_sword_pivot,distance=0..] at @s rotated ~45 ~ positioned ^ ^ ^28 positioned ~ 123 ~ run tp @n[tag=morbex_spinning_sword,tag=2,distance=0..] ~ ~ ~
execute as @n[tag=morbex_spinning_sword_pivot,distance=0..] at @s rotated ~90 ~ positioned ^ ^ ^28 positioned ~ 123 ~ run tp @n[tag=morbex_spinning_sword,tag=3,distance=0..] ~ ~ ~
execute as @n[tag=morbex_spinning_sword_pivot,distance=0..] at @s rotated ~135 ~ positioned ^ ^ ^28 positioned ~ 123 ~ run tp @n[tag=morbex_spinning_sword,tag=4,distance=0..] ~ ~ ~
execute as @n[tag=morbex_spinning_sword_pivot,distance=0..] at @s rotated ~180 ~ positioned ^ ^ ^28 positioned ~ 123 ~ run tp @n[tag=morbex_spinning_sword,tag=5,distance=0..] ~ ~ ~
execute as @n[tag=morbex_spinning_sword_pivot,distance=0..] at @s rotated ~225 ~ positioned ^ ^ ^28 positioned ~ 123 ~ run tp @n[tag=morbex_spinning_sword,tag=6,distance=0..] ~ ~ ~
execute as @n[tag=morbex_spinning_sword_pivot,distance=0..] at @s rotated ~270 ~ positioned ^ ^ ^28 positioned ~ 123 ~ run tp @n[tag=morbex_spinning_sword,tag=7,distance=0..] ~ ~ ~
execute as @n[tag=morbex_spinning_sword_pivot,distance=0..] at @s rotated ~315 ~ positioned ^ ^ ^28 positioned ~ 123 ~ run tp @n[tag=morbex_spinning_sword,tag=8,distance=0..] ~ ~ ~

execute store result entity @n[tag=morbex_spinning_sword_pivot,distance=0..] Rotation[1] float 0.01 run scoreboard players get morbex_spinning_sword_angle Value

execute if score morbex_spinning_sword_dir Value matches 1 run scoreboard players remove morbex_spinning_sword_angle Value 50
execute if score morbex_spinning_sword_dir Value matches 2 run scoreboard players add morbex_spinning_sword_angle Value 75
execute if score morbex_spinning_sword_dir Value matches 3 run scoreboard players add morbex_spinning_sword_angle Value 25

execute if score morbex_spinning_sword_angle Value matches 7400.. if score morbex_spinning_sword_dir Value matches 2 run function boss:final/morbex/attack/spinning_swords/transform_upright

execute if score morbex_spinning_sword_angle Value matches ..75 if score morbex_spinning_sword_dir Value matches 1 run scoreboard players set morbex_spinning_sword_dir Value 2
execute if score morbex_spinning_sword_angle Value matches 7400.. if score morbex_spinning_sword_dir Value matches 2 run scoreboard players set morbex_spinning_sword_dir Value 3
execute if score morbex_spinning_sword_angle Value matches 9000.. run function boss:final/morbex/attack/spinning_swords/end

execute as @e[tag=morbex_spinning_sword,distance=0..] at @s as @a[distance=..2,tag=mg.flw] at @s if block ~ ~-0.1 ~ minecraft:sculk run damage @s 16 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]
execute as @e[tag=morbex_spinning_sword,distance=0..] at @s as @a[distance=..2,tag=mg.flw] at @s if block ~0.5 ~-0.1 ~0.5 minecraft:sculk run damage @s 16 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]
execute as @e[tag=morbex_spinning_sword,distance=0..] at @s as @a[distance=..2,tag=mg.flw] at @s if block ~-0.5 ~-0.1 ~0.5 minecraft:sculk run damage @s 16 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]
execute as @e[tag=morbex_spinning_sword,distance=0..] at @s as @a[distance=..2,tag=mg.flw] at @s if block ~0.5 ~-0.1 ~-0.5 minecraft:sculk run damage @s 16 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]
execute as @e[tag=morbex_spinning_sword,distance=0..] at @s as @a[distance=..2,tag=mg.flw] at @s if block ~-0.5 ~-0.1 ~-0.5 minecraft:sculk run damage @s 16 minecraft:dragon_breath by @n[tag=l_morbex_2,distance=0..]


execute as @a[tag=mg.flw] at @s at @n[tag=morbex_spinning_sword,distance=0..] run playsound minecraft:block.grindstone.use hostile @s ~ ~ ~ 0.1 2
#scoreboard players set morbex_spinning_sword_angle Value 7800

