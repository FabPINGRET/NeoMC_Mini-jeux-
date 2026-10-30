execute positioned 10022 94 -102 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10022 94 -102 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> I accept this duty and this power. I will be a Lord of Self-Sacrifice. A Lord of Heroes.","color":"white"},{"text":" ⇒","color":"light_purple"}]

setblock 10033 91 -98 minecraft:redstone_block

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/16 9s replace
