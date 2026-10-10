# 🙈 Labyrinthe aveugle : 8 couloirs, labyrinthe $lbm (0..2)
fill -3 62 38197 28 84 38240 minecraft:air
fill 29 62 38197 60 84 38240 minecraft:air
fill 61 62 38197 92 84 38240 minecraft:air
fill 93 62 38197 124 84 38240 minecraft:air
fill 125 62 38197 156 84 38240 minecraft:air
fill 157 62 38197 188 84 38240 minecraft:air
fill 189 62 38197 220 84 38240 minecraft:air
fill 221 62 38197 252 84 38240 minecraft:air
fill 253 62 38197 284 84 38240 minecraft:air
fill 285 62 38197 316 84 38240 minecraft:air
fill 317 62 38197 334 84 38240 minecraft:air
execute positioned 0 64 38200 run function mg:lab/lane
execute if score $lbm mg.st matches 0 positioned 0 64 38200 run function mg:lab/maze_0
execute if score $lbm mg.st matches 1 positioned 0 64 38200 run function mg:lab/maze_1
execute if score $lbm mg.st matches 2 positioned 0 64 38200 run function mg:lab/maze_2
execute positioned 42 64 38200 run function mg:lab/lane
execute if score $lbm mg.st matches 0 positioned 42 64 38200 run function mg:lab/maze_0
execute if score $lbm mg.st matches 1 positioned 42 64 38200 run function mg:lab/maze_1
execute if score $lbm mg.st matches 2 positioned 42 64 38200 run function mg:lab/maze_2
execute positioned 84 64 38200 run function mg:lab/lane
execute if score $lbm mg.st matches 0 positioned 84 64 38200 run function mg:lab/maze_0
execute if score $lbm mg.st matches 1 positioned 84 64 38200 run function mg:lab/maze_1
execute if score $lbm mg.st matches 2 positioned 84 64 38200 run function mg:lab/maze_2
execute positioned 126 64 38200 run function mg:lab/lane
execute if score $lbm mg.st matches 0 positioned 126 64 38200 run function mg:lab/maze_0
execute if score $lbm mg.st matches 1 positioned 126 64 38200 run function mg:lab/maze_1
execute if score $lbm mg.st matches 2 positioned 126 64 38200 run function mg:lab/maze_2
execute positioned 168 64 38200 run function mg:lab/lane
execute if score $lbm mg.st matches 0 positioned 168 64 38200 run function mg:lab/maze_0
execute if score $lbm mg.st matches 1 positioned 168 64 38200 run function mg:lab/maze_1
execute if score $lbm mg.st matches 2 positioned 168 64 38200 run function mg:lab/maze_2
execute positioned 210 64 38200 run function mg:lab/lane
execute if score $lbm mg.st matches 0 positioned 210 64 38200 run function mg:lab/maze_0
execute if score $lbm mg.st matches 1 positioned 210 64 38200 run function mg:lab/maze_1
execute if score $lbm mg.st matches 2 positioned 210 64 38200 run function mg:lab/maze_2
execute positioned 252 64 38200 run function mg:lab/lane
execute if score $lbm mg.st matches 0 positioned 252 64 38200 run function mg:lab/maze_0
execute if score $lbm mg.st matches 1 positioned 252 64 38200 run function mg:lab/maze_1
execute if score $lbm mg.st matches 2 positioned 252 64 38200 run function mg:lab/maze_2
execute positioned 294 64 38200 run function mg:lab/lane
execute if score $lbm mg.st matches 0 positioned 294 64 38200 run function mg:lab/maze_0
execute if score $lbm mg.st matches 1 positioned 294 64 38200 run function mg:lab/maze_1
execute if score $lbm mg.st matches 2 positioned 294 64 38200 run function mg:lab/maze_2
