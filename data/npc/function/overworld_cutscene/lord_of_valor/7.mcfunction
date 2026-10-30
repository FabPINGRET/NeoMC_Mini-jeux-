execute positioned 10022 93 -99 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10022 93 -99 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Grlu","color":"light_purple"},{"text":"> Well, yeah, I did do those things, but I did them so that everyone would see me as a hero and think I'm super brave and cool.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/8 10s replace
