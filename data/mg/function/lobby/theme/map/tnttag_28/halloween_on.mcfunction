# halloween : habille la carte tnttag (généré par tools/lobby/gen_theme_maps.py ; inverse : halloween_off)
scoreboard players set $tm28 mg.st 1
execute if block -15 81 6085 minecraft:lantern run setblock -15 81 6085 minecraft:soul_lantern
execute if block -15 81 6115 minecraft:lantern run setblock -15 81 6115 minecraft:soul_lantern
execute if block 15 81 6085 minecraft:lantern run setblock 15 81 6085 minecraft:soul_lantern
execute if block 15 81 6115 minecraft:lantern run setblock 15 81 6115 minecraft:soul_lantern
