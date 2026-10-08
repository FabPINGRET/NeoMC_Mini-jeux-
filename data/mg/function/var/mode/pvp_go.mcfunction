# Arène PvP, variante : kit selon la difficulté (appelé à la fin de pvp/go). Généré.
execute if score $dif mg.st matches 1 run give @a[tag=mg.play] minecraft:golden_apple 2
execute if score $dif mg.st matches 1 run give @a[tag=mg.play] minecraft:arrow 16
execute if score $dif mg.st matches 3.. run item replace entity @a[tag=mg.play] weapon.offhand with minecraft:air
execute if score $dif mg.st matches 3 run clear @a[tag=mg.play] minecraft:golden_apple 1
execute if score $dif mg.st matches 4 run clear @a[tag=mg.play] minecraft:golden_apple
execute if score $dif mg.st matches 4 run item replace entity @a[tag=mg.play] armor.chest with minecraft:leather_chestplate
execute if score $dif mg.st matches 4 run tellraw @a[tag=mg.play] {"text":"★★★★ Pas de bouclier, pas de pomme d’or, plastron en cuir : chaque coup compte.","color":"red"}
