# Le rayon touche un bloc
particle minecraft:smoke ~ ~ ~ 0.05 0.05 0.05 0.01 3
execute if score $gdn mg.st matches 6 run function mg:gun/splash
