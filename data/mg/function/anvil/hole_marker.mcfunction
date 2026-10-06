# Trou en cours (@s = marqueur au centre, à sa position)
scoreboard players remove @s mg.t 1
execute if score @s mg.t matches 181..219 run particle minecraft:flame ~ ~0.3 ~ 1 0 1 0.01 4
execute if score @s mg.t matches 180 run function mg:anvil/hole_open
execute if score @s mg.t matches ..0 run function mg:anvil/hole_close
