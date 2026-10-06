# Mob Arena (thèmes à 20 vagues) — construit l'arène puis place les joueurs (planifié depuis prepare_x)
execute unless score $state mg.st matches 1 run return 0
execute if score $mt mg.st matches 6 run function mg:mobarena/cathedral/build
execute if score $mt mg.st matches 7 run function mg:mobarena/lab/build
execute if score $mt mg.st matches 8 run function mg:mobarena/temple/build
execute if score $mt mg.st matches 9 run function mg:mobarena/forge/build
execute if score $mt mg.st matches 10 run function mg:mobarena/ship/build
function mg:mobarena/spawn_all
# Contrôle : la Forge doit avoir son sol — sinon 2e tentative et alerte
execute if score $mt mg.st matches 9 if block 0 65 10290 minecraft:air run tellraw @a[tag=mg.admin] [{"text":"[Mob Arena] ","color":"dark_green"},{"text":"La carte de la Forge n'a pas pu être construite (2e tentative).","color":"red"}]
execute if score $mt mg.st matches 9 if block 0 65 10290 minecraft:air run schedule function mg:mobarena/xbuild2 20t
