# @s = kart : couleur (bloc) et modèle 3D (pack) selon ses mg.kty / mg.kcol
execute if score $rp mg.st matches 0 if score @s mg.kcol matches 1 run data modify entity @s block_state.Name set value "minecraft:red_concrete"
execute if score $rp mg.st matches 0 if score @s mg.kcol matches 2 run data modify entity @s block_state.Name set value "minecraft:blue_concrete"
execute if score $rp mg.st matches 0 if score @s mg.kcol matches 3 run data modify entity @s block_state.Name set value "minecraft:lime_concrete"
execute if score $rp mg.st matches 0 if score @s mg.kcol matches 4 run data modify entity @s block_state.Name set value "minecraft:yellow_concrete"
execute if score $rp mg.st matches 0 if score @s mg.kcol matches 5 run data modify entity @s block_state.Name set value "minecraft:purple_concrete"
execute if score $rp mg.st matches 0 if score @s mg.kcol matches 6 run data modify entity @s block_state.Name set value "minecraft:orange_concrete"
execute if score $rp mg.st matches 0 if score @s mg.kcol matches 7 run data modify entity @s block_state.Name set value "minecraft:cyan_concrete"
execute if score $rp mg.st matches 0 if score @s mg.kcol matches 8 run data modify entity @s block_state.Name set value "minecraft:pink_concrete"
execute if score $rp mg.st matches 1 on passengers if entity @s[tag=mg.k3d] run kill @s
execute if score $rp mg.st matches 1 run function mg:kart/rp_kart
