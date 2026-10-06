# Sheep War — recharge périodique de munitions (période et quantité selon le nombre de joueurs)
scoreboard players operation $sr mg.st = $srp mg.st
execute as @a[tag=mg.play] run function mg:sheepwar/give_roll
execute if score $srn mg.st matches 2.. as @a[tag=mg.play] run function mg:sheepwar/give_roll
