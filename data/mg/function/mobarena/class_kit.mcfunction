# Mob Arena — remplace le kit de base par celui de la classe choisie (@s, mg.cl 2..8 ; 1 = Guerrier = kit de base)
clear @s minecraft:iron_sword
clear @s minecraft:bow
clear @s minecraft:arrow
execute if score @s mg.cl matches 2 run function mg:mobarena/class/archer
execute if score @s mg.cl matches 3 run function mg:mobarena/class/tank
execute if score @s mg.cl matches 4 run function mg:mobarena/class/assassin
execute if score @s mg.cl matches 5 run function mg:mobarena/class/mage
execute if score @s mg.cl matches 6 run function mg:mobarena/class/pyro
execute if score @s mg.cl matches 7 run function mg:mobarena/class/berserker
execute if score @s mg.cl matches 8 run function mg:mobarena/class/poseidon
