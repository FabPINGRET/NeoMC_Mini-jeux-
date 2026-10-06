# La Forge du Titan — tick
# Niveau de lave : un palier toutes les 5 vagues (vagues 6, 11 et 16)
execute if score $wv mg.st matches 6.. if score $lvl mg.st matches 0 run function mg:mobarena/forge/raise1
execute if score $wv mg.st matches 11.. if score $lvl mg.st matches 1 run function mg:mobarena/forge/raise2
execute if score $wv mg.st matches 16.. if score $lvl mg.st matches 2 run function mg:mobarena/forge/raise3
execute as @e[tag=mg.meteor] at @s run function mg:mobarena/forge/meteor_tick
execute if entity @e[tag=mg.boss] run function mg:mobarena/forge/boss_tick
