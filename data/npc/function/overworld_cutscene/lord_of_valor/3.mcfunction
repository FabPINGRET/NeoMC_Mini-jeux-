execute positioned 10022 93 -99 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 10022 93 -99 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Grlu","color":"light_purple"},{"text":"> I think I ended up embarrassing myself though. I got into a bind and would've died in a cage if it weren't for my sidekick here.","color":"white"},{"text":" ⇒","color":"light_purple"}]

setblock 10031 91 -101 minecraft:redstone_block

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/4 11s replace
