# @s : nouvelle boule (repère de la piste #ln)
tag @s remove mg.bnew
scoreboard players operation @s mg.bln = #ln mg.st
scoreboard players operation @s mg.bcx = #cx mg.st
scoreboard players operation @s mg.bx = #lx mg.st
scoreboard players set @s mg.bz 0
scoreboard players operation @s mg.bvx = #vx mg.st
scoreboard players operation @s mg.bvz = #vz mg.st
scoreboard players operation @s mg.bsp = #sp mg.st
execute if score #ln mg.st matches 0 run data modify entity @s item.id set value "minecraft:ender_pearl"
execute if score #ln mg.st matches 1 run data modify entity @s item.id set value "minecraft:magma_cream"
execute if score #ln mg.st matches 2 run data modify entity @s item.id set value "minecraft:slime_ball"
execute if score #ln mg.st matches 3 run data modify entity @s item.id set value "minecraft:fire_charge"
execute if score #ln mg.st matches 4 run data modify entity @s item.id set value "minecraft:snowball"
execute if score #ln mg.st matches 5 run data modify entity @s item.id set value "minecraft:ender_eye"
execute if score #ln mg.st matches 6 run data modify entity @s item.id set value "minecraft:heart_of_the_sea"
execute if score #ln mg.st matches 7 run data modify entity @s item.id set value "minecraft:firework_star"
function mg:bowl/pos
