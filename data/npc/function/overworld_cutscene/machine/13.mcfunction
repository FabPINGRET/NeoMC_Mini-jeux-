execute positioned 10396 170 -16 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned 10396 170 -16 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.unfreeze neutral @a[tag=mg.flw] ~ ~ ~ 1 1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Forest","color":"green"},{"text":"> I’ve heard enough.","color":"white"},{"text":" Morbex","color":"dark_aqua"},{"text":", you are hereby banished from the ","color":"white"},{"text":"Dark Isles","color":"dark_purple"},{"text":" forever.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/machine/14 8s replace

fill 10381 46 -7 10389 46 -15 minecraft:redstone_block

#","color":"white"},{"text":"
