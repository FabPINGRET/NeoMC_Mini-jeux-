execute positioned 10022 94 -102 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10022 94 -102 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Valor","color":"yellow"},{"text":"> We'll meet you there, hero. Don't worry, you can still be my sidekick!","color":"white"}]

setblock 10031 91 -101 redstone_block

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/23 7s replace
