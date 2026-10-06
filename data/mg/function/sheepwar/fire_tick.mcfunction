# Flammes du mouton de feu (@s = marqueur, à sa position) : le feu se propage (rayon +1 toutes les 0,5 s, de 3 à 8), puis tout s'éteint
scoreboard players remove @s mg.t 1
execute if score @s mg.t matches 130 run fill ~-4 ~ ~-4 ~4 ~ ~4 minecraft:fire replace minecraft:air
execute if score @s mg.t matches 130 run particle minecraft:flame ~ ~0.5 ~ 2.4 0.3 2.4 0.05 30
execute if score @s mg.t matches 130 run playsound minecraft:block.fire.ambient master @a ~ ~ ~ 1 0.8
execute if score @s mg.t matches 120 run fill ~-5 ~ ~-5 ~5 ~ ~5 minecraft:fire replace minecraft:air
execute if score @s mg.t matches 120 run particle minecraft:flame ~ ~0.5 ~ 3.0 0.3 3.0 0.05 30
execute if score @s mg.t matches 120 run playsound minecraft:block.fire.ambient master @a ~ ~ ~ 1 0.8
execute if score @s mg.t matches 110 run fill ~-6 ~ ~-6 ~6 ~ ~6 minecraft:fire replace minecraft:air
execute if score @s mg.t matches 110 run particle minecraft:flame ~ ~0.5 ~ 3.6 0.3 3.6 0.05 30
execute if score @s mg.t matches 110 run playsound minecraft:block.fire.ambient master @a ~ ~ ~ 1 0.8
execute if score @s mg.t matches 100 run fill ~-7 ~ ~-7 ~7 ~ ~7 minecraft:fire replace minecraft:air
execute if score @s mg.t matches 100 run particle minecraft:flame ~ ~0.5 ~ 4.2 0.3 4.2 0.05 30
execute if score @s mg.t matches 100 run playsound minecraft:block.fire.ambient master @a ~ ~ ~ 1 0.8
execute if score @s mg.t matches 90 run fill ~-8 ~ ~-8 ~8 ~ ~8 minecraft:fire replace minecraft:air
execute if score @s mg.t matches 90 run particle minecraft:flame ~ ~0.5 ~ 4.8 0.3 4.8 0.05 30
execute if score @s mg.t matches 90 run playsound minecraft:block.fire.ambient master @a ~ ~ ~ 1 0.8
execute if score @s mg.t matches 80 run fill ~-8 ~ ~-8 ~8 ~ ~8 minecraft:fire replace minecraft:air
execute if score @s mg.t matches 70 run fill ~-8 ~ ~-8 ~8 ~ ~8 minecraft:fire replace minecraft:air
execute if score @s mg.t matches 60 run fill ~-8 ~ ~-8 ~8 ~ ~8 minecraft:fire replace minecraft:air
execute if score @s mg.t matches 50 run fill ~-8 ~ ~-8 ~8 ~ ~8 minecraft:fire replace minecraft:air
execute if score @s mg.t matches 40 run fill ~-8 ~ ~-8 ~8 ~ ~8 minecraft:fire replace minecraft:air
execute if score @s mg.t matches 30 run fill ~-8 ~ ~-8 ~8 ~ ~8 minecraft:fire replace minecraft:air
execute if score @s mg.t matches ..0 run fill ~-8 ~ ~-8 ~8 ~ ~8 minecraft:air replace minecraft:fire
execute if score @s mg.t matches ..0 run kill @s
