execute as @s at @s run fill ~-1 ~-1 ~-1 ~ ~10 ~ air replace barrier
execute at @s positioned ~-2 ~-2 ~-2 run kill @e[tag=vesperal_spike,dx=4,dy=12,dz=4]
execute as @s at @s unless entity @e[tag=mooneye,distance=0..] run tp @n[tag=v_paladin,distance=0..] ~ ~ ~
execute as @s at @s unless entity @e[tag=mooneye,distance=0..] at @n[tag=v_paladin,distance=0..] run particle block{block_state:"polished_tuff"} ~ ~1 ~ 0.5 1 0.5 0 200 normal
execute as @s at @s unless entity @e[tag=mooneye,distance=0..] at @n[tag=v_paladin,distance=0..] run playsound minecraft:entity.villager.ambient hostile @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute as @s at @s unless entity @e[tag=mooneye,distance=0..] at @n[tag=v_paladin,distance=0..] run playsound minecraft:block.amethyst_cluster.break hostile @a[tag=mg.flw] ~ ~ ~ 1 1
execute if score v_paladin_health Value matches 38..150 as @s at @s unless entity @e[tag=mooneye,distance=0..] run schedule function floaty:sched/boss/mini/vesperal_paladin/arrange_spikes 3s replace
kill @s
