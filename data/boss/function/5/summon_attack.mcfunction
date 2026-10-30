execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run fill ~-1 ~ ~-1 ~1 ~9 ~1 air
execute as @e[tag=boss_skt_hole_last,limit=1,distance=0..] at @s run clone -10193 72 457 -10191 76 459 ~-1 ~ ~-1
execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s as @a[gamemode=!spectator,tag=mg.flw] positioned ~ 98 ~ run function summon:cuauhtli

execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run playsound minecraft:block.trial_spawner.spawn_mob hostile @a[tag=mg.flw] ~ ~ ~ 4 1
execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run playsound minecraft:entity.spider.ambient hostile @a[tag=mg.flw] ~ ~ ~ 4 0.1
execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run particle minecraft:totem_of_undying ~ ~3 ~ 1 2 1 0.1 200

function boss:5/neutral_anim
execute if block -10196 55 411 stone run schedule function floaty:sched/boss/5/pick_attack 4s
