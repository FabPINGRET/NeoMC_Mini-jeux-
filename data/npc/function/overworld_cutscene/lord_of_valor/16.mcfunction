execute positioned 10022 94 -102 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10022 94 -102 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Slime Man","color":"green"},{"text":"> The ","color":"white"},{"text":"Lord of Valor","color":"yellow","bold":true},{"text":".","color":"white","bold":false},{"text":" ⇒","color":"light_purple"}]

setblock 10033 91 -98 minecraft:air

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/17 2s replace
