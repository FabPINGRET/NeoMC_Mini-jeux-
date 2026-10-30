execute positioned 10016 94 -90 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.ravager.stunned neutral @a[tag=mg.flw] ~ ~ ~ 1 1.4
execute positioned 10016 94 -90 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Flame","color":"red"},{"text":"> Welcome to our ranks,","color":"white"},{"text":" Lord of Valor","color":"yellow"},{"text":". Now that the Seven Lords are finally reunited, we have urgent work to do.","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute as @n[tag=lord_of_valor,distance=0..] at @s facing entity @n[tag=lord_of_flame,distance=0..] eyes run tp @s ~ ~ ~ ~ ~

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/20 9s replace
