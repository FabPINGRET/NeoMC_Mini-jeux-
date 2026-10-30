execute as @n[tag=sc_boss_model_body,distance=0..] at @s run playsound minecraft:entity.witch.throw hostile @a[tag=mg.flw] ~ ~ ~ 3 1

execute as @n[tag=sc_boss_head_draw,distance=0..] at @s run tp @n[tag=sc_boss_rarm_draw,distance=0..] ~ ~ ~ ~ ~
execute as @n[tag=sc_boss_body_draw,distance=0..] at @s positioned ~ ~3.7 ~ run tp @n[tag=sc_boss_rarm_draw,distance=0..] ^-1.7 ^ ^
execute as @n[tag=sc_boss_rarm_draw,distance=0..] at @s run tp @n[tag=sc_boss_model_rarm,tag=origin,distance=0..] ~ ~ ~ ~ ~

execute as @n[tag=sc_boss_model_body,tag=origin,distance=0..] at @s positioned ^ ^4 ^1.5 run function boss:secret/model/keystar
execute as @n[tag=sc_boss_model_keystar,tag=origin,tag=new,distance=0..] at @s rotated as @n[tag=sc_boss_model_rarm,tag=origin,distance=0..] run tp @s ~ ~ ~ ~ ~
tag @n[tag=sc_boss_model_keystar,tag=origin,tag=new,distance=0..] remove new
execute as @n[tag=sc_boss_model_body,tag=origin,distance=0..] at @s positioned ^ ^4 ^1.5 run function boss:secret/model/keystar
execute as @n[tag=sc_boss_model_keystar,tag=origin,tag=new,distance=0..] at @s rotated as @n[tag=sc_boss_model_rarm,tag=origin,distance=0..] run tp @s ~ ~ ~ ~11 ~
tag @n[tag=sc_boss_model_keystar,tag=origin,tag=new,distance=0..] remove new
execute as @n[tag=sc_boss_model_body,tag=origin,distance=0..] at @s positioned ^ ^4 ^1.5 run function boss:secret/model/keystar
execute as @n[tag=sc_boss_model_keystar,tag=origin,tag=new,distance=0..] at @s rotated as @n[tag=sc_boss_model_rarm,tag=origin,distance=0..] run tp @s ~ ~ ~ ~-11 ~
tag @n[tag=sc_boss_model_keystar,tag=origin,tag=new,distance=0..] remove new


execute as @n[tag=sc_boss_model_body,tag=origin,distance=0..] at @s positioned ^ ^4 ^1.5 run function boss:secret/model/keystar
execute as @n[tag=sc_boss_model_keystar,tag=origin,tag=new,distance=0..] at @s rotated as @n[tag=sc_boss_model_rarm,tag=origin,distance=0..] run tp @s ~ ~ ~ ~6 ~-7
tag @n[tag=sc_boss_model_keystar,tag=origin,tag=new,distance=0..] remove new
execute as @n[tag=sc_boss_model_body,tag=origin,distance=0..] at @s positioned ^ ^4 ^1.5 run function boss:secret/model/keystar
execute as @n[tag=sc_boss_model_keystar,tag=origin,tag=new,distance=0..] at @s rotated as @n[tag=sc_boss_model_rarm,tag=origin,distance=0..] run tp @s ~ ~ ~ ~-6 ~-7
tag @n[tag=sc_boss_model_keystar,tag=origin,tag=new,distance=0..] remove new
