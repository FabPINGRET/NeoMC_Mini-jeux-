#execute positioned 10180 40 -237 at @e[sort=nearest,limit=1,tag=npc] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a ~ ~ ~ 1 1.2

fill 10181 41 -238 10180 41 -238 air
scoreboard players set lord_of_valor Story 2

execute positioned 10180 40 -237 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> Me? As a Lord? I don't think the Lords would really want me, but thanks for thinking of me, sidekick. I guess if you insist, it couldn't hurt to go talk with them at ","color":"white"},{"text":"Valor Tower","color":"red"},{"text":".","color":"white"}]

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/slimecave_1 14s replace
