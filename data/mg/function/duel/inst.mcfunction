# Duel sniper — arène $(i) (macro) : un seul duelliste restant = victoire par forfait
$execute store result score #dln mg.st if entity @a[tag=mg.dl,scores={mg.dli=$(i)}]
$execute if score #dln mg.st matches 1 as @a[tag=mg.dl,scores={mg.dli=$(i)}] run function mg:duel/left
