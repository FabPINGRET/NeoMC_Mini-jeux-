# Quelqu'un est dans la galerie : clics sur les piédestaux
execute as @e[type=minecraft:interaction,tag=mg.hati] if data entity @s interaction run function mg:hat/click
execute as @e[type=minecraft:interaction,tag=mg.hati] if data entity @s attack run function mg:hat/click
