# Spawn : grande île flottante (générée par tools/lobby/gen_lobby.py), construite en plusieurs ticks
kill @e[type=minecraft:text_display,tag=mg.deco]
forceload add -80 -80 80 80
forceload add 81 -32 144 32
forceload add -115 81 115 225
tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Construction du spawn (quelques secondes)...","color":"gray"}]
schedule function mg:lobby/build_1 5s
