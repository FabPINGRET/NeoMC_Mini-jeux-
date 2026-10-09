schedule clear mg:bomber/build_step
clear @a minecraft:elytra[custom_data~{mg_bomb:1b}]
clear @a minecraft:firework_rocket[custom_data~{mg_bomb:1b}]
kill @e[tag=mg.bomb]
kill @e[tag=mg.bsm]
bossbar remove mg:bomber
scoreboard players reset * mg.bmb
scoreboard players reset * mg.bid
effect clear @a[tag=mg.play]
