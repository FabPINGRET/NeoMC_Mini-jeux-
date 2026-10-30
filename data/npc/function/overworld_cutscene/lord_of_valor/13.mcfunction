execute positioned 10027 94 -101 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.drowned.ambient_water neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned 10027 94 -101 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Water","color":"blue"},{"text":"> You won't know until you take the power, ","color":"white"},{"text":"Slime Man","color":"green"},{"text":". Go to it, it's calling to you.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/14 6s replace
