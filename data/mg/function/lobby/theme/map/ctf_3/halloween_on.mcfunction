# halloween : habille la carte ctf (généré par tools/lobby/gen_theme_maps.py ; inverse : halloween_off)
scoreboard players set $tm3 mg.st 1
execute if block -40 81 21595 minecraft:lantern run setblock -40 81 21595 minecraft:soul_lantern
execute if block -40 81 21605 minecraft:lantern run setblock -40 81 21605 minecraft:soul_lantern
execute if block 40 81 21595 minecraft:lantern run setblock 40 81 21595 minecraft:soul_lantern
execute if block 40 81 21605 minecraft:lantern run setblock 40 81 21605 minecraft:soul_lantern
