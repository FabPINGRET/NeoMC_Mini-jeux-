# Solo : un des 8 coins/bords, au hasard
execute store result score $khr mg.st run random value 0..7
execute if score $khr mg.st matches 0 run spreadplayers -21 35479 1 2 under 83 false @s
execute if score $khr mg.st matches 1 run spreadplayers 21 35479 1 2 under 83 false @s
execute if score $khr mg.st matches 2 run spreadplayers -21 35521 1 2 under 83 false @s
execute if score $khr mg.st matches 3 run spreadplayers 21 35521 1 2 under 83 false @s
execute if score $khr mg.st matches 4 run spreadplayers -22 35500 1 2 under 83 false @s
execute if score $khr mg.st matches 5 run spreadplayers 22 35500 1 2 under 83 false @s
execute if score $khr mg.st matches 6 run spreadplayers 0 35478 1 2 under 83 false @s
execute if score $khr mg.st matches 7 run spreadplayers 0 35522 1 2 under 83 false @s
