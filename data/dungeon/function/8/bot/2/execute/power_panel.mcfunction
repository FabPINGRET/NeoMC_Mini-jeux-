execute as @n[tag=fs_bot,tag=2,distance=0..] at @s positioned ~ ~2 ~ run summon minecraft:lightning_bolt
execute as @n[tag=fs_bot,tag=2,distance=0..] at @s run particle minecraft:end_rod ^ ^1.5 ^1 0 0 0 0.05 50
execute as @n[tag=fs_bot,tag=2,distance=0..] at @s if block ~ ~-1 ~ netherite_block run fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 lapis_ore

#CHECK IF WIN CONDITION MET
execute if block -10773 47 400 minecraft:lapis_ore if block -10779 47 403 minecraft:lapis_ore if block -10776 47 409 minecraft:lapis_ore run setblock -10768 46 383 minecraft:redstone_torch
execute if block -10773 47 400 minecraft:lapis_ore if block -10779 47 403 minecraft:lapis_ore if block -10776 47 409 minecraft:lapis_ore run schedule function floaty:sched/dungeon/8/bot/step_clear_all 5t replace
