# halloween : habille la carte oitc (généré par tools/lobby/gen_theme_maps.py ; inverse : halloween_off)
scoreboard players set $tm19 mg.st 1
execute if block -19 81 11681 minecraft:lantern run setblock -19 81 11681 minecraft:soul_lantern[hanging=false]
execute if block -19 81 11719 minecraft:lantern run setblock -19 81 11719 minecraft:soul_lantern[hanging=false]
execute if block -8 81 11700 minecraft:lantern run setblock -8 81 11700 minecraft:soul_lantern[hanging=false]
execute if block 0 81 11692 minecraft:lantern run setblock 0 81 11692 minecraft:soul_lantern[hanging=false]
execute if block 0 81 11708 minecraft:lantern run setblock 0 81 11708 minecraft:soul_lantern[hanging=false]
execute if block 8 81 11700 minecraft:lantern run setblock 8 81 11700 minecraft:soul_lantern[hanging=false]
execute if block 19 81 11681 minecraft:lantern run setblock 19 81 11681 minecraft:soul_lantern[hanging=false]
execute if block 19 81 11719 minecraft:lantern run setblock 19 81 11719 minecraft:soul_lantern[hanging=false]
