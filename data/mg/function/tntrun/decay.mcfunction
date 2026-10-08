# TNT Run — cycle de disparition en 2 temps : laine rouge → laine orange → vide
# (un bloc piétiné disparaît entre 9 et 18 ticks plus tard, jamais instantanément)
execute if score $ar mg.st matches 1.. run return run function mg:var/floor/decay
scoreboard players set $dk mg.st 9
fill -14 84 586 14 84 614 minecraft:air replace minecraft:orange_wool
fill -12 74 588 12 74 612 minecraft:air replace minecraft:orange_wool
fill -10 64 590 10 64 610 minecraft:air replace minecraft:orange_wool
fill -14 84 586 14 84 614 minecraft:orange_wool replace minecraft:red_wool
fill -12 74 588 12 74 612 minecraft:orange_wool replace minecraft:red_wool
fill -10 64 590 10 64 610 minecraft:orange_wool replace minecraft:red_wool
