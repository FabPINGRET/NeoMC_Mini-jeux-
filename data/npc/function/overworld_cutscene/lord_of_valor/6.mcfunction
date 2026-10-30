execute positioned 10028 94 -90 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned 10028 94 -90 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.unfreeze neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10028 94 -90 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Forest","color":"green"},{"text":"> Pupu-Nini mentioned you to me, she said you tried to rescue her when she was kidnapped.","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute as @n[tag=lord_of_valor,distance=0..] at @s facing entity @n[tag=lord_of_forest,distance=0..] eyes run tp @s ~ ~ ~ ~ ~

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/7 9s replace
