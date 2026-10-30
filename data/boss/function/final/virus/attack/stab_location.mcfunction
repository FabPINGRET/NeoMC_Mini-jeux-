execute as @n[tag=targeted,distance=0..] at @s facing entity @n[tag=wv_center,distance=0..] eyes positioned ^ ^ ^4.5 run summon marker ~ ~ ~ {NoGravity:1b,Silent:1b,Tags:["wv_stab_loc"]}
execute as @e[tag=wv_stab_loc,distance=0..] at @s rotated as @n[tag=wv_center,distance=0..] run tp @s ~ ~ ~ ~ ~
