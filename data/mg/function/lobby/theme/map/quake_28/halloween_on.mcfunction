# halloween : habille la carte quake (généré par tools/lobby/gen_theme_maps.py ; inverse : halloween_off)
scoreboard players set $tm28 mg.st 1
execute if block -7 89 16403 minecraft:lantern run setblock -7 89 16403 minecraft:soul_lantern[hanging=true]
execute if block -3 94 16393 minecraft:lantern run setblock -3 94 16393 minecraft:soul_lantern[hanging=true]
execute if block 3 84 16407 minecraft:lantern run setblock 3 84 16407 minecraft:soul_lantern[hanging=true]
execute if block 7 89 16397 minecraft:lantern run setblock 7 89 16397 minecraft:soul_lantern[hanging=true]
