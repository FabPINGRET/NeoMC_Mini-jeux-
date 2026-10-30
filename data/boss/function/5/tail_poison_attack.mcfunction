execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run fill ~-1 ~ ~-1 ~1 ~9 ~1 air
execute as @e[tag=boss_skt_hole_last,limit=1,distance=0..] at @s run clone -10193 72 457 -10191 76 459 ~-1 ~ ~-1
execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run summon area_effect_cloud ~ ~ ~ {Radius:3f,RadiusPerTick:0.3f,Duration:100,potion_contents:{potion:"minecraft:strong_poison"}}
execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run summon area_effect_cloud ~ 94 ~ {Radius:3f,RadiusPerTick:0.3f,Duration:100,potion_contents:{potion:"minecraft:strong_poison"}}

execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run playsound minecraft:block.trial_spawner.spawn_item hostile @a[tag=mg.flw] ~ ~ ~ 4 0.1
execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run playsound minecraft:entity.spider.ambient hostile @a[tag=mg.flw] ~ ~ ~ 4 0.1
execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run particle minecraft:sneeze ~ ~3 ~ 1 2 1 0.1 200

function boss:5/neutral_anim
execute if block -10196 55 411 stone run schedule function floaty:sched/boss/5/pick_attack 7s
