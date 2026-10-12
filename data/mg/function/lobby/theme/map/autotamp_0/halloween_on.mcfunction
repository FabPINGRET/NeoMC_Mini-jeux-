# halloween : habille la carte autotamp (généré par tools/lobby/gen_theme_maps.py ; inverse : halloween_off)
scoreboard players set $tm0 mg.st 1
execute if block -21 68 37400 minecraft:lantern run setblock -21 68 37400 minecraft:soul_lantern
execute if block -15 68 37385 minecraft:lantern run setblock -15 68 37385 minecraft:soul_lantern
execute if block -15 68 37415 minecraft:lantern run setblock -15 68 37415 minecraft:soul_lantern
execute if block 0 68 37379 minecraft:lantern run setblock 0 68 37379 minecraft:soul_lantern
execute if block 0 68 37421 minecraft:lantern run setblock 0 68 37421 minecraft:soul_lantern
execute if block 15 68 37385 minecraft:lantern run setblock 15 68 37385 minecraft:soul_lantern
execute if block 15 68 37415 minecraft:lantern run setblock 15 68 37415 minecraft:soul_lantern
execute if block 21 68 37400 minecraft:lantern run setblock 21 68 37400 minecraft:soul_lantern
