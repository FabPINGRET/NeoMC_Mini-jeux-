fill ~-2 ~-1 ~-2 ~2 ~3 ~2 tuff replace crying_obsidian
fill ~-2 ~-1 ~-2 ~2 ~3 ~2 tuff replace glowstone

fill ~-2 ~-1 ~-2 ~2 ~3 ~2 dead_fire_coral_block replace amethyst_block
fill ~-2 ~-1 ~-2 ~2 ~3 ~2 dead_fire_coral_block replace raw_gold_block

setblock ~ ~-2 ~ air

kill @e[tag=worldgate_to,limit=1,distance=..5]
kill @e[tag=worldgate_from,limit=1,distance=..5]
kill @e[tag=worldgate_vir,limit=1,distance=..5]
