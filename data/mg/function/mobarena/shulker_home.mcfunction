# Shulker sorti de l'arène (@s = shulker) : retour sur un point d'appui valide
execute if score $mt mg.st matches 2 run tp @s 11.5 64 1800.5
execute if score $mt mg.st matches 2 run data modify entity @s AttachFace set value 0b
execute if score $mt mg.st matches 10 run tp @s 20.5 67 10700.5
execute if score $mt mg.st matches 10 run data modify entity @s AttachFace set value 5b
