execute positioned 10017 94 -101 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute positioned 10017 94 -101 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:block.trial_spawner.spawn_item_begin neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10017 94 -101 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Ice","color":"aqua"},{"text":"> That's right. It's time to drive","color":"white"},{"text":" Morbex ","color":"dark_aqua"},{"text":"out of the Dark Isles for good.","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute as @n[tag=lord_of_valor,distance=0..] at @s facing entity @n[tag=lord_of_ice,distance=0..] eyes run tp @s ~ ~ ~ ~ ~

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/21 9s replace
