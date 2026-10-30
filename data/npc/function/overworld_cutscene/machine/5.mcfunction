execute positioned 10388 170 -16 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.drowned.ambient_water neutral @a[tag=mg.flw] ~ ~ ~ 1 2

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Water","color":"blue"},{"text":"> The tides of the world have turned against you. None of your underlings still stand.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/machine/6 7s replace

#","color":"white"},{"text":"
