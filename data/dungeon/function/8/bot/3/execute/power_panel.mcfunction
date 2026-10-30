execute as @n[tag=fs_bot,tag=3,distance=0..] at @s positioned ~ ~2 ~ run summon minecraft:lightning_bolt
execute as @n[tag=fs_bot,tag=3,distance=0..] at @s run particle minecraft:end_rod ^ ^1.5 ^1 0 0 0 0.05 50
execute as @n[tag=fs_bot,tag=3,distance=0..] at @s if block ~ ~-1 ~ netherite_block run fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 lapis_ore

#CHECK IF WIN CONDITION MET
execute if block -10685 -18 333 minecraft:lapis_ore if block -10682 -18 336 minecraft:lapis_ore if block -10679 -18 330 minecraft:lapis_ore if block -10679 -18 333 minecraft:lapis_ore if block -10676 -18 336 minecraft:lapis_ore run setblock -10699 -19 344 minecraft:redstone_torch
execute if block -10685 -18 333 minecraft:lapis_ore if block -10682 -18 336 minecraft:lapis_ore if block -10679 -18 330 minecraft:lapis_ore if block -10679 -18 333 minecraft:lapis_ore if block -10676 -18 336 minecraft:lapis_ore run schedule function floaty:sched/dungeon/8/bot/step_clear_all 5t replace
