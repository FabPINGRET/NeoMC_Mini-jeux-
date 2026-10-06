# Pluie d'Enclumes — variante « sol troué » : de temps en temps, un trou 3x3 s'ouvre dans le sol
scoreboard players remove $hc mg.st 1
execute if score $hc mg.st matches ..0 run function mg:anvil/hole_event
execute as @e[type=minecraft:marker,tag=mg.hl] at @s run function mg:anvil/hole_marker
