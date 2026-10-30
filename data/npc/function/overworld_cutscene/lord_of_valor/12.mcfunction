execute positioned 10022 93 -99 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10022 93 -99 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> I accept, but I don't know what to expect. Will I be the new Lord of Smoke? Lord of Slime? Lord of Yucky Martial Arts?","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/13 10s replace
