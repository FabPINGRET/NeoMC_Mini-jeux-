# halloween : habille la carte ctf3 (généré par tools/lobby/gen_theme_maps.py ; inverse : halloween_off)
scoreboard players set $tm4 mg.st 1
execute if block -40 81 41495 minecraft:lantern run setblock -40 81 41495 minecraft:soul_lantern
execute if block -40 81 41505 minecraft:lantern run setblock -40 81 41505 minecraft:soul_lantern
execute if block -18 88 41500 minecraft:lantern run setblock -18 88 41500 minecraft:soul_lantern
execute if block 18 88 41500 minecraft:lantern run setblock 18 88 41500 minecraft:soul_lantern
execute if block 40 81 41495 minecraft:lantern run setblock 40 81 41495 minecraft:soul_lantern
execute if block 40 81 41505 minecraft:lantern run setblock 40 81 41505 minecraft:soul_lantern
