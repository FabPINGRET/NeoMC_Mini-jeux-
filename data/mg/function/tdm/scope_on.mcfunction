# Lunette en place (renouvelée à chaque tick tant que mg.gads est posé)
tag @s add mg.tmsc
effect give @s minecraft:slowness 1 6 true
title @s times 0 5 2
execute if score $rp mg.st matches 1 run title @s title {"text":"","font":"mg:gta","color":"white","shadow_color":0}
execute unless score $rp mg.st matches 1 run title @s title {"text":"+","color":"white"}
