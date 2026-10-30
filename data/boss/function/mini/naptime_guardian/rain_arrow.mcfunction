summon arrow ~ ~ ~ {pickup:2b,crit:1b,damage:15d,Tags:["naptime_stage_arrow"]}

execute as @e[tag=naptime_stage_arrow,distance=0..] run data modify entity @s Owner set from entity @n[tag=boss_naptime_name,distance=0..] UUID


execute as @n[tag=naptime_stage_arrow,distance=0..] store result entity @s Motion[0] double 0.001 run random value -1200..1200
execute as @n[tag=naptime_stage_arrow,distance=0..] store result entity @s Motion[1] double 0.001 run random value -2001..-2000
execute as @n[tag=naptime_stage_arrow,distance=0..] store result entity @s Motion[2] double 0.001 run random value -1200..1200

playsound minecraft:entity.arrow.shoot hostile @a[tag=mg.flw] ~ ~ ~ 0.5 2
