# Seconde tentative de construction (Forge)
execute unless score $state mg.st matches 1..2 run return 0
execute if score $mt mg.st matches 9 run forceload add -40 10260 40 10340
execute if score $mt mg.st matches 9 run function mg:mobarena/forge/build
execute if score $mt mg.st matches 9 run function mg:mobarena/spawn_all
execute if score $mt mg.st matches 9 if block 0 65 10290 minecraft:air run tellraw @a[tag=mg.admin] [{"text":"[Mob Arena] ","color":"dark_green"},{"text":"Échec : la Forge ne se construit pas. Lance /function mg:core/setup_build puis relance la partie.","color":"red"}]
