execute as @a[tag=mg.flw] at @s unless block ~ ~ ~ minecraft:light run attribute @s minecraft:gravity base reset
execute as @a[tag=mg.flw] at @s if block ~ ~ ~ minecraft:light[level=0] run attribute @s minecraft:gravity base set -0.04

execute as @e[tag=enemy,distance=0..] at @s unless block ~ ~ ~ minecraft:light run attribute @s minecraft:gravity base reset
execute as @e[tag=enemy,distance=0..] at @s if block ~ ~ ~ minecraft:light[level=0] run attribute @s minecraft:gravity base set -0.04

execute if score fs_fanswitch Value matches 1 as @a[tag=mg.flw] at @s if block ~ ~ ~ minecraft:light[level=1] run attribute @s minecraft:gravity base set -0.04
execute if score fs_fanswitch Value matches 2 as @a[tag=mg.flw] at @s if block ~ ~ ~ minecraft:light[level=2] run attribute @s minecraft:gravity base set -0.04
execute if score fs_fanswitch Value matches 3 as @a[tag=mg.flw] at @s if block ~ ~ ~ minecraft:light[level=3] run attribute @s minecraft:gravity base set -0.04

execute if score fs_fanswitch Value matches 1 as @e[tag=fs_fan,tag=1,tag=on,tag=axle,distance=0..] at @s run playsound minecraft:entity.breeze.idle_ground ambient @a[tag=mg.flw] ~ ~ ~ 0.01 0.1
execute if score fs_fanswitch Value matches 1 as @e[tag=fs_fan,tag=1,tag=on,tag=axle,distance=0..] at @s run particle minecraft:trial_spawner_detection_ominous ~ ~3 ~ 0.5 3 0.5 0 1
execute if score fs_fanswitch Value matches 1 as @e[tag=fs_fan,tag=1,tag=on,distance=0..] at @s run rotate @s ~23 0

execute if score fs_fanswitch Value matches 2 as @e[tag=fs_fan,tag=2,tag=on,tag=axle,distance=0..] at @s run playsound minecraft:entity.breeze.idle_ground ambient @a[tag=mg.flw] ~ ~ ~ 0.01 0.1
execute if score fs_fanswitch Value matches 2 as @e[tag=fs_fan,tag=2,tag=on,tag=axle,distance=0..] at @s run particle minecraft:trial_spawner_detection_ominous ~ ~3 ~ 0.5 3 0.5 0 1
execute if score fs_fanswitch Value matches 2 as @e[tag=fs_fan,tag=2,tag=on,distance=0..] at @s run rotate @s ~23 0

execute if score fs_fanswitch Value matches 3 as @e[tag=fs_fan,tag=3,tag=on,tag=axle,distance=0..] at @s run playsound minecraft:entity.breeze.idle_ground ambient @a[tag=mg.flw] ~ ~ ~ 0.01 0.1
execute if score fs_fanswitch Value matches 3 as @e[tag=fs_fan,tag=3,tag=on,tag=axle,distance=0..] at @s run particle minecraft:trial_spawner_detection_ominous ~ ~3 ~ 0.5 3 0.5 0 1
execute if score fs_fanswitch Value matches 3 as @e[tag=fs_fan,tag=3,tag=on,distance=0..] at @s run rotate @s ~23 0

execute as @e[tag=fs_fan,tag=always,tag=on,tag=axle,tag=!quiet,distance=0..] at @s run playsound minecraft:entity.breeze.idle_ground ambient @a[tag=mg.flw] ~ ~ ~ 0.01 0.1
execute as @e[tag=fs_fan,tag=always,tag=on,tag=axle,distance=0..] at @s run particle minecraft:trial_spawner_detection_ominous ~ ~3 ~ 0.5 3 0.5 0 1
execute as @e[tag=fs_fan,tag=always,tag=on,distance=0..] at @s run rotate @s ~23 0

execute as @e[tag=fs_fan,tag=stopping,distance=0..] at @s run rotate @s ~10 0
