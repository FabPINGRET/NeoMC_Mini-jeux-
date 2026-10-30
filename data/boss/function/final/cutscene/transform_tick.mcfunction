execute as @n[tag=lord_morbex_stand,distance=0..] at @s run particle minecraft:block{block_state:"end_gateway"} ~ ~3 ~ 0.5 2 0.5 0 3
execute as @n[tag=lord_morbex_stand,distance=0..] at @s run particle minecraft:block{block_state:"diamond_block"} ~ ~3 ~ 0.5 2 0.5 0 3
execute store result entity @n[tag=lord_morbex_stand,distance=0..] Rotation[0] float 1 run random value -100..-80
execute store result entity @n[tag=lord_morbex_stand,distance=0..] Pose.Head[1] float 1 run random value -10..10
