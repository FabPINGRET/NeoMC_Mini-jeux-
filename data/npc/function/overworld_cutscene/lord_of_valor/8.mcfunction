execute positioned 10015 94 -95 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.silverfish.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned 10015 94 -95 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.puffer_fish.blow_up neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute positioned 10015 94 -95 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Spores","color":"light_purple"},{"text":"> That's not what you told me after helping rescue me, ","color":"white"},{"text":"Slime Man","color":"green"},{"text":". You fought valiantly and were excited to tell me how a true hero fights not for themselves, but for others.","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute as @n[tag=lord_of_valor,distance=0..] at @s facing entity @n[tag=lord_of_spores,distance=0..] eyes run tp @s ~ ~ ~ ~ ~

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/9 14s replace
