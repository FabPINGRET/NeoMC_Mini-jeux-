summon arrow ~ ~ ~ {pickup:2b,crit:1b,damage:50d,Tags:["naptime_stage_arrow"]}

#execute as @e[tag=naptime_stage_arrow] run data modify entity @s Owner set from entity @n[tag=boss_fs_name] UUID

#execute as @n[tag=naptime_stage_arrow] store result entity @s Motion[0] double 0.001 run random value -1000..-700
#execute as @n[tag=naptime_stage_arrow] store result entity @s Motion[1] double 0.001 run random value 2000..2500
#execute as @n[tag=naptime_stage_arrow] store result entity @s Motion[2] double 0.001 run random value -300..300

execute as @n[tag=naptime_stage_arrow,distance=0..] store result entity @s Motion[0] double 0.001 run random value -700..-500
execute as @n[tag=naptime_stage_arrow,distance=0..] store result entity @s Motion[1] double 0.001 run random value 1000..1500
execute as @n[tag=naptime_stage_arrow,distance=0..] store result entity @s Motion[2] double 0.001 run random value -300..300

playsound minecraft:entity.arrow.shoot hostile @a[tag=mg.flw] ~ ~ ~ 0.5 2
