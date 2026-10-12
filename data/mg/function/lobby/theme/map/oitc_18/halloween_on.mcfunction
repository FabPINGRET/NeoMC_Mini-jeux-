# halloween : habille la carte oitc (généré par tools/lobby/gen_theme_maps.py ; inverse : halloween_off)
scoreboard players set $tm18 mg.st 1
execute if block -12 81 5788 minecraft:lantern run setblock -12 81 5788 minecraft:soul_lantern
execute if block -12 81 5812 minecraft:lantern run setblock -12 81 5812 minecraft:soul_lantern
execute if block 12 81 5788 minecraft:lantern run setblock 12 81 5788 minecraft:soul_lantern
execute if block 12 81 5812 minecraft:lantern run setblock 12 81 5812 minecraft:soul_lantern
