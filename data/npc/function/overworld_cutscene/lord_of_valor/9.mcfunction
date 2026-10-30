execute positioned 10027 94 -101 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.drowned.ambient_water neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned 10027 94 -101 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Water","color":"blue"},{"text":"> I'm convinced! You're a real hero Grlu, would you join us? Would you accept the power of the seventh Lord? The","color":"white"},{"text":" Dark Isles","color":"dark_purple"},{"text":" need you.","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute as @n[tag=lord_of_valor,distance=0..] at @s facing entity @n[tag=lord_of_water,distance=0..] eyes run tp @s ~ ~ ~ ~ ~

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/10 10s replace
