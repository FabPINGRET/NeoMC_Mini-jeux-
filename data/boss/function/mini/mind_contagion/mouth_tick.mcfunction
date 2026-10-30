execute if score boss_mind_mouth_angle Value matches 0 run data modify entity @n[tag=mind_boss_mouth,distance=0..] Pose set value {Head:[70.0f,0.0f,0.0f]}
execute if score boss_mind_mouth_angle Value matches 0 as @n[tag=mind_boss_mouth,distance=0..] at @s positioned ~ ~4.5 ~ positioned ^ ^ ^1.3 facing ^ ^-1 ^1 run function boss:mini/mind_contagion/mouth_laser

execute if score boss_mind_mouth_angle Value matches 1 run data modify entity @n[tag=mind_boss_mouth,distance=0..] Pose set value {Head:[60.0f,0.0f,0.0f]}
execute if score boss_mind_mouth_angle Value matches 1 as @n[tag=mind_boss_mouth,distance=0..] at @s positioned ~ ~4.6 ~ positioned ^ ^ ^1.4 facing ^ ^-0.65 ^1 run function boss:mini/mind_contagion/mouth_laser

execute if score boss_mind_mouth_angle Value matches 2 run data modify entity @n[tag=mind_boss_mouth,distance=0..] Pose set value {Head:[50.0f,0.0f,0.0f]}
execute if score boss_mind_mouth_angle Value matches 2 as @n[tag=mind_boss_mouth,distance=0..] at @s positioned ~ ~4.7 ~ positioned ^ ^ ^1.5 facing ^ ^-0.4 ^1 run function boss:mini/mind_contagion/mouth_laser

execute if score boss_mind_mouth_angle Value matches 3 run data modify entity @n[tag=mind_boss_mouth,distance=0..] Pose set value {Head:[40.0f,0.0f,0.0f]}
execute if score boss_mind_mouth_angle Value matches 3 as @n[tag=mind_boss_mouth,distance=0..] at @s positioned ~ ~4.95 ~ positioned ^ ^ ^1.5 facing ^ ^-0.2 ^1 run function boss:mini/mind_contagion/mouth_laser

execute if score boss_mind_mouth_angle Value matches 4 run data modify entity @n[tag=mind_boss_mouth,distance=0..] Pose set value {Head:[30.0f,0.0f,0.0f]}
execute if score boss_mind_mouth_angle Value matches 4 as @n[tag=mind_boss_mouth,distance=0..] at @s positioned ~ ~5.2 ~ positioned ^ ^ ^1.5 facing ^ ^ ^1 run function boss:mini/mind_contagion/mouth_laser

execute if score boss_mind_mouth_angle Value matches 5 run data modify entity @n[tag=mind_boss_mouth,distance=0..] Pose set value {Head:[20.0f,0.0f,0.0f]}
execute if score boss_mind_mouth_angle Value matches 5 as @n[tag=mind_boss_mouth,distance=0..] at @s positioned ~ ~5.3 ~ positioned ^ ^ ^1.5 facing ^ ^0.2 ^1 run function boss:mini/mind_contagion/mouth_laser
