execute as @n[tag=wahrog_pivot,distance=0..] at @s facing entity @p[tag=targeted,tag=mg.flw] eyes rotated ~ 0 run tp @s ~ ~ ~ ~ ~

execute if score wahrog_target Value matches 1..2 as @n[tag=wahrog_stand,distance=0..] at @s facing entity @p[tag=targeted,tag=mg.flw] eyes run tp @s ~ ~ ~ ~ ~
execute if score wahrog_target Value matches 2 as @n[tag=wahrog_pivot,distance=0..] at @s facing entity @p[tag=targeted,tag=mg.flw] eyes rotated ~ 0 positioned ^ ^ ^-6 run tp @n[tag=wahrog_stand,distance=0..] ~ 70 ~

#SUBSURFACE

#execute if block -11146 83 332 light[level=15,waterlogged=false] run fill -11130 66 348 -11162 66 316 light[level=15,waterlogged=false] replace minecraft:diamond_block
#execute if block -11146 83 332 light[level=15,waterlogged=false] run fill -11130 66 348 -11162 66 316 light[level=15,waterlogged=false] replace minecraft:diamond_block
#execute as @e[tag=wahrog_bat] at @s run fill ~-1 66 ~-1 ~1 66 ~1 diamond_block replace light

#fill -11130 67 348 -11162 67 316 blue_stained_glass replace minecraft:cyan_stained_glass
#execute as @e[tag=wahrog_bat] at @s run fill ~-1 67 ~-1 ~1 67 ~1 cyan_stained_glass replace blue_stained_glass

fill -11130 67 348 -11162 67 316 blue_stained_glass replace minecraft:diamond_block
execute as @e[tag=wahrog_bat,distance=0..] at @s run fill ~-1 67 ~-1 ~1 67 ~1 diamond_block replace blue_stained_glass
