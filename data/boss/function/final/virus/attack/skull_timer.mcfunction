scoreboard players remove wv_skull_timer Value 1
execute if score wv_skull_timer Value matches 0 run playsound minecraft:entity.ghast.shoot hostile @a[tag=mg.flw] -12384 123 355 3 1
execute if score wv_skull_timer Value matches 0 as @n[tag=wv_skull_loc,distance=0..] at @s run function boss:final/virus/attack/skull_shoot
execute if score wv_skull_timer Value matches 0 as @n[tag=wv_skull_loc,distance=0..] at @s run function boss:final/virus/attack/skull_shoot
execute if score wv_skull_timer Value matches 0 as @n[tag=wv_skull_loc,distance=0..] at @s run function boss:final/virus/attack/skull_shoot

execute if score wv_skull_timer Value matches 0 run scoreboard players set wv_skull_timer Value 2
